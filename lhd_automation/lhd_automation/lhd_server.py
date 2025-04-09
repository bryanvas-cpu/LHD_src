#!/usr/bin/env python3
import rclpy
import time
import math
import threading
from rclpy.node import Node
from rclpy.action import ActionServer, GoalResponse, CancelResponse
from rclpy.action.server import ServerGoalHandle
from lhd_msgs.action import NavToWaypoint
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup
from geometry_msgs.msg import Pose2D, TransformStamped, Twist, PoseStamped
from tf2_ros import TransformListener, Buffer
from tf_transformations import quaternion_from_euler, euler_from_quaternion
from lhd_automation.MPC_diff_drive_class import DiffDriveNMPC
import numpy as np
from nav_msgs.msg import Path

class NavToWaypointServerNode(Node):
    def __init__(self):
        self.current_pose = Pose2D()
        # for acquisition of current_pose        
        self.current_pose.x = 0.0
        self.current_pose.y = 0.0
        self.current_pose.theta = 0.0
        
        self.trajectory_remaining = []
        self.current_trajectory = []
        
        self.starting_pose = self.current_pose
        
        super().__init__("lhd_server")
        self.goal_handle_: ServerGoalHandle = None
        self.goal_lock_ = threading.Lock()
        self.count_until_server_ = ActionServer(
            self, 
            NavToWaypoint, 
            "nav_to_waypoint",
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback,
            execute_callback=self.execute_callback,
            callback_group=ReentrantCallbackGroup())
        self.get_logger().info("Action server has been started")
        
        self.control_horizon = 20
        self.MPC_solver = DiffDriveNMPC(dt=0.02, N=self.control_horizon)
        
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        
        self.vel_pub = self.create_publisher(Twist, "auto_vel", 10)
        self.traj_pub = self.create_publisher(Path, "/mpc_path", 10)
        
    def goal_callback(self, goal_request: NavToWaypoint.Goal):
        self.get_logger().info("Received a goal")

        # Validate the goal request
        if not goal_request.waypoints:
            self.get_logger().info("Rejecting the goal")
            return GoalResponse.REJECT
        
        # Policy: preempt existing goal when receiving new goal
        with self.goal_lock_:
            if self.goal_handle_ is not None and self.goal_handle_.is_active:
                self.get_logger().info("Abort current goal and accept new goal")
                self.goal_handle_.abort()
    
        self.get_logger().info("Accepting the goal")
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info("Received a cancel request")
        return CancelResponse.ACCEPT # or REJECT

    def execute_callback(self, goal_handle: ServerGoalHandle):
        # get current nav2 location of base_footprint, wrt odom
        start_time = time.time()
        with self.goal_lock_:
            self.goal_handle_ = goal_handle
        
        # Get request from goal
        # target_pose = goal_handle.request.waypoint
        self.current_trajectory=[]
        i = 0
        for pose in goal_handle.request.waypoints.poses:
            i += 1
            x = pose.position.x
            y = pose.position.y
            q = (pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w)
            _, _, theta = euler_from_quaternion(q)
            self.current_trajectory.append([x, y, theta])
            # self.get_logger().info(f"traj[{i}]: {x:.2f}, {y:.2f}, {theta:.2f}")

        # Execute the action
        self.get_logger().info("Executing the goal")
        feedback = NavToWaypoint.Feedback()
        result = NavToWaypoint.Result()
        
        self.trajectory_remaining = self.current_trajectory.copy()
        if self.current_trajectory:
            final_point = self.current_trajectory[-1]
            for _ in range(self.control_horizon):
                self.trajectory_remaining.append(final_point)
        
        path_msg = Path()
        path_msg.header.frame_id = "map"  # or "odom" depending on your TF tree
        while(True):
            self.get_logger().info(f"trajectory_remaining: {len(self.trajectory_remaining)}")

            if not goal_handle.is_active:
                result.time_taken = time.time() - start_time
                # self.process_next_goal_in_queue()
                return result
            if goal_handle.is_cancel_requested:
                self.get_logger().info("Canceling the goal")
                goal_handle.canceled()
                result.time_taken = time.time() - start_time
                # self.process_next_goal_in_queue()
                return result
            if len(self.trajectory_remaining) <= self.control_horizon:
                self.get_logger().info("Trajectory complete.")
                twist_msg = Twist()
                twist_msg.linear.x = 0.0
                twist_msg.angular.z = 0.0
                self.vel_pub.publish(twist_msg)
                break
            
            try:
                now = rclpy.time.Time()
                trans: TransformStamped = self.tf_buffer.lookup_transform('map', 'base_footprint', now)
                self.current_pose.x = trans.transform.translation.x
                self.current_pose.y = trans.transform.translation.y
                qx = trans.transform.rotation.x
                qy = trans.transform.rotation.y
                qz = trans.transform.rotation.z
                qw = trans.transform.rotation.w
                roll, pitch, yaw = euler_from_quaternion([qx, qy, qz, qw])
                self.current_pose.theta = yaw
                # Store or print
                # self.get_logger().info(f'Position: x={self.current_pose.x:.2f}, y={self.current_pose.y:.2f} | yaw={self.current_pose.theta:.2f} rad')
            except Exception as e:
                self.get_logger().warn(f'Could not get transform: {e}')
            
            target = self.trajectory_remaining[0]
            dx = target[0] - self.current_pose.x
            dy = target[1] - self.current_pose.y
            distance = np.hypot(dx, dy)

            # If close enough, remove it
            if distance < 0.5:
                self.trajectory_remaining.pop(0)
                self.get_logger().info("Reached waypoint, popping from trajectory.")
            else:
                # Use NMPC to compute control
                x0 = np.array([self.current_pose.x, self.current_pose.y, self.current_pose.theta])
                traj_arr = np.array(self.trajectory_remaining[:self.MPC_solver.N + 1])
                x_ref = traj_arr[:, 0]
                y_ref = traj_arr[:, 1]
                theta_ref = traj_arr[:, 2]

                path_msg.header.stamp = self.get_clock().now().to_msg()
                for i in range(traj_arr.shape[0]):
                    pose = PoseStamped()
                    pose.header.frame_id = "map"  # must match above
                    pose.header.stamp = path_msg.header.stamp
                    pose.pose.position.x = traj_arr[i, 0]
                    pose.pose.position.y = traj_arr[i, 1]
                    pose.pose.position.z = 0.0

                    # Create orientation from theta
                    theta = traj_arr[i, 2]
                    quat = quaternion_from_euler(0, 0, theta)
                    pose.pose.orientation.x = quat[0]
                    pose.pose.orientation.y = quat[1]
                    pose.pose.orientation.z = quat[2]
                    pose.pose.orientation.w = quat[3]

                    path_msg.poses.append(pose)

                # Publish the path
                self.traj_pub.publish(path_msg)
                # Solve for control
                control_action = self.MPC_solver.solve(x0, x_ref, y_ref, theta_ref)  # -> [v, omega]
                # self.get_logger().info(f"current_pose_x,y,theta: {x0[0]:.2f}, {x0[1]:.2f}, {x0[2]:.2f}, next_target: {x_ref[0]:.2f}, {y_ref[0]:.2f}, {theta_ref[0]:.2f}")
                # self.get_logger().info(f"Control: ({control_action[0]:.2f}, {control_action[1]:.2f}), distance: ({distance:.2f}")
                
                twist_msg = Twist()
                twist_msg.linear.x = control_action[0]
                twist_msg.angular.z = control_action[1]
                self.vel_pub.publish(twist_msg)
            
            feedback.current_x_y_theta.data = [self.current_pose.x, self.current_pose.y ,self.current_pose.theta]
            
            goal_handle.publish_feedback(feedback)
            
            time.sleep(0.02)

        # Once done, set goal final state
        goal_handle.succeed()

        # and send the result        
        result.time_taken = float(time.time() - start_time)
        
        return result

def main(args=None):
    rclpy.init(args=args)
    node = NavToWaypointServerNode()
    rclpy.spin(node, MultiThreadedExecutor())
    rclpy.shutdown()


if __name__ == "__main__":
    main()
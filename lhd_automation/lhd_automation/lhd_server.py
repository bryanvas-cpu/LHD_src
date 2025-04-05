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
from geometry_msgs.msg import Pose
from tf_transformations import quaternion_from_euler

class NavToWaypointServerNode(Node):
    def __init__(self):
        
        self.current_position = Pose()
        self.current_position.position.x = 119.0
        self.current_position.position.y = 111.0
        self.current_position.position.z = 0.0
        
        initial_q = quaternion_from_euler(0,0,0)
        
        self.current_position.orientation.x = initial_q[0]
        self.current_position.orientation.y = initial_q[1]
        self.current_position.orientation.z = initial_q[2]
        self.current_position.orientation.w = initial_q[3]
        
        super().__init__("count_until_server")
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

    def goal_callback(self, goal_request: NavToWaypoint.Goal):
        self.get_logger().info("Received a goal")

        # Validate the goal request
        if goal_request.waypoint.position.x >= 530 or goal_request.waypoint.position.x <= 20 or goal_request.waypoint.position.y >= 370 or goal_request.waypoint.position.y <= 0:
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
        start_time = time.time()
        with self.goal_lock_:
            self.goal_handle_ = goal_handle
        
        # Get request from goal
        target_pose = goal_handle.request.waypoint

        # Execute the action
        self.get_logger().info("Executing the goal")
        feedback = NavToWaypoint.Feedback()
        result = NavToWaypoint.Result()
        
        
        while(True):
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
            dist = [target_pose.position.x-self.current_position.position.x, target_pose.position.y-self.current_position.position.y]

            if (dist[0] >= 0.1 or dist[0] <= -0.1):
                self.current_position.position.x += 0.5 * dist[0]
            if (dist[1] >= 0.1 or dist[1] <= -0.1):
                self.current_position.position.y += 0.5 * dist[1]
            if (dist[0] < 0.1 and dist[0] > -0.1 and dist[1] < 0.1 and dist[1] > -0.1):
                break
            
            feedback.current_position.pose.position.x = self.current_position.position.x
            feedback.current_position.pose.position.y = self.current_position.position.y
            # feedback.current_position.pose.position.x = self.current_position.position.x
            goal_handle.publish_feedback(feedback)
            time.sleep(0.2)

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
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle, GoalStatus
from lhd_msgs.action import NavToWaypoint
from lhd_msgs.srv import GetWaypoints
from geometry_msgs.msg import PoseArray, Pose
import cv2

class NavToWaypointClientNode(Node):
    def __init__(self):
        super().__init__("lhd_client")
        self.starting_x = 119
        self.starting_y = 111
        self.starting_theta = 0
        
        self.current_x = 119
        self.current_y = 111
        self.current_theta = 0
        
        self.action_client = ActionClient(self, NavToWaypoint, "nav_to_waypoint")
        self.waypoints_client = self.create_client(GetWaypoints,"waypoints")
        
        while not self.waypoints_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

    def send_goal(self, response: GetWaypoints.Response):
        # Wait for the server
        self.action_client.wait_for_server()
        
        trajectory = response.waypoints.poses
        header = response.waypoints.header
        
        # Create and populate the goal
        goal = NavToWaypoint.Goal()
        goal.waypoints = PoseArray()
        goal.waypoints.header = header
        
        transformed_poses = []
        for pose in trajectory:
            real_pose = self.convert_to_real_pose(pose)
            # real_pose = pose
            transformed_poses.append(real_pose)

        goal.waypoints.poses = transformed_poses

        # Send the goal
        self.get_logger().info("Sending goal")
        self.action_client. \
            send_goal_async(goal, feedback_callback=self.goal_feedback_callback). \
                add_done_callback(self.goal_response_callback)

    def cancel_goal(self):
        self.get_logger().info("Send a cancel request")
        self.goal_handle_.cancel_goal_async()
        self.timer_.cancel()

    def goal_response_callback(self, future):
        self.goal_handle_: ClientGoalHandle = future.result()
        if self.goal_handle_.accepted:
           self.get_logger().info("Goal got accepted")
           self.goal_handle_.get_result_async().add_done_callback(self.goal_result_callback)
        else:
            self.get_logger().warn("Goal got rejected")

    def goal_result_callback(self, future):
        status = future.result().status
        result = future.result().result
        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info("Success")
            self.get_logger().info("Got feedback: x: " + str(self.current_x) + " y: " + str(self.current_y) + " theta: " + str(self.current_theta))
        elif status == GoalStatus.STATUS_ABORTED:
            self.get_logger().error("Aborted")
        elif status == GoalStatus.STATUS_CANCELED:
            self.get_logger().warn("Canceled")
        self.get_logger().info("Result: " + str(result.time_taken))
        
    def goal_feedback_callback(self, feedback_msg):
        pose_data = feedback_msg.feedback.current_x_y_theta.data
        pose = self.convert_to_pixel_pose(pose_data)
        # pose = pose_data
        self.current_x, self.current_y, self.current_theta = pose[0], pose[1], pose[2]
        # self.get_logger().info("Got feedback: x: " + str(pose[0]) + " y: " + str(pose[1]) + " theta: " + str(pose[2]))

    def send_request(self, start_x, start_y, end_x, end_y):

            #  complete send_request method, which will send the request and return a future
            req = GetWaypoints.Request()
            req.start.position.x = float(start_x)
            req.start.position.y = float(start_y)
            req.end.position.x = float(end_x)
            req.end.position.y = float(end_y)
            future = self.waypoints_client.call_async(req)
            self.get_logger().info("Waiting for waypoints future")
            rclpy.spin_until_future_complete(self, future)
            self.get_logger().info("received future")
            return future
        
    def convert_to_real_pose(self, pose: Pose):
        real_pose = Pose()
        real_pose = pose
        real_pose.position.x = (pose.position.x - self.starting_x)*(15.0/298.0)
        real_pose.position.y = -(pose.position.y - self.starting_y)*(15.0/298.0)
        # minus since y axis of photo is inverted
        return real_pose
    def convert_to_pixel_pose(self, pose):
        pixel_pose = pose
        pixel_pose[0] = pose[0]*(298.0/15.0) + self.starting_x
        pixel_pose[1] = -pose[1]*(298.0/15.0) + self.starting_y
        # minus since y axis of photo is inverted
        return pixel_pose

def click_callback(event, x, y, flags, param):
    """ Callback for mouse click to capture coordinates """
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"\ngoing from: ({param.current_x}, {param.current_y}) to ({x}, {y})")
        future = param.send_request(param.current_x, param.current_y, x, y)
        response = future.result()
        if response.success == True:
            param.get_logger().info(f"Waypoints received by the action client{response}")
            param.send_goal(response)
        else:
            param.get_logger().info("request_rejected")

def main(args=None):
    rclpy.init(args=args)
    node = NavToWaypointClientNode()

    # Load the map or image
    image_path = "/home/bryan/lhd_ws/src/lhd_mapping/maps/mine/mine_gimp_calibration.png"  # Update with your map image
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if image is None:
        print("Error: Could not load image.")
        return

    cv2.namedWindow("Map")
    cv2.setMouseCallback("Map", click_callback, node)

    while rclpy.ok():
        cv2.imshow("Map", image)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC to exit
            break
        rclpy.spin_once(node, timeout_sec=0.1)

    cv2.destroyAllWindows()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle, GoalStatus
from lhd_msgs.action import NavToWaypoint


class NavToWaypointClientNode(Node):
    def __init__(self):
        super().__init__("count_until_client")
        self.count_until_client_ = ActionClient(self, NavToWaypoint, "nav_to_waypoint")

    def send_goal(self, x, y):
        # Wait for the server
        self.count_until_client_.wait_for_server()

        # Create a goal
        goal = NavToWaypoint.Goal()
        goal.waypoint.position.x = x
        goal.waypoint.position.y = y

        # Send the goal
        self.get_logger().info("Sending goal")
        self.count_until_client_. \
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
        elif status == GoalStatus.STATUS_ABORTED:
            self.get_logger().error("Aborted")
        elif status == GoalStatus.STATUS_CANCELED:
            self.get_logger().warn("Canceled")
        self.get_logger().info("Result: " + str(result.time_taken))

    def goal_feedback_callback(self, feedback_msg):
        position = [feedback_msg.feedback.current_position.pose.position.x, feedback_msg.feedback.current_position.pose.position.y]
        self.get_logger().info("Got feedback: " + str(position[0]) + " " + str(position[1]))


def main(args=None):
    rclpy.init(args=args)
    node = NavToWaypointClientNode()
    node.send_goal(5.0, 1.0)
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
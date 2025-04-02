#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.constants import S_TO_NS
from rclpy.time import Time
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import TwistStamped
from sensor_msgs.msg import JointState
from nav_msgs.msg import Odometry
import numpy as np
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
import math
from tf_transformations import quaternion_from_euler
# create publisher to simple_velocity_controller/commands
# create publisher to simple_position_controller/commands
# create publisher to /bumperbot_controller/odom

# create subscriber to /lhd_controller/cmd_vel -> we get angular and lin vel
# create subscriber to /joint_states -> feedback
# implement diff drive control and turnung angle inverse 
#  kinematics based on ur derivation 

class DrivetrainController(Node):
    def __init__(self):
        super().__init__("drivetrain_controller")
        self.declare_parameter("wheel_radius",0.107)
        self.declare_parameter("wheel_separation",0.279)
        
        self.wheel_radius_ = self.get_parameter("wheel_radius").get_parameter_value().double_value
        self.wheel_separation_ = self.get_parameter("wheel_separation").get_parameter_value().double_value
        
        self.left_wheel_prev_pos_ = 0.0
        self.right_wheel_prev_pos_ = 0.0
        self.x_ = 0.0
        self.y_ = 0.0
        self.theta_ = 0.0
        self.l1 = 0.261
        self.l2 = 0.223

        self.vel_sub_ = self.create_subscription(TwistStamped, "lhd_controller/cmd_vel", self.velCallback, 10)
        self.joint_sub_ = self.create_subscription(JointState,"joint_states", self.jointCallback, 10)     
        
        self.wheel_cmd_pub_ = self.create_publisher(Float64MultiArray, "simple_velocity_controller/commands", 10)
        self.front_angle_cmd_pub_ = self.create_publisher(Float64MultiArray, "simple_position_controller/commands", 10)   
        self.odom_pub_ = self.create_publisher(Odometry, "lhd_controller/odom", 10)
        
        self.speed_conversion_ = np.array([[self.wheel_radius_/2, self.wheel_radius_/2],
                                           [self.wheel_radius_/self.wheel_separation_, -self.wheel_radius_/self.wheel_separation_]])
        self.get_logger().info("The conversion matrix is %s" % self.speed_conversion_)
        
        # Fill the Odometry message with invariant parameters
        self.odom_msg_ = Odometry()
        self.odom_msg_.header.frame_id = "odom"
        self.odom_msg_.child_frame_id = "base_footprint"
        self.odom_msg_.pose.pose.orientation.x = 0.0
        self.odom_msg_.pose.pose.orientation.y = 0.0
        self.odom_msg_.pose.pose.orientation.z = 0.0
        self.odom_msg_.pose.pose.orientation.w = 1.0
        
        # Fill the TF message
        self.br_ = TransformBroadcaster(self)
        self.transform_stamped_ = TransformStamped()
        self.transform_stamped_.header.frame_id = "odom"
        self.transform_stamped_.child_frame_id = "base_footprint"
        
        self.prev_time_ = self.get_clock().now()

        
    def velCallback(self, msg):
        # self.get_logger().info("Received cmd_vel message")
        if msg.twist.angular.z != 0:  # Prevent division by zero
            radius_of_curvature = max(-100000, min(100000, msg.twist.linear.x / msg.twist.angular.z))
        else:
            radius_of_curvature = 100000 if msg.twist.linear.x >= 0 else -100000  # Assume a large straight-line motion

        # self.get_logger().info("\n  ROC is %f " % radius_of_curvature)

        if(radius_of_curvature>=0):
            alpha_1 = math.atan(self.l1/max(0.00001,radius_of_curvature))
        else:
            alpha_1 = -math.atan(self.l1/max(0.00001,-radius_of_curvature))
            
        alpha_2 = math.asin(self.l2/math.sqrt(radius_of_curvature**2 + self.l1**2))
        if alpha_1 < 0 or radius_of_curvature < 0:
            alpha_2 = -alpha_2
        alpha = min(max(-0.785,alpha_1+alpha_2),0.785)


        # radius_of_curvature = min(100000,msg.linear.x / max(0.00001,msg.angular.z))
        # alpha = math.atan2(self.l1, radius_of_curvature) + math.asin(self.l2/math.sqrt(max(0.0001, (radius_of_curvature**2 + self.l1**2))))
        front_angle_msg = Float64MultiArray()
        front_angle_msg.data = [alpha]
        
        robot_speed = np.array([[msg.twist.linear.x],
                                [msg.twist.angular.z]])
        wheel_speed = np.matmul(np.linalg.inv(self.speed_conversion_), robot_speed) 

        wheel_speed_msg = Float64MultiArray()
        wheel_speed_msg.data = [wheel_speed[1, 0], -wheel_speed[0, 0]]

        self.front_angle_cmd_pub_.publish(front_angle_msg)
        self.wheel_cmd_pub_.publish(wheel_speed_msg)
        # self.get_logger().info("\n  alpha_1 is %f \n alpha_2 is %f \n " % (alpha_1, alpha_2))
        
    def jointCallback(self, msg):
        # Implements the inverse differential kinematic model
        # Given the position of the wheels, calculates their velocities
        # then calculates the velocity of the robot wrt the robot frame
        # and then converts it in the global frame and publishes the TF
        dp_left = msg.position[3] - self.left_wheel_prev_pos_
        dp_right = -(msg.position[4] - self.right_wheel_prev_pos_)
        dt = Time.from_msg(msg.header.stamp) - self.prev_time_

        # Actualize the prev pose for the next itheration
        self.left_wheel_prev_pos_ = msg.position[3]
        self.right_wheel_prev_pos_ = msg.position[4]
        self.prev_time_ = Time.from_msg(msg.header.stamp)

        # Calculate the rotational speed of each wheel
        fi_left = dp_left / (dt.nanoseconds / S_TO_NS)
        fi_right = dp_right / (dt.nanoseconds / S_TO_NS)

        # Calculate the linear and angular velocity
        linear = (self.wheel_radius_ * fi_right + self.wheel_radius_ * fi_left) / 2
        angular = (self.wheel_radius_ * fi_right - self.wheel_radius_ * fi_left) / self.wheel_separation_

        # Calculate the position increment
        d_s = (self.wheel_radius_ * dp_right + self.wheel_radius_ * dp_left) / 2
        d_theta = (self.wheel_radius_ * dp_right - self.wheel_radius_ * dp_left) / self.wheel_separation_
        self.theta_ += d_theta
        self.x_ += d_s * math.cos(self.theta_)
        self.y_ += d_s * math.sin(self.theta_)
        # self.get_logger().info("\n  joints %.4f %.4f %.4f %.4f%.4f\n " % (msg.position[0], msg.position[1], msg.position[2], msg.position[3], msg.position[4]))
        # print("Callback triggered!")
        # print(msg)
        self.get_logger().info("\n x,y %.4f, %.4f \n " % (self.x_, self.y_))

        
        # Compose and publish the odom message
        q = quaternion_from_euler(0, 0, self.theta_)
        self.odom_msg_.header.stamp = msg.header.stamp
        self.odom_msg_.pose.pose.position.x = self.x_
        self.odom_msg_.pose.pose.position.y = self.y_
        self.odom_msg_.pose.pose.orientation.x = q[0]
        self.odom_msg_.pose.pose.orientation.y = q[1]
        self.odom_msg_.pose.pose.orientation.z = q[2]
        self.odom_msg_.pose.pose.orientation.w = q[3]
        self.odom_msg_.twist.twist.linear.x = linear
        self.odom_msg_.twist.twist.angular.z = angular
        self.odom_pub_.publish(self.odom_msg_)

        # TF
        self.transform_stamped_.transform.translation.x = self.x_
        self.transform_stamped_.transform.translation.y = self.y_
        self.transform_stamped_.transform.rotation.x = q[0]
        self.transform_stamped_.transform.rotation.y = q[1]
        self.transform_stamped_.transform.rotation.z = q[2]
        self.transform_stamped_.transform.rotation.w = q[3]
        self.transform_stamped_.header.stamp = msg.header.stamp
        self.br_.sendTransform(self.transform_stamped_)

def main():
    rclpy.init()

    drivetrain_controller = DrivetrainController()
    rclpy.spin(drivetrain_controller)
    
    drivetrain_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
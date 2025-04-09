import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # use_slam = LaunchConfiguration("use_slam")

    # use_slam_arg = DeclareLaunchArgument(
    #     "use_slam",
    #     default_value="false"
    # )

    gazebo = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("lhd_description"),
            "launch",
            "gazebo.launch.py"
        ),
    )
    
    controller = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("lhd_controller"),
            "launch",
            "controller.launch.py"
        ),
        # launch_arguments={
        #     "use_simple_controller": "True",
        #     "use_python": "True"
        # }.items(),
    )
    
    joystick = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("lhd_controller"),
            "launch",
            "joystick_teleop.launch.py"
        ),
        launch_arguments={
            "use_sim_time": "True"
        }.items()
    )

    return LaunchDescription([
        gazebo,
        controller,
        joystick,
    ])
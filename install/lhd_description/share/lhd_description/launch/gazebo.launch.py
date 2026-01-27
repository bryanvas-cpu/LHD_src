import os
from pathlib import Path
from os import pathsep
from ament_index_python.packages import get_package_share_directory, get_package_prefix

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.substitutions import Command, LaunchConfiguration

from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    lhd_description = get_package_share_directory("lhd_description")

    ros_distro = os.environ["ROS_DISTRO"]
    is_ignition = 'True' if ros_distro=="humble" else "False"

    model_arg = DeclareLaunchArgument(name="model", 
                                      default_value=os.path.join(lhd_description, "urdf", "lhd.urdf.xacro"),
                                      description="Absolute path to robot urdf file"
    )

    robot_description = ParameterValue(Command(["xacro ", LaunchConfiguration("model"),
                                                " is_ignition:=",
                                                is_ignition
                                                ]),
                                       value_type=str)
    
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description}]
    )
    
############################################## mine ############################################
    model_arg_2 = DeclareLaunchArgument(
        name="model_2",
        default_value=os.path.join(lhd_description, "urdf", "mine.urdf.xacro"),  # Different file
        description="Absolute path to second robot URDF file"
    )

    robot_description_2 = ParameterValue(Command(["xacro ", LaunchConfiguration("model_2"),
                                                  " is_ignition:=", is_ignition]),
                                         value_type=str)
    
    robot_state_publisher_node_2 = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        namespace="mine",
        parameters=[
            {"use_sim_time": True},
            {"robot_description": robot_description_2},
        ],
    )



    gazebo_resource_path = SetEnvironmentVariable(
        name="GZ_SIM_RESOURCE_PATH",
        value=str(Path(lhd_description).parent.resolve())
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory("ros_gz_sim"),"launch"), "/gz_sim.launch.py"
        ]),
        launch_arguments=[
            ("gz_args", [" -v 4", " -r", " empty.sdf"])
        ]
    )

    gz_spawn_entity = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=["-topic", "robot_description", "-name", "lhd",
                   "-x", "0.0", "-y", "0.0", "-z", "0.15"]
    )
    
    gz_spawn_entity_2 = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=[
        "-topic", "/mine/robot_description",
        "-name", "mine",
        "-x", "0.0", "-y", "0.0", "-z", "0.15",  # Position
        "-R", "0.0", "-P", "0.0", "-Y", "3.1415"   # Orientation (Roll, Pitch, Yaw in radians)
    ]
    )


    # gz_ros2_bridge = Node(
    #     package="ros_gz_bridge",
    #     executable="parameter_bridge",
    #     arguments=[
    #         "/imu@sensor_msgs/msg/Imu@gz.msgs.IMU"
    #     ],
    #     remappings=[
    #         ("/imu", "/imu/out")
    #     ]
    # )
    gz_ros2_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            "/clock@rosgraph_msgs/msg/Clock@gz.msgs.Clock",
            "/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan"
        ],
        # remappings=[
        #     ('/imu', '/imu/out'),
        # ]
    )

    return LaunchDescription([
        model_arg,
        model_arg_2,
        robot_state_publisher_node,
        robot_state_publisher_node_2,
        gazebo_resource_path,
        gazebo,
        gz_spawn_entity,
        gz_spawn_entity_2,
        gz_ros2_bridge
    ])
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, GroupAction, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    simulation = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("lhd_bringup"),
            "launch",
            "simulated_robot.launch.py"
        )
    
    )
    
    localization = TimerAction(
        period=5.0,
        actions=[
            IncludeLaunchDescription(
                os.path.join(
                    get_package_share_directory("lhd_localization"),
                    "launch",
                    "global_localization.launch.py"
                )
                
            )
        ]
    )
    
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", os.path.join(get_package_share_directory("lhd_localization"), "rviz", "amcl_particle_cloud_path.rviz")],
    )
    
    system = GroupAction(
        actions=[
            TimerAction(
                period=5.0,
                actions=[
                    Node(package="lhd_automation", executable="lhd_client.py", output="screen"),
                    Node(package="lhd_automation", executable="lhd_server.py", output="screen"),
                    Node(package="lhd_automation", executable="path_planning_service.py", output="screen")
                ]
            )
        ]
    )

    return LaunchDescription([
        simulation,
        localization,
        rviz_node,
        system
    ])

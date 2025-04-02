from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, OpaqueFunction
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.conditions import UnlessCondition, IfCondition
from launch.actions import TimerAction


def generate_launch_description():
    group = GroupAction(
        actions=[
            Node(
                package="lhd_controller",
                executable="drivetrain_controller.py"
            )
            # Node(
            #     package="lhd_controller",
            #     executable="arm_controller"
            # )
        ]
    )

    
    joint_state_broadcaster_spawner = TimerAction(
        period=2.0,  # Delay of 2 seconds
        actions=[
            Node(
                package="controller_manager",
                executable="spawner",
                arguments=[
                    "joint_state_broadcaster",
                    "--controller-manager",
                    "/controller_manager"
                ]
            )
        ]
    )

    simple_drivetrain_controller = GroupAction(
        actions=[
            TimerAction(
                period=4.0,  # Delay in seconds
                actions=[
                    Node(
                        package="controller_manager",
                        executable="spawner",
                        arguments=[
                            "simple_velocity_controller",
                            "--controller-manager",
                            "/controller_manager"
                        ]
                    ),
                    Node(
                        package="controller_manager",
                        executable="spawner",
                        arguments=[
                            "simple_position_controller",
                            "--controller-manager",
                            "/controller_manager"
                        ]
                    )
                ]
            )
        ]
    )

    # lhd_controller = Node(
    #             package="lhd_controller",
    #             executable="drivetrain_controller.py"
    #         )

    
    # joint_state_broadcaster = Node(
    #             package="controller_manager",
    #             executable="spawner",
    #             arguments=[
    #                 "joint_state_broadcaster",
    #                 "--controller-manager",
    #                 "/controller_manager"
    #             ]
    #         )

    # simple_velocity_controller = Node(
    #                     package="controller_manager",
    #                     executable="spawner",
    #                     arguments=[
    #                         "simple_velocity_controller",
    #                         "--controller-manager",
    #                         "/controller_manager"
    #                     ]
    #                 )
    # simple_position_controller = Node(
    #                     package="controller_manager",
    #                     executable="spawner",
    #                     arguments=[
    #                         "simple_position_controller",
    #                         "--controller-manager",
    #                         "/controller_manager"
    #                     ]
    #                 )


    return LaunchDescription(
        [
            joint_state_broadcaster_spawner,
            simple_drivetrain_controller,
            group
        ]
    )
    # return LaunchDescription(
    #     [
    #         lhd_controller,
    #         joint_state_broadcaster,
    #         simple_velocity_controller,
    #         simple_position_controller
    #     ]
    # )
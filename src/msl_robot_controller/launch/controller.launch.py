from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    msl_robot_controller_config = os.path.join(
        get_package_share_directory("msl_robot_controller"),
        "config",
        "msl_robot_controllers.yaml"
    )

    # Launch the controller manager node
    controller_manager_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[msl_robot_controller_config], 
        output="screen",
        arguments=["--ros-args", "--log-level", "INFO"],
    )

    # Spawn the joint_state_broadcaster
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
    )

    # Add your primary ROS 2 controller here if needed
    wheel_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["msl_robot_controller", "--controller-manager", "/controller_manager"],
    )

    return LaunchDescription(
        [
            controller_manager_node,
            joint_state_broadcaster_spawner,
            wheel_controller_spawner,
        ]
    )

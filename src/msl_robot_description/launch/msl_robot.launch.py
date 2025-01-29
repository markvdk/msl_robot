from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Get package directories
    msl_robot_desc_dir = get_package_share_directory('msl_robot_description')
    msl_robot_ctrl_dir = get_package_share_directory('msl_robot_controller')
    
    # Include gazebo.launch.py
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(msl_robot_desc_dir, 'launch', 'gazebo.launch.py')
        )
    )

    # Include controller.launch.py
    controller_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(msl_robot_ctrl_dir, 'launch', 'controller.launch.py')
        )
    )
    
    # Start joy_node
    joy_node = Node(
        package='joy',
        executable='joy_node',
        name='joy_node',
        output='screen'
    )

    # Include joystick_teleop.launch.py
    joystick_teleop_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(msl_robot_ctrl_dir, 'launch', 'joystick_teleop.launch.py')
        )
    )

    return LaunchDescription([
        gazebo_launch,
        controller_launch,
        joy_node,
        joystick_teleop_launch
    ])

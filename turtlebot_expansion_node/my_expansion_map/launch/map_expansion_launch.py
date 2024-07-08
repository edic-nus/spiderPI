from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_expansion_map',
            executable='map_expansion_node',
            name='map_expansion_node',
            output='screen'),
    ])

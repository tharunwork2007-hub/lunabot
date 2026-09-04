from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=[
                'gz', 'sim', '-r',
                '/home/tharunkumar/lunabot_ws/src/lunabot_description/worlds/lunar_world.sdf'
            ],
            output='screen'
        ),

        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-file',
                '/home/tharunkumar/lunabot_ws/src/lunabot_description/urdf/lunabot.urdf',
                '-name',
                'lunabot',
                '-x', '0',
                '-y', '0',
                '-z', '0.6'
            ],
            output='screen'
        ),
    ])

from launch import LaunchDescription
from launch_ros.actions import Node
#if you run the launch file using ros2 launch after changing the parameter values, you need to rerun colcon build
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_serial_interface',
            executable='serial_controller',
            name='serial_controller_node',
            output='screen',
            emulate_tty=True,
            parameters=[
                {'device': '/dev/ttyACM0'},
                {'wheel_instructions_topic': 'wheel_instructions_topic'},
                {'move_forward_lin_vel': 1.0},
                {'move_backward_lin_vel': -1.0},
                {'turn_left_ang_vel': 1.0},
                {'turn_right_ang_vel': -1.0},
                {'move_forward_val': 'w'},
                {'move_backward_val': 's'},
                {'turn_right_val': 'd'},
                {'turn_left_val': 'a'},
                {'stop_val': 'x'}
            ]
        )
    ])
import rclpy
from rclpy.node import Node
#from pynput.keyboard import Key, Listener, KeyCode
# Handle Twist messages, linear and angular velocity
from geometry_msgs.msg import Twist
import time
def run_publisher(node):
    #msg.data = 'Up key pressed'
    msg = Twist()
    msg.linear.x = 1.0
    node.publisher_.publish(msg)
    time.sleep(0.25)
    #msg.data = 'Down key pressed'
    msg = Twist()
    msg.linear.x = -1.0
    node.publisher_.publish(msg)
    time.sleep(0.25)
    #msg.data = 'Left key pressed'
    msg = Twist()
    msg.angular.z = 1.0
    node.publisher_.publish(msg)
    time.sleep(0.25)
    #msg.data = 'Right key pressed'
    msg = Twist()
    msg.angular.z = -1.0
    node.publisher_.publish(msg)
    time.sleep(0.25)
class KeyboardPublisher(Node):
    def __init__(self):
        super().__init__('keyboard_publisher')
        self.publisher_ = self.create_publisher(Twist, 'wheel_instructions_topic', 10)
        self.isFinished = False

def main(args=None):
    rclpy.init(args=args)

    keyboard_publisher = KeyboardPublisher()
    run_publisher(keyboard_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    keyboard_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

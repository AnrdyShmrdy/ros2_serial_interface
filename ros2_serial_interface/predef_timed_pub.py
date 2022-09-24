#This program publishes predefined messages to a ROS2 topic at timed intervals
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
def run_publisher(node):
    msg = Twist()
    msg.linear.x = 1.0
    node.publisher_.publish(msg)
    time.sleep(0.25)

    msg = Twist()
    msg.linear.x = -1.0
    node.publisher_.publish(msg)
    time.sleep(0.25)

    msg = Twist()
    msg.angular.z = 1.0
    node.publisher_.publish(msg)
    time.sleep(0.25)

    msg = Twist()
    msg.angular.z = -1.0
    node.publisher_.publish(msg)
    time.sleep(0.25)
class Publisher(Node):
    def __init__(self):
        super().__init__('publisher')
        self.publisher_ = self.create_publisher(Twist, 'wheel_instructions_topic', 10)
        self.isFinished = False

def main(args=None):
    rclpy.init(args=args)

    publisher = Publisher()
    run_publisher(publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

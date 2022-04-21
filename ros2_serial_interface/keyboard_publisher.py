import rclpy
from rclpy.node import Node
from pynput.keyboard import Key, Listener, KeyCode
# Handle Twist messages, linear and angular velocity
from geometry_msgs.msg import Twist

def run_publisher(node):
    while (node.isFinished == False):
        def onpress(key):
            msg = Twist()
            if isinstance(key, KeyCode): #lets us know if we can safely use key.char
                if key.char == 'w':
                    #msg.data = 'Up key pressed'
                    msg.linear.x = 1.0
                    node.publisher_.publish(msg)
                    return False
                elif key.char == 's':
                    #msg.data = 'Down key pressed'
                    msg.linear.x = -1.0
                    node.publisher_.publish(msg)
                    return False
                elif key.char == 'a':
                    #msg.data = 'Left key pressed'
                    msg.angular.z = 1.0
                    node.publisher_.publish(msg)
                    return False
                elif key.char == 'd':
                    #msg.data = 'Right key pressed'
                    msg.angular.z = -1.0
                    node.publisher_.publish(msg)
                    return False
            elif key == Key.esc:
            # Stop listener
                node.isFinished = True
                return False
        def onrelease(key):
            if isinstance(key, KeyCode): #lets us know if we can safely use key.char
                if key.char in {'w', 's', 'a', 'd'}:
                    node.publisher_.publish(Twist()) #Publishes a Twist message with values of 0. This indicates stopping
                    return False
            elif key == Key.esc:
            # Stop listener
                node.isFinished = True
                return False
        # initialising Listener object   
        with Listener(suppress = True, on_press = onpress) as l: #TODO: Add back suppress = True parameter
            l.join()
        with Listener(suppress = True, on_release = onrelease) as l: #TODO: Add back suppress = True parameter
            l.join()
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

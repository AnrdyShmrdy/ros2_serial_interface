from time import sleep
from xmlrpc.client import Boolean
import rclpy
from pynput import keyboard
from rclpy.node import Node
from pynput.keyboard import Listener
from std_msgs.msg import String

def run_publisher(node):
    while (node.isFinished == False):
        def onpress(key):
            msg = String()
            if key == keyboard.Key.up:
                print('Up key pressed')
                msg.data = 'led4_on'
                node.publisher_.publish(msg)
                return False
            elif key == keyboard.Key.down:
                print('Down key pressed')
                msg.data = 'led1_on'
                node.publisher_.publish(msg)
                return False
            elif key == keyboard.Key.left:
                print('Left key pressed')
                msg.data = 'led3_on'
                node.publisher_.publish(msg)
                return False
            elif key == keyboard.Key.right:
                print('Right key pressed')
                msg.data = 'led2_on'
                node.publisher_.publish(msg)
                return False
            elif key == keyboard.Key.esc:
            # Stop listener
                node.isFinished = True
                return False
        def onrelease(key):
            msg = String()
            if key == keyboard.Key.up:
                print('Up key released')
                msg.data = 'led4_off'
                node.publisher_.publish(msg)
                return False
            elif key == keyboard.Key.down:
                print('Down key released')
                msg.data = 'led1_off'
                node.publisher_.publish(msg)
                return False
            elif key == keyboard.Key.left:
                print('Left key released')
                msg.data = 'led3_off'
                node.publisher_.publish(msg)
                return False
            elif key == keyboard.Key.right:
                print('Right key released')
                msg.data = 'led2_off'
                node.publisher_.publish(msg)
                return False
            elif key == keyboard.Key.esc:
            # Stop listener
                node.isFinished = True
                return False
        #initialising Listener object   
        with Listener(suppress = True, on_press = onpress) as l:
            l.join()
        with Listener(suppress = True, on_release = onrelease) as l:
            l.join()
class KeyboardPublisher(Node):
    def __init__(self):
        super().__init__('keyboard_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
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

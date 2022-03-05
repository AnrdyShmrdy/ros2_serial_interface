import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TimerPublisher(Node):

	def __init__(self):
		super().__init__('timer_publisher')
		self.state = String()
#		TODO: Have topic name grabbed from namespace in .yaml config file
		self.declare_parameter('topic', 'topic') #TODO: Define and set this in a .yaml config file + launch file
		#TODO: Change publisher to fetch the parameter value from a namespace in a .yaml config file
		self.publisher = self.create_publisher(String, 
                                         self.get_parameter('topic').get_parameter_value().string_value, 
                                        10)
		timer_period = 0.25 # second
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0

	def timer_callback(self):
		if self.i % 2 == 0:
			self.state.data = "all_on"
		else:
			self.state.data = "all_off"
		self.publisher.publish(self.state)
		self.get_logger().info('Published Data: {}'.format(self.state.data))
		self.i += 1

def main(args=None):
	rclpy.init(args=args)
	timer_publisher = TimerPublisher()
	rclpy.spin(timer_publisher)

if __name__ == '__main__':
	main()

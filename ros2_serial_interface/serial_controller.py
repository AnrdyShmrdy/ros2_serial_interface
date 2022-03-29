# Node to publish a string topic
import rclpy
from rclpy.node import Node
import serial

# Handle Twist messages, linear and angular velocity
from geometry_msgs.msg import Twist
class SerialController(Node):
	def __init__(self):
		super().__init__('serial_controller')
		#TODO: Try and see if it's possible to use parameters without declaration of default value
		#Default Value declarations of ros2 params:
		self.declare_parameter('device', '/dev/ttyACM0')
		self.declare_parameter('wheel_instructions_topic', 'wheel_instructions_topic')
		self.declare_parameter('move_forward_lin_vel', 1.0)
		self.declare_parameter('move_backward_lin_vel', -1.0)
		self.declare_parameter('turn_left_ang_vel', 1.0)
		self.declare_parameter('turn_right_ang_vel', -1.0)
		self.declare_parameter('move_forward_val', 1)
		self.declare_parameter('move_backward_val', 2)
		self.declare_parameter('turn_right_val', 3)
		self.declare_parameter('turn_left_val', 4)
		self.wheel_topic_name = self.get_parameter('wheel_instructions_topic').get_parameter_value().string_value
		self.device_name = self.get_parameter('device').get_parameter_value().string_value
		self.forward_vel = float(self.get_parameter('move_forward_lin_vel').get_parameter_value().double_value)
		self.backward_vel = float(self.get_parameter('move_backward_lin_vel').get_parameter_value().double_value)
		self.turn_right_vel = float(self.get_parameter('turn_right_ang_vel').get_parameter_value().double_value)
		self.turn_left_vel = float(self.get_parameter('turn_left_ang_vel').get_parameter_value().double_value)
		self.move_forward_val = bin(self.get_parameter('move_forward_val').get_parameter_value().integer_value)
		self.move_backward_val = bin(self.get_parameter('move_backward_val').get_parameter_value().integer_value)
		self.turn_right_val = bin(self.get_parameter('turn_right_val').get_parameter_value().integer_value)
		self.turn_left_val = bin(self.get_parameter('turn_left_val').get_parameter_value().integer_value)
		print(self.device_name)
		print(self.wheel_topic_name)
		print(self.forward_vel)
		print(self.backward_vel)
		print(self.turn_left_vel)
		print(self.turn_right_vel)
		print(self.move_forward_val)
		print(self.move_backward_val)
		print(self.turn_left_val)
		print(self.turn_right_val)
		self.ser = serial.Serial(self.device_name,
                           9600, #Note: Baud Rate must be the same in the arduino program, otherwise signal is not recieved!
                           timeout=4)
		
		self.subscriber = self.create_subscription(Twist, 
                                              self.wheel_topic_name, 
                                              self.serial_listener_callback, 
                                              10)
		self.subscriber # prevent unused variable warning
		self.ser.reset_input_buffer()
	
	def serial_listener_callback(self, msg):
		"""Move Forward"""
		if msg.linear.x == self.forward_vel:
			self.ser.write(self.move_forward_val)
			line = self.ser.readline().decode('utf-8').rstrip()
			print(line) #TODO: "command_name" sent
			print("move-forward: " + str(self.move_forward_val))
		"""Move Backward"""
		if msg.linear.x == self.backward_vel:
			self.ser.write(self.move_backward_val)
			line = self.ser.readline().decode('utf-8').rstrip()
			print(line)  #TODO: "command_name" sent
			print("move-backward: " + str(self.move_backward_val))
		"""Turn Left"""
		if msg.angular.z == self.turn_left_vel:
			self.ser.write(self.turn_left_val)
			line = self.ser.readline().decode('utf-8').rstrip()
			print(line)  #TODO: "command_name" sent
			print("turn-left: " + str(self.turn_left_val))
		"""Turn Right"""
		if msg.angular.z == self.turn_right_vel:
			self.ser.write(self.turn_right_val) #TODO: future format ideally would be "if msg.data == command_value"
			line = self.ser.readline().decode('utf-8').rstrip()
			print(line)  #TODO: "command_name" sent
			print("turn-right: " + str(self.turn_right_val))

def main(args=None):
	rclpy.init(args=args)
	serial_controller = SerialController()
	rclpy.spin(serial_controller)

if __name__ == '__main__':
	main()
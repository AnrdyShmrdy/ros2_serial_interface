# Node to publish a string topic
from time import sleep
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
		self.declare_parameter('transmitting_device', '/dev/ttyS0') #device we are trasmitting messages to
		self.declare_parameter('recieving_device', '/dev/ttyS3') #device we are recieving messages from
		self.declare_parameter('wheel_instructions_topic', 'wheel_instructions_topic')
		self.declare_parameter('move_forward_lin_vel', 1.0)
		self.declare_parameter('move_backward_lin_vel', -1.0)
		self.declare_parameter('turn_left_ang_vel', 1.0)
		self.declare_parameter('turn_right_ang_vel', -1.0)
		self.declare_parameter('move_forward_cmd', 'w')
		self.declare_parameter('move_backward_cmd', 's')
		self.declare_parameter('turn_right_cmd', 'd')
		self.declare_parameter('turn_left_cmd', 'a')
		self.declare_parameter('stop_cmd', 'x')
		self.wheel_topic_name = self.get_parameter('wheel_instructions_topic').get_parameter_value().string_value
		self.recieving_device = self.get_parameter('recieving_device').get_parameter_value().string_value
		self.transmitting_device = self.get_parameter('transmitting_device').get_parameter_value().string_value
		self.forward_vel = float(self.get_parameter('move_forward_lin_vel').get_parameter_value().double_value)
		self.backward_vel = float(self.get_parameter('move_backward_lin_vel').get_parameter_value().double_value)
		self.turn_left_vel = float(self.get_parameter('turn_left_ang_vel').get_parameter_value().double_value)
		self.turn_right_vel = float(self.get_parameter('turn_right_ang_vel').get_parameter_value().double_value)
		self.move_forward_cmd = self.get_parameter('move_forward_cmd').get_parameter_value().string_value
		self.move_backward_cmd = self.get_parameter('move_backward_cmd').get_parameter_value().string_value
		self.turn_left_cmd = self.get_parameter('turn_left_cmd').get_parameter_value().string_value
		self.turn_right_cmd = self.get_parameter('turn_right_cmd').get_parameter_value().string_value
		self.stop_cmd = self.get_parameter('stop_cmd').get_parameter_value().string_value
		print(self.transmitting_device)
		print(self.recieving_device)
		print(self.wheel_topic_name)
		print(self.forward_vel)
		print(self.backward_vel)
		print(self.turn_left_vel)
		print(self.turn_right_vel)
		print(self.move_forward_cmd)
		print(self.move_backward_cmd)
		print(self.turn_left_cmd)
		print(self.turn_right_cmd)
		print(self.stop_cmd)
		self.serial_send = serial.Serial(self.transmitting_device,
				9600, #Note: Baud Rate must be the same in the arduino program, otherwise signal is not recieved!
				timeout=.1)
		self.serial_recieve = serial.Serial(self.recieving_device,
						9600, #Note: Baud Rate must be the same in the arduino program, otherwise signal is not recieved!
						timeout=.1)
		
		self.subscriber = self.create_subscription(Twist, 
                                              self.wheel_topic_name, 
                                              self.serial_listener_callback, 
                                              10)
		self.subscriber # prevent unused variable warning
	def send_cmd(self, cmd):
		print("Sending: " + cmd)
		self.serial_send.write(bytes(cmd,'utf-8'))
	def recieve_cmd(self):
		try:
			#try normal way of recieving data
			sleep(.01) #sleep to allow time for serial_data to arrive. Otherwise this might return nothing
			line = self.serial_recieve.readline().decode('utf-8').rstrip()
		except:
			#if normal way doesn't work, try getting binary representation to see what went wrong
			line = str(self.serial_recieve.readline())
		print("Recieved: " + line)
	def serial_listener_callback(self, msg):
		#NOTE: 
		# For some reason, arduino sends back null byte (0b'' or Oxff) back after the first call to ser.write
		# If the statement in "try" executes when this happens, it causes this error which crashes the program:
		# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
		# To prevent this, I added the try-except blocks to prevent the program from crashing
		# If a null byte is sent, "except" is called which prevents the program from crashing
		"""Move Forward"""
		if msg.linear.x == self.forward_vel:
			self.send_cmd(self.move_forward_cmd)
			self.recieve_cmd()
		"""Move Backward"""
		if msg.linear.x == self.backward_vel:
			self.send_cmd(self.move_backward_cmd)
			self.recieve_cmd()
		"""Turn Left"""
		if msg.angular.z == self.turn_left_vel:
			self.send_cmd(self.turn_left_cmd)
			self.recieve_cmd()
		"""Turn Right"""
		if msg.angular.z == self.turn_right_vel:
			self.send_cmd(self.turn_right_cmd)
			self.recieve_cmd()	
		"""Stop"""
		if msg == Twist():
			self.send_cmd(self.stop_cmd)
			self.recieve_cmd()
			

def main(args=None):
	rclpy.init(args=args)
	serial_controller = SerialController()
	rclpy.spin(serial_controller)

if __name__ == '__main__':
	main()
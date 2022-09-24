# Serial server node
import rclpy
from rclpy.node import Node
import serial

# Handle Twist messages, linear and angular velocity
from geometry_msgs.msg import Twist
class SerialServer(Node):
	def __init__(self):
		super().__init__('serial_server')
		#Default Value declarations of ros2 params:
		self.declare_parameters(
		namespace='',
		parameters=[
			('device', '/dev/ttyACM0'), #device we are trasmitting to & recieving messages from
		    ('wheel_instructions_topic', 'wheel_instructions_topic'),
		    ('move_forward_lin_vel', 1.0),
		    ('move_backward_lin_vel', -1.0),
		    ('turn_left_ang_vel', 1.0),
		    ('turn_right_ang_vel', -1.0),
		    ('move_forward_cmd', 'w'),
		    ('move_backward_cmd', 's'),
		    ('turn_right_cmd', 'd'),
		    ('turn_left_cmd', 'a'),
		    ('stop_cmd', 'x'),
		]
		)
		self.wheel_topic_name = self.get_param_str('wheel_instructions_topic')
		self.device_name = self.get_param_str('device')
		self.forward_vel = self.get_param_float('move_forward_lin_vel')
		self.backward_vel = self.get_param_float('move_backward_lin_vel')
		self.turn_left_vel = self.get_param_float('turn_left_ang_vel')
		self.turn_right_vel = self.get_param_float('turn_right_ang_vel')
		self.move_forward_cmd = self.get_param_str('move_forward_cmd')
		self.move_backward_cmd = self.get_param_str('move_backward_cmd')
		self.turn_left_cmd = self.get_param_str('turn_left_cmd')
		self.turn_right_cmd = self.get_param_str('turn_right_cmd')
		self.stop_cmd = self.get_param_str('stop_cmd')
		self.ser = serial.Serial(self.device_name,
                           9600, #Note: Baud Rate must be the same in the arduino program, otherwise signal is not recieved!
                           timeout=.1)
		
		self.subscriber = self.create_subscription(Twist, 
                                              self.wheel_topic_name, 
                                              self.serial_listener_callback, 
                                              10)
		self.subscriber # prevent unused variable warning
		self.ser.reset_input_buffer()
	def get_param_float(self, name):
		try:
			return float(self.get_parameter(name).get_parameter_value().double_value)
		except:
			pass
	def get_param_str(self, name):
		try:
			return self.get_parameter(name).get_parameter_value().string_value
		except:
			pass
	def send_cmd(self, cmd):
		print("Sending: " + cmd)
		self.ser.write(bytes(cmd,'utf-8'))
	def recieve_cmd(self):
		try:
			#try normal way of recieving data
			#sleep(.01) #sleep to allow time for serial_data to arrive. Otherwise this might return nothing
			line = self.ser.readline().decode('utf-8').rstrip()
		except:
			#if normal way doesn't work, try getting binary representation to see what went wrong
			line = str(self.ser.readline())
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
	serial_server = SerialServer()
	rclpy.spin(serial_server)

if __name__ == '__main__':
	main()
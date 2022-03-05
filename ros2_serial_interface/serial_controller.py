# Node to publish a string topic
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
#TODO: Create a launch file for this Node
class SerialController(Node):
	def __init__(self):
		super().__init__('serial_controller')
		self.declare_parameter('device', '/dev/ttyACM0') #TODO: Define and set this in a .yaml config file + launch file
		self.declare_parameter('topic', 'topic') #TODO: Define and set this in a .yaml config file + launch file
		#Example of Potential robot command: self.declare_paramter('turnLeft', 'leftMotorRoutine') 
		
  		#TODO: Change below line to fetch the parameter value from a namespace in a .yaml config file
		self.ser = serial.Serial(self.get_parameter('device').get_parameter_value().string_value,
                           9600, #Note: Baud Rate must be the same in the arduino program, otherwise signal is not recieved!
                           timeout=4)
		
  		#TODO: Change below subscription to fetch the parameter value from a namespace in a .yaml config file
		self.subscriber = self.create_subscription(String, 
                                              self.get_parameter('topic').get_parameter_value().string_value, 
                                              self.serial_listener_callback, 
                                              10)
		self.subscriber # prevent unused variable warning
		self.ser.reset_input_buffer()
	
	def serial_listener_callback(self, msg):
		#TODO: Change this so that commands are derived from a variable array of paramters. 
  		#TODO: Make it so that we can avoid editing this function in the future by editing the paramater values
		if msg.data == "all_on": #TODO: future format ideally would be "if msg.data == command_paramater"
			self.ser.write(b'9') #TODO: future format ideally would be "if msg.data == command_value"
			line = self.ser.readline().decode('utf-8').rstrip()
			print(line) #TODO: "command_name" sent
		if msg.data == "all_off": #TODO: future format ideally would be "if msg.data == command_value"
			self.ser.write(b'0')  #TODO: future format ideally would be "if msg.data == command_value"
			line = self.ser.readline().decode('utf-8').rstrip()
			print(line)  #TODO: "command_name" sent
		if msg.data == "led1_on":
			self.ser.write(b'1') #TODO: future format ideally would be "if msg.data == command_value"
			line = self.ser.readline().decode('utf-8').rstrip()
			print(line)  #TODO: "command_name" sent
		if msg.data == "led2_on":
			self.ser.write(b'2') #TODO: future format ideally would be "if msg.data == command_value"
			line = self.ser.readline().decode('utf-8').rstrip()
			print(line)  #TODO: "command_name" sent
		if msg.data == "led3_on":
			self.ser.write(b'3') #TODO: future format ideally would be "if msg.data == command_value"
			line = self.ser.readline().decode('utf-8').rstrip()
			print(line)  #TODO: "command_name" sent
		if msg.data == "led4_on":
			self.ser.write(b'4') #TODO: future format ideally would be "if msg.data == command_value"
			line = self.ser.readline().decode('utf-8').rstrip()
			print(line)  #TODO: "command_name" sent
		if msg.data == "led1_off":
			self.ser.write(b'5') #TODO: future format ideally would be "if msg.data == command_value"
			line = self.ser.readline().decode('utf-8').rstrip()
			print(line)  #TODO: "command_name" sent
		if msg.data == "led2_off":
			self.ser.write(b'6') #TODO: future format ideally would be "if msg.data == command_value"
			line = self.ser.readline().decode('utf-8').rstrip()
			print(line)  #TODO: "command_name" sent
		if msg.data == "led3_off":
			self.ser.write(b'7') #TODO: future format ideally would be "if msg.data == command_value"
			line = self.ser.readline().decode('utf-8').rstrip()
			print(line)  #TODO: "command_name" sent
		if msg.data == "led4_off":
			self.ser.write(b'8') #TODO: future format ideally would be "if msg.data == command_value"
			line = self.ser.readline().decode('utf-8').rstrip()
			print(line)  #TODO: "command_name" sent


def main(args=None):
	rclpy.init(args=args)
	serial_controller = SerialController()
	rclpy.spin(serial_controller)

if __name__ == '__main__':
	main()
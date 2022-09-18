from time import sleep
import serial

class SerialReader():
	def __init__(self):
		self.transmitting_device = '/dev/ttyS2' #device we are trasmitting messages to
		self.recieving_device = '/dev/ttyS1' #device we are recieving messages from
		self.serial_send = serial.Serial(self.transmitting_device,
            9600, #Note: Baud Rate must be the same in the arduino program, otherwise signal is not recieved!
            timeout=.1)
		self.serial_recieve = serial.Serial(self.recieving_device,
						9600, #Note: Baud Rate must be the same in the arduino program, otherwise signal is not recieved!
						timeout=.1)
	def send_cmd(self, cmd):
		print("Sending: " + cmd)
		self.serial_send.write(bytes(cmd,'utf-8'))
	def recieve_cmd(self):
		try:
			#try normal way of recieving data
			sleep(.01) #sleep to allow time for serial_data to arrive. Otherwise this might return nothing
			self.line = self.serial_recieve.readline().decode('utf-8').rstrip()
		except:
			#if normal way doesn't work, try getting binary representation to see what went wrong
			self.line = str(self.serial_recieve.readline())
		if(self.line == "w"):
			print("recieved the letter w")
			print("sending response...")
			self.send_cmd("I have recieved w")
		elif(self.line == "a"):
			print("recieved the letter a")
			print("sending response...")
			self.send_cmd("I have recieved a")
		elif(self.line == "s"):
			print("recieved the letter s")
			print("sending response...")
			self.send_cmd("I have recieved s")
		elif(self.line == "d"):
			print("recieved the letter d")
			print("sending response...")
			self.send_cmd("I have recieved d")

def main(args=None):
    serial_reader = SerialReader()
    while True:
        serial_reader.recieve_cmd()

if __name__ == '__main__':
	main()
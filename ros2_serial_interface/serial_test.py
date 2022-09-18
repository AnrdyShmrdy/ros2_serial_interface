from serial import Serial
isFinished = False
device_name = '/dev/ttyAMA0' #arduino device name for Linux-based OS
baud_rate = 9600 #Note: this must equal Arduino baud rate, otherwise signal is not recieved!
#maybe make a try-except-finally for different serial connections if one doesn't work, ie try ttyS0 if ttyAMA0 doesn't work
serialConn = Serial(device_name, baud_rate, timeout=.1)
serialConn.reset_input_buffer()
def send_serialMsg(msg):
	global serialConn
	print("Sending: " + msg)
	serialConn.write(bytes(msg,'utf-8'))
def recieve_serialMsg():
	try:
		#try normal way of recieving data
		line = serialConn.readline().decode('utf-8').rstrip()
	except:
		#if normal way doesn't work, try getting binary representation to see what went wrong
		line = str(serialConn.readline())
	print("Recieved: " + line)
#Test:
print("Starting test:")
send_serialMsg('test')
recieve_serialMsg()
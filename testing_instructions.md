# Step-by-step testing instructions

## Testing with predef_timed_pub.py, serial_server.py, netcat, and socat

First open three terminals and run "source install/setup.bash" in each of them

In the first terminal, run:

`nc -l 60001`

This command sets up a netcat server to listen to messages on 127.0.0.1:60001

In the second terminal, run these two commands:

`socat pty,link=/dev/ttyACM0,raw tcp:127.0.0.1:60001&`

`ros2 run ros2_serial_interface serial_server`

The first command uses socat to setup /dev/ttyACM0 to forward data to 127.0.0.1:60001 and runs it in the background

The second command runs the serial_server.py program, which listens to various ROS2 topics. By default it listens to the wheel_instructions_topic topic

In the third terminal, run:

`ros2 run ros2_serial_interface predef_timed_pub`

This runs predef_timed_pub.py, which publishes various Twist messages to the wheel_instructions_topic topic

In the second terminal, you'll see that the serial_server program reads the published messages from the third terminal

In the first terminal, you'll see messages arrive that were sent by the second terminal

Essentially, the serial server (second terminal) recieves the messages from predef_time_pub (third terminal). Based on the messages recieved, the serial_server sends the appropriate response via serial to /dev/ttyAMA0 (aka the serial client). The moment /dev/ttyACM0 recieves it, socat forwards it to 127.0.0.1:60001. Finally the netcat process that is listening for messages on 127.0.0.1:60001 displays these messages in the first terminal

## Testing with virtual_serial_server.py, virtual_serial_client.py, predef_timed_pub.py, and virtual_serial_setup

This test essentially sets up two mock devices:

### virtual_serial_server

- Like serial_server.py, this subscribes to the wheel_instructions_topic topic
- Unlike serial_server.py, the port trasmitted to and the port received from are different
- This transmits data to a serial port called '/dev/ttyS0' 
- The data sent to 'dev/ttyS0' gets forwarded to '/dev/ttyS1' using the socat utility
- This recieves data from a serial port called '/dev/ttyS3'
- The data recieved by '/dev/ttyS3' was forwarded from another serial port called '/dev/ttyS2'
- Essentially, 'dev/ttyS0' sends data to '/dev/ttyS3' and '/dev/ttyS1' recieves data from '/dev/ttyS2'

### virtual_serial_client

- This essentially communicates with the virtual_serial_server
- This transmits data to a serial port called '/dev/ttyS2'
- The data sent to 'dev/ttyS2' gets forwarded to '/dev/ttyS3' using the socat utility
- This recieves data from a serial port called '/dev/ttyS1'
- The data recieved by '/dev/ttyS1' was forwarded from another serial port called '/dev/ttyS0'
- Essentially, 'dev/ttyS2' sends data to '/dev/ttyS1' and '/dev/ttyS3' recieves data from '/dev/ttyS0'

First open three terminals and run "source install/setup.bash" in each of them

In the first terminal, run the following commands:

`ros2 run ros2_serial_interface virtual_serial_setup`

`ros2 run ros2_serial_interface virtual_serial_server`

The first command sets up /dev/ttyS0 to forward data to /dev/ttyS1 and then sets up /dev/ttyS2 to forward data to /dev/ttyS3

The second command runs virtual_serial_server.py

Like serial_server.py, virtual_serial_server.py will send serial data based on what data published to the wheel_instructions_topic topic

Unlike serial_server.py however, virtual_serial_server.py sends serial data to /dev/ttyS0 and recieves serial data from /dev/ttyS3

In the second terminal, run the following command:

`ros2 run ros2_serial_interface virtual_serial_client`

This command runs virtual_serial_client.py, which sets up a mock serial device to be used with virtual_serial_client.py. This mock device will recieve serial data from /dev/ttyS1 and send serial data to /dev/ttyS2

In the third terminal, run the following command:

`ros2 run ros2_serial_interface predef_timed_pub`

This command runs predef_timed_pub.py, which will publishes data to the wheel_instructions_topic topic

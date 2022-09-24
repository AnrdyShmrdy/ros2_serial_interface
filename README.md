# ROS2 Serial Interface

## What this is

This interface is designed to serve as a serial communication bridge between two devices: the serial server and the serial client.

The serial server is the device used to indirectly control the serial client via the use of ROS2 and serial communication

The serial client is the device that listens for serial communication from the serial server. Based on what is communicated to it, the serial client performs a pre-defined action

In theory any device capable of recieving data via serial communication can be the serial client or the serial server. However, the expectation is that the serial server is a device that runs/uses ROS2 (ie, like a Raspberry Pi), while the serial client is a device that doesn't run/use ROS2 (ie, like a microcontroller)

Note that the serial client must be programmed with the intent of doing a particular action upon recieving a specific input from the serial server. For example, if the serial server sends the character 'w' to the serial client, the serial client must be programmed to listen for the character 'w'. Additionally, the serial server must be programmed knowing what the serial client will do once it recieves the character 'w'.

The main intention of this project is to provide a basic framework/idea that anyone can use and modify to suit their particular project. The programs in this repository are designed to demonstrate what one CAN do with their project, not what one SHOULD do with their project. It is expected that those who wish to use these files will modify them heavily to suit their own individual needs

## Description of what each file does (in progress)

predef_timed_pub.py:

pynput_key_pub.py:

serial_server.py:

serial_server_launch.py:

terminal_key_pub.py:

virtual_serial_client.py:

virtual_serial_server.py:

virtual_serial_setup.py:

## Running these files

To run predef_timed_pub.py:

`ros2 run ros2_serial_interface predef_timed_pub`

To run pynput_key_pub.py:

`ros2 run ros2_serial_interface pynput_key_pub`

To run serial_server.py:

`ros2 run ros2_serial_interface serial_server`

To run serial_server_launch.py:

`ros2 launch ros2_serial_interface serial_server_launch.py`

To run terminal_key_pub.py:

`ros2 run ros2_serial_interface terminal_key_pub`

To run virtual_serial_client.py:

`ros2 run ros2_serial_interface virtual_serial_client`

To run virtual_serial_server.py:

`ros2 run ros2_serial_interface virtual_serial_server`

To run virtual_serial_setup.py:

`ros2 run ros2_serial_interface virtual_serial_setup`

## Testing these files

For instructions on testing these files, see testing_instructions.md

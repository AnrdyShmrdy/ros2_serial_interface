# ROS2 Serial Interface:
This interface will ideally serve as the communication bridge between a device running ROS2 and another device capable of serial communication

The main purpose behind this project is to negate the need to run ROS2 subscribers directly on microcontrollers. 

For Arduino microcontrollers this would allow them to tie messages published to ROS2 topics to specific actions (ie, turning on an led, running a motor, etc) without needing to rely on libraries such as Ros2Arduino, Rosserial, or Micro-Ros. This is great for the ATMega2560 (which is the device being used for testing) as many ROS2 Arduino libraries do not support it

Currently this is being tested in ROS2-Foxy, but the interface should be simple enough to be easily converted to other versions and distributions of ROS if it ever should need to be

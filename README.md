# ROS2 Serial Interface

## What this is

This interface is designed to serve as a serial communication bridge between two devices: the serial server and the serial client.

The serial server is the device used to indirectly control the serial client via the use of ROS2 and serial communication with the serial client

The serial client is the device that listens for serial communication from the serial server. Based on what is communicated to it, the serial client will perform a pre-programmed action

In theory any device capable of recieving data via serial communication can be the serial client or the serial server. However, the expection is that the serial server is a device that will run/use ROS2 (ie, like a Raspberry Pi), while the serial client is a device that won't run/use ROS2 (ie, like a microcontroller)

Note that the idea here is that the serial client is pre-programmed to respond in a specific way to input that is sent to it via serial communication. In other words, the serial client must be programmed with the intent of doing a particular action upon recieving a specific input from the serial server. For example, if the serial server sends the character 'w' to the serial client, the serial client must be programmed to listen for the character 'w'. Additionally, the serial server must be programmed knowing what the serial client will do once it recieved the character 'w'.

## Running these files


**WIP**

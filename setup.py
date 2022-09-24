from setuptools import setup
import os
from glob import glob

package_name = 'ros2_serial_interface'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*_launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='andyp',
    maintainer_email='andy.ponce@outlook.com',
    description='Ros2 Serial Interface',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'predef_timed_pub = ros2_serial_interface.predef_timed_pub:main',
        	'pynput_key_pub = ros2_serial_interface.pynput_key_pub:main',
            'serial_server = ros2_serial_interface.serial_server:main',
            'terminal_key_pub = ros2_serial_interface.terminal_key_pub:main',
        	'virtual_serial_client = ros2_serial_interface.virtual_serial_client:main',
            'virtual_serial_setup = ros2_serial_interface.virtual_serial_setup:main',
            'virtual_serial_server = ros2_serial_interface.virtual_serial_server:main'
        ],
    },
)

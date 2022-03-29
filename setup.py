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
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'serial_controller = ros2_serial_interface.serial_controller:main',
        	'timer_publisher = ros2_serial_interface.timer_publisher:main',
        	'keyboard_publisher = ros2_serial_interface.keyboard_publisher:main'
        	
        ],
    },
)

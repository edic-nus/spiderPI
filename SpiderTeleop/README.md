This is a ROS2 package that contains the Rteleop package for the HiWonder SpiderPi hexapod robot.

How to use rteleop:
1) Navigate to the root directory of "SpiderTeleop"
2) Source the rteleop package "source /install/local_setup.bash"
3) Type "echo $AMENT_PREFIX_PATH" to verify that the "rpc_commands" package and ROS2 humble is correctly sourced
4) Use the ROS2 command to run Rteleop.py "ros2 run rpc_commands rteleop"
5) Press ctrl+c to exit the rteleop


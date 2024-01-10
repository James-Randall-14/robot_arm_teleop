rm -rf /home/jhsrobo/armws/robot_arm_teleop/urdf/robot_arm.urdf.xml
xacro /home/jhsrobo/armws/robot_arm_teleop/urdf/robot_arm.xacro >> /home/jhsrobo/armws/robot_arm_teleop/urdf/robot_arm.urdf.xml
cd /home/jhsrobo/armws
colcon build
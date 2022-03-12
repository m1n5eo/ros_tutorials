cmake_minimum_required(VERSION 3.0.2)
project(rospy_tutorials)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_install_python(PROGRAMS
  publisher_and_subscriber/publisher_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/publisher_and_subscriber
)
catkin_install_python(PROGRAMS
  publisher_and_subscriber/subscriber_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/publisher_and_subscriber
)
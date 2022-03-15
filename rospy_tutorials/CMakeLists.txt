cmake_minimum_required(VERSION 3.0.2)
project(rospy_tutorials)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)


add_message_files(
  FILES
  Position.msg
)

add_service_files(
  FILES
  multiplier.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)


# publisher_and_subscriber
catkin_install_python(PROGRAMS publisher_and_subscriber/publisher_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/publisher_and_subscriber
)
catkin_install_python(PROGRAMS publisher_and_subscriber/subscriber_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/publisher_and_subscriber
)

# custom_message
catkin_install_python(PROGRAMS custom_message/publisher_node2.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/custom_message
)
catkin_install_python(PROGRAMS custom_message/subscriber_node2.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/custom_message
)

# service
catkin_install_python(PROGRAMS service/server_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/service
)
catkin_install_python(PROGRAMS service/client_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/service
)
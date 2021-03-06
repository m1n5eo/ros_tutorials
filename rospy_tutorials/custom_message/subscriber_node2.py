#!/usr/bin/env python3.8

import rospy
from std_msgs.msg import String
from rospy_tutorials.msg import Position

def callback(data):
    rospy.loginfo("%s x: %f y: %f", data.message, data.x, data.y)

def listener():
    rospy.init_node("Subscriber_node", anonymous=True)
    rospy.Subscriber('talking_topic', Position, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
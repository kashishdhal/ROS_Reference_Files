#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    print msg                                   # Print the value 'data' inside the 'msg' parameter

rospy.init_node('odom_sub_node')                   # Initiate a Node called 'topic_subscriber'

sub = rospy.Subscriber('/odom', Odometry, callback)  # Create a Subscriber object that will listen to the /counter

rospy.spin()

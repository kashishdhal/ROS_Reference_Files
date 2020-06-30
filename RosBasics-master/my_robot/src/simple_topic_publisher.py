#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('move_robot_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
vel = Twist()
vel.linear.x = 0.5
vel.angular.z = 0.5

while not rospy.is_shutdown():
  pub.publish(vel)
  rate.sleep()
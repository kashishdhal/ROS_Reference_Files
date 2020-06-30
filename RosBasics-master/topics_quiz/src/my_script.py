#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(data):
    sum_left=0.0
    sum_front = 0.0
    sum_right = 0.0
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(0,240):
        if data.ranges[i] <30.0:
            sum_left += data.ranges[i]
            count1 += 1
    for i in range(240,480):
        if data.ranges[i] <30.0:
            count2 += 1
            sum_front += data.ranges[i]
    for i in range(480,720):
        if data.ranges[i] <30.0:
            count3 += 1
            sum_right += data.ranges[i]

    #print sum_left
    #print sum_front
    #print sum_right

    left_distance = 0.0
    front_distance = 0.0
    right_distance = 0.0

    if count1!=0:
        left_distance = sum_left/count1
    if count2!=0:
        front_distance = sum_front/count2
    if count3!=0:
        right_distance = sum_right/count3

    #print count1

    #print "left distance:", left_distance
    #print "front distance:", front_distance
    #print "right distance:", right_distance

    pub = rospy.Publisher('/cmd_vel', Twist,queue_size=1)
    rate = rospy.Rate(2)
    vel = Twist()

    if (left_distance>1 and right_distance>1 and front_distance>1) or (left_distance==0 and front_distance==0 and right_distance==0):
        vel.linear.x = 0.1
    elif left_distance<1 and (left_distance<right_distance or left_distance<front_distance):
        print "steering left"
        vel.linear.x = -0.1
        vel.angular.z = -0.5
    else:
        print "steering right"
        vel.linear.x = -0.1
        vel.angular.z = 0.5

   # while not rospy.is_shutdown():
    pub.publish(vel)
      #  rate.sleep()

def dxl_control():
    rospy.init_node('topics_quiz_node')
    sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        dxl_control()
    except rospy.ROSInterruptException:
        pass
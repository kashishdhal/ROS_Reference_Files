#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle has been called")
    move_circle.linear.x = 0.2
    move_circle.angular.z = 0.2
    my_pub.publish(move_circle)
    rospy.loginfo("Finished service move_bb8_in_circle")
    # the service Response class, in this case EmptyResponse
    return EmptyResponse() 

rospy.init_node('service_move_bb8_in_circle_server')
# create the Service called move_bb8_in_circle with the defined callback
my_service = rospy.Service('/move_bb8_in_circle', Empty , my_callback) 
# Create the publisher to publish to /cmd_vel of type Twist
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
# Create an object of the type Twist
move_circle = Twist()
# display that the service is ready and waiting for client
rospy.loginfo("Service /move_bb8_in_circle Ready")
# mantain the service open.
rospy.spin() 
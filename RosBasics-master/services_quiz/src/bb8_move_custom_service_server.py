#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle_custom has been called")
    
    while(request.repetitions>0):

        j=0 
        while(j<4):

            # Moving the robot
            print('Moving the robot for ' + str(request.side) + 'mtr')
            i = 0
            move_circle.linear.x = 0.2
            move_circle.angular.z = 0.0
            while i <= request.side:
                my_pub.publish(move_circle)
                print('Length Travelled =' +  str(i))
                rate.sleep()
                i=i+1

            # Linear speed in x is zero
            move_circle.linear.x = 0.0
            my_pub.publish(move_circle)

            # Rotating the robot
            i = 0
            move_circle.angular.z = 0.2
            move_circle.linear.x = 0.0
            while i <= 3:
                my_pub.publish(move_circle)
                print('Length Travelled =' +  str(i))
                rate.sleep()
                i=i+1   

            # Angular speed in z is zero
            move_circle.angular.z = 0.0
            my_pub.publish(move_circle)

            # Increment the counter
            j = j+1
    
        request.repetitions = request.repetitions - 1


    move_circle.linear.x = 0
    move_circle.angular.z = 0.0    
    my_pub.publish(move_circle)
    
    rospy.loginfo("Finished service move_bb8_in_circle_custom")

    response = BB8CustomServiceMessageResponse()
    response.success = True
    return response # the service Response class, in this case EmptyResponse

rospy.init_node('service_move_bb8_in_square_custom_server')
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback) # create the Service called move_bb8_in_circle with the defined callback
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_circle = Twist()
rate = rospy.Rate(1)
rospy.loginfo("Service /move_bb8_in_circle_custom Ready")
rospy.spin() # mantain the service open.
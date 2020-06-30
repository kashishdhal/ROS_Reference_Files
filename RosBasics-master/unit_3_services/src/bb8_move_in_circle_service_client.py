#! /usr/bin/env python
import rospkg
import rospy
from std_srvs.srv import Empty, EmptyRequest # you import the service message python classes generated from Empty.srv.

# Initialise a ROS node with the name service_move_bb8_in_circle_client
rospy.init_node('service_move_bb8_in_circle_client') 
# Wait for the service client /move_bb8_in_circle to be running
rospy.wait_for_service('/move_bb8_in_circle') 
# Create the connection to the service
move_bb8_in_circle_service_client = rospy.ServiceProxy('/move_bb8_in_circle', Empty) 
# Create an object of type EmptyRequest
move_bb8_in_circle_request_object = EmptyRequest() 
# Call the service by sending the request object to the server
result = move_bb8_in_circle_service_client(move_bb8_in_circle_request_object) 
# Print the result given by the service called
print result 
#! /usr/bin/env python
import rospkg
import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest

# Initialise a ROS node with the name service_move_bb8_in_circle_client
rospy.init_node('service_move_bb8_in_circle_custom_client') 
# Wait for the service client /move_bb8_in_circle to be running
rospy.wait_for_service('/move_bb8_in_circle_custom') 
# Create the connection to the service
move_bb8_in_circle_service_client = rospy.ServiceProxy('/move_bb8_in_circle_custom', MyCustomServiceMessage) 
# Create an object of type EmptyRequest
move_bb8_in_circle_request_object = MyCustomServiceMessageRequest()
#Duration for which you would like to execute the service
move_bb8_in_circle_request_object.duration = 10
# Call the service by sending the request object to the server
result = move_bb8_in_circle_service_client(move_bb8_in_circle_request_object) 
# Print the result given by the service called
print result 
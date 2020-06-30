#! /usr/bin/env python
import rospkg
import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

# Initialise a ROS node with the name service_move_bb8_in_circle_client
rospy.init_node('service_move_bb8_in_square_custom_client') 
# Wait for the service client /move_bb8_in_circle to be running
rospy.wait_for_service('/move_bb8_in_square_custom') 
# Create the connection to the service
move_bb8_in_square_service_client = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage) 
# Create an object of type EmptyRequest
move_bb8_in_square_request_object = BB8CustomServiceMessageRequest()
#Duration for which you would like to execute the service
move_bb8_in_square_request_object.side = 5
move_bb8_in_square_request_object.repetitions = 2
# Call the service by sending the request object to the server
result = move_bb8_in_square_service_client(move_bb8_in_square_request_object) 
# Print the result given by the service called
print result 

#Duration for which you would like to execute the service
move_bb8_in_square_request_object.side = 10
move_bb8_in_square_request_object.repetitions = 1
# Call the service by sending the request object to the server
result = move_bb8_in_square_service_client(move_bb8_in_square_request_object) 
# Print the result given by the service called
print result 
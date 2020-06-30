#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse # you import the service message python classes
                                                                                         # generated from MyCustomServiceMessage.srv.


def my_callback(request):

    print "Request Data==> duration="+str(request.duration)
    my_response = MyCustomServiceMessageResponse()
    
    if request.duration > 5.0:
        my_response.success = True
    else:
        my_response.success = False
    
    # the service Response class, in this case MyCustomServiceMessageResponse
    return  my_response 

# Create a service node named service_client
rospy.init_node('service_client')
 # create the Service called my_service with the defined callback
my_service = rospy.Service('/my_service', MyCustomServiceMessage , my_callback)
# maintain the service open.
rospy.spin() 
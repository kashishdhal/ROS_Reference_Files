#! /usr/bin/env python
import rospy
import time
import actionlib
import actions_quiz

from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from actions_quiz.msg import CustomActionMsgAction, CustomActionMsgFeedback, CustomActionMsgResult

class MoveSquareClass(object):
    
  # create messages that are used to publish feedback/result
  _feedback = CustomActionMsgFeedback()
  _result   = CustomActionMsgResult()

  def __init__(self):
    # creates the action server
    self._as = actionlib.SimpleActionServer("action_custom_msg_as", CustomActionMsgAction, self.goal_callback, False)
    self._as.start()
    self.ctrl_c = False
    self.rate = rospy.Rate(10)
    
  
  def publish_once_in_cmd_vel(self, cmd):
    """
    This is because publishing in topics sometimes fails teh first time you publish.
    In continuos publishing systems there is no big deal but in systems that publish only
    once it IS very important.
    """
    while not self.ctrl_c:
        connections = self._pub_cmd_vel.get_num_connections()
        if connections > 0:
            self._pub_cmd_vel.publish(cmd)
            rospy.loginfo("Publish in cmd_vel...")
            break
        else:
            self.rate.sleep()
            
  def take_off(self):
    # make the drone takeoff
    i=0
    while not i == 5:
        self._pub_takeoff.publish(self._takeoff_msg)
        rospy.loginfo('Taking off...')
        time.sleep(1)
        i += 1
    rospy.loginfo('Finished Takeoff' )
    self._as.set_succeeded(self._result)          

  def land(self):
          # make the drone takeoff
    i=0
    while not i == 5:
        self._pub_land.publish(self._land_msg)
        rospy.loginfo('Landing...')
        time.sleep(1)
        i += 1
    rospy.loginfo('Finished Landing' )
    self._as.set_succeeded(self._result)    


  def goal_callback(self, goal):
    # this callback is called when the action server is called.
    # this is the function that computes the Fibonacci sequence
    # and returns the sequence to the node that called the action server
    
    # helper variables
    r = rospy.Rate(1)
    success = True
    
    # define the different publishers and messages that will be used
    self._pub_cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    self._move_msg = Twist()
    self._pub_takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
    self._takeoff_msg = Empty()
    self._pub_land = rospy.Publisher('/drone/land', Empty, queue_size=1)
    self._land_msg = Empty()
    
   
    # get the command from goal object
    command = goal.goal    
    
    # check that preempt (cancelation) has not been requested by the action client
    if self._as.is_preempt_requested():
        rospy.loginfo('The goal has been cancelled/preempted')
        # the following line, sets the client in preempted state (goal cancelled)
        self._as.set_preempted()
        success = False
    elif command == "TAKEOFF":
        self.take_off()
        self._feedback.feedback = "TAKEOFF"
    elif command == "LAND":
        self.land()    
        self._feedback.feedback = "LAND"

    # build and publish the feedback message
    self._as.publish_feedback(self._feedback)
    # the sequence is computed at 1 Hz frequency
    r.sleep()
    
    # at this point, either the goal has been achieved (success==true)
    # or the client preempted the goal (success==false)
    # If success, then we publish the final result
    # If not success, we do not publish anything in the result
    if success:
      rospy.loginfo('Finished the mission, you may type another command' )

        

      
if __name__ == '__main__':
  rospy.init_node('move_square')
  rospy.loginfo('Server is up and running')
  MoveSquareClass()
  rospy.spin()
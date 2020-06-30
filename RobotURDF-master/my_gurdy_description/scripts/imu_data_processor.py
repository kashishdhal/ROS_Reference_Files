#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion



class GurdyImuDataProcessor(object):

    def __init__(self):

        self.movement = "basic_stance"
        self.imu_topic_name = '/gurdy/imu/data'
        self._check_imu_data_ready()


    def _check_imu_data_ready(self):
        self.imu_data = None
        while self.imu_data is None and not rospy.is_shutdown():
            try:
                self.imu_data = rospy.wait_for_message(self.imu_topic_name, Imu, timeout=1.0)
                rospy.logdebug("Current "+str(self.imu_topic_name)+" READY")

            except:
                rospy.logerr("Current "+str(self.imu_topic_name)+" not ready yet, retrying")

        self.process_imu_data(self.imu_data)

        self.sub = rospy.Subscriber (self.imu_topic_name, Imu, self.get_imu_data)


    def extract_rpy_imu_data (self, imu_msg):

        orientation_quaternion = imu_msg.orientation
        orientation_list = [orientation_quaternion.x,
                            orientation_quaternion.y,
                            orientation_quaternion.z,
                            orientation_quaternion.w]
        roll, pitch, yaw = euler_from_quaternion (orientation_list)
        return roll, pitch, yaw


    def detect_upsidedown(self, roll, pitch, yaw):

        detected_upsidedown = False

        #rospy.loginfo("[roll, pitch, yaw]=["+str(roll)+","+str(pitch)+","+str(yaw)+"]")

        # UpRight: 0.011138009176,0.467822324143,2.45108157992
        # NEW UpRight: [roll, pitch, yaw]=[0.0122901501501,-0.00605881110832,-0.362102155385]

        # UpSideDown: [-3.1415891735,-2.12226602154e-05,2.38423951221]
        # UpSideDown: [3.14141489641,-0.000114323270767,2.38379058991]
        # NEW UpsideDown: [roll, pitch, yaw]=[2.70987958046,0.32139792461,1.32555268987]

        roll_trigger = 1.25

        if abs(roll) > roll_trigger:
            rospy.logwarn("UPASIDEDOWN-ROLL!")
            detected_upsidedown = True

        return detected_upsidedown


    def process_imu_data(self, msg):
        roll, pitch, yaw = self.extract_rpy_imu_data(msg)
        self.detected_upsidedown = self.detect_upsidedown(roll, pitch, yaw)

    def get_imu_data(self, msg):
        self.process_imu_data(msg)

    def is_upasidedown(self):
        return self.detected_upsidedown


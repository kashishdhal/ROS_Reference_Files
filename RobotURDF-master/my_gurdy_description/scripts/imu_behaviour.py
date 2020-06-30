#!/usr/bin/env python

import rospy
from gurdy_behaviour import GurdyBehaviour


def start_imu_behaviour_behaviour():
    # We Start Here
    rospy.init_node('imu_behaviour_node')
    gurdy_bhv = GurdyBehaviour()
    gurdy_bhv.start_behaviour(behaviour="init_stance")


if __name__ == "__main__":
    start_imu_behaviour_behaviour()
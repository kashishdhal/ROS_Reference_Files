#!/usr/bin/env python

import rospy
from gurdy_behaviour import GurdyBehaviour


def start_jump_behaviour_behaviour():
    # We Start Here
    rospy.init_node('jump_behaviour_node')
    gurdy_bhv = GurdyBehaviour()
    gurdy_bhv.start_behaviour(behaviour="jump")


if __name__ == "__main__":
    start_jump_behaviour_behaviour()
from cmath import sqrt
from re import X
from turtle import distance
import rospy
#from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal #
from geometry_msgs.msg import PoseStamped, Twist, Pose2D
from std_msgs.msg import Int16
from time import sleep
from struct import *
import math
import tf
import actionlib
import roslib
import smach_ros

import sys
sys.path.append('~/home/catkin_ws/src/kheperas_description/python')

from position import *
from scipy import special
import matplotlib.pyplot as plt
import numpy as np
from kheperas_description.msg import SignalQuality


def publisher():
    pub = rospy.Publisher('/robot1/position',Pose2D,queue_size=10)
    rospy.init_node('robot1_signal_publisher',anonymous=True)
    r = rospy.Rate(20) #1Hz
    msg = Pose2D()

    while not rospy.is_shutdown():
        [msg.x, msg.y, msg.theta]=position3('robot1')

        #rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    
    try:
        publisher()
    except rospy.ROSInterruptException: pass
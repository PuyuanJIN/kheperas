
import rospy
#from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal #
from geometry_msgs.msg import PoseStamped, Twist
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

def FSPL():


    signal_wavelength = 3*10**8/700/10**9
    (x1, y1, yaw1) = position_mrobot()
    (x2, y2, yaw2) = position_reference()

    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    return (10*math.log10(4*math.pi*dist/signal_wavelength)**2)


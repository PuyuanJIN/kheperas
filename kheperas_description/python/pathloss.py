
from python.position import position
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


def FSPL(signal_wavelength):

    (x_cur, y_cur, yaw_cur) = position()
    dist = math.sqrt(x_cur*x_cur + y_cur*y_cur)

    return (4*math.pi*dist/signal_wavelength)^2


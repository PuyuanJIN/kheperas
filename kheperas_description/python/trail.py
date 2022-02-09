from numpy import disp
import rospy
import actionlib
from smach import State, StateMachine
import roslaunch
from time import sleep
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped, Twist
from std_msgs.msg import Int16
from struct import *
import math
import tf
from tf.transformations import quaternion_from_euler, euler_from_quaternion
import roslib
import smach_ros

import sys
sys.path.append('~/home/catkin_ws/src/kheperas_description/python')

from position import *
from move import *
from rotation import *


if __name__ == '__main__':
    rospy.init_node('trail')
    position2()




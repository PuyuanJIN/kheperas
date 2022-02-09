
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



class Move(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
    
    def execute(self, userdata):

        move(1,2.0)
        display_position()
        return 'success'


class Rotate(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
    
    def execute(self, userdata):

        rotate(90)
        display_position()
        return 'success'


class Wait(State):
    def __init__(self):
        State.__init__(self, outcomes=['move','rotate'])
    
    def execute(self, userdata):
        print('''
        #####################
        # m     -move
        # r     -rotate
        #####################
        ''')
        command = input('user input>')
        if command == 'm':
            return 'move'
        elif command == 'r':
            return 'rotate'
        else:
            exit()


if __name__ == '__main__':
    rospy.init_node('patrol')
    display_position()
    patrol = StateMachine('WAIT')

    with patrol:
        StateMachine.add('WAIT', Wait(), transitions={'move':'Move','rotate':'Rotate'})
        StateMachine.add('Move',Move(),transitions={'success':'WAIT'})
        StateMachine.add('Rotate', Rotate(),transitions={'success':'WAIT'})

    
    patrol.execute()

from email.errors import MissingHeaderBodySeparatorDefect
from pdb import post_mortem
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
from pathloss import *




class Move(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
    
    def execute(self, userdata):

        move()
        print('success')
        return 'success'


class Rotate(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
    
    def execute(self, userdata):

        rotate()
        sleep(1)
        print('success')
        return 'success'


class Wait(State):
    def __init__(self):
        State.__init__(self, outcomes=['move','rotate','signal check','odom'])
    
    def execute(self, userdata):
        print('''
        #####################
        Welcome to the robot simulator control pannel!
        Available command are following:
        ---------------------
        # odom  -print out robot position
        # m     -move
        # r     -rotate
        # s     -signal check
        #####################
        ''')
        command = input('~')
        if command == 'm':
            return 'move'
        elif command == 'r':
            return 'rotate'
        elif command == 's':
            return('signal check')
        elif command =='odom':
            return 'odom'
        else:
            exit()

class Signal(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
    
    def execute(self, userdata):

        DeliveryFailure()
        print('success')
        return 'success'

#this is the class that give robot position 
class Odom(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
    
    def execute(self, userdata):
        position2()
        return 'success'



if __name__ == '__main__':
    rospy.init_node('patrol')
    patrol = StateMachine('WAIT')

    with patrol:
        StateMachine.add('WAIT', Wait(), transitions={'move':'Move','rotate':'Rotate','signal check':'Signal','odom':'Odom'})
        StateMachine.add('Move',Move(),transitions={'success':'WAIT'})
        StateMachine.add('Rotate', Rotate(),transitions={'success':'WAIT'})
        StateMachine.add('Signal', Signal(),transitions={'success':'WAIT'})
        StateMachine.add('Odom', Odom(),transitions={'success':'WAIT'})
    
    patrol.execute()
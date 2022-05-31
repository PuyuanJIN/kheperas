

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

def planner(goal):

    # read robot current position and the goal position #
    (x_cur, y_cur, yaw_cur) = position_mrobot()
    x_goal = float(goal[0])
    y_goal = float(goal[1])

    #calculate the distance from cureent postion to goal position #
    a = y_goal - y_cur
    b = x_goal - x_cur
    dist = math.sqrt(a*a+b*b)

    #yaw_diff calculation
    if b != 0:
        th = math.atan(a/b)
    if a == 0.0 and b > 0.0:
        th = 0.0
    if a == 0.0 and b < 0.0:
        th = math.pi
    if b == 0.0 and a > 0.0:
        th = math.pi / 2.0
    if b ==0.0 and a < 0.0:
        th = math.pi / 2.0 * -1
    if a > 0.0 and b < 0.0:
        th = th + math.pi
    if a < 0.0 and b < 0.0:
        th = th - math.pi
    

    yaw_goal = math.degrees(th)
    yaw_diff = (yaw_goal - yaw_cur)

    return yaw_diff, dist
    sleep(1)


def rotate():

    #request the robot name that the user want to use
    print('''
        =====================
        input the robot you want to control, options below 
        # 1     -robot 1
        # 2     -robot 2
        # 3     -robot 3
        # 4     -robot 4
        =====================
        ''')
    robot_index = input('~')

    #convert into a valid rostopic name/path
    topic_name = '/robot' + str(robot_index) + '/cmd_vel'
    print('publisher direct to the following path:{}'.format(topic_name))

    #ros velocity publisher initialised
    vel_pub = rospy.Publisher(topic_name,Twist, queue_size=1)

    #command initialized
    move_cmd = Twist()
    move_cmd.linear.x = 0.0
    move_cmd.linear.y = 0.0
    move_cmd.linear.z = 0.0
    move_cmd.angular.x = 0.0
    move_cmd.angular.y = 0.0
    move_cmd.angular.z = 0.0

    #set default angular speed to 0.3 rad/s
    angular_speed = 0.4
    #set default command signal rate to 5Hz
    Hz = 20

    print('''
        =====================
        input rotate command, format direction,angle
        for example:
        1,90        rotate 90 degrees anti-clockwise
        -1,180      rotate 180 degrees clockwise
        =====================
        ''')
    
    command = input('~')
    direction = int(command.split(',')[0])
    degrees = float(command.split(',')[1])

    goal = math.radians(degrees)
    t = goal/angular_speed*Hz
    t_total = goal / angular_speed * Hz + Hz

    #rate index
    i = 0
    rate = rospy.Rate(Hz)
    while i <= t_total:
        if i < t:
            move_cmd.angular.z = angular_speed * direction
        else:
            move_cmd.angular.z = 0.0
        
        vel_pub.publish(move_cmd)
        i = i+1
        rate.sleep()






























from dis import dis
import rospy
import actionlib
import roslaunch
from time import sleep
from geometry_msgs.msg import PoseStamped, Twist
from std_msgs.msg import Int16
from struct import *
import math
import roslib


def move():

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
    vel_pub = rospy.Publisher(topic_name, Twist, queue_size=1)

    #move cmd initialized
    move_cmd = Twist()
    move_cmd.linear.x = 0.0
    move_cmd.linear.y = 0.0
    move_cmd.linear.z = 0.0
    move_cmd.angular.x = 0.0
    move_cmd.angular.y = 0.0
    move_cmd.angular.z = 0.0

    #set default speed 
    linear_speed = 0.20
    #set default command signal rate
    Hz = 5

    print('''
        =====================
        input move command, format direction,distance
        for example:
        1,0.5       move 0.5m forward
        -1,1        move 1.0m backward
        =====================
        ''')
    
    command = input('~')
    direction = int(command.split(',')[0])
    distance = int(command.split(',')[1])

    t = distance / linear_speed * Hz
    t_total = t + Hz

    #rate index
    i = 0

    rate = rospy.Rate(Hz)
    while i <= t_total:
        if i < t:
            move_cmd.linear.x = direction * linear_speed
            
        else:
            move_cmd.linear.x = 0.0
        
        vel_pub.publish(move_cmd)
        i = i+1
        rate.sleep()




























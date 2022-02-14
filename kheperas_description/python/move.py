

import rospy
import actionlib
import roslaunch
from time import sleep
from geometry_msgs.msg import PoseStamped, Twist
from std_msgs.msg import Int16
from struct import *
import math
import roslib


def move(direction,distance):

    #ros velocity publisher initialised
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

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




























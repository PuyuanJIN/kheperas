

import rospy
import roslaunch
from struct import *
import math
import tf
from tf.transformations import quaternion_from_euler, euler_from_quaternion
import roslib
from gazebo_msgs.srv import *


# this function calculate the robot's current position relavtive to the map's origional #
def position1():

    #subsrible to the tf topic #
    listener = tf.TransformListener()
    listener.waitForTransform('/world','/base_footprint',rospy.Time(),rospy.Duration(4))
    (trans,rot)=listener.lookupTransform('/map','/base_link',rospy.Time(0))

    # math operator #
    euler = euler_from_quaternion(rot)
    x_cur = round(trans[0],4)
    y_cur = round(trans[1],4)
    yaw_cur = math.degrees(euler[2])
    return x_cur, y_cur, yaw_cur


def position2():
    get_state_service = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    model = GetModelStateRequest()
    model.model_name='mrobot'
    obj = get_state_service(model)
    state=(obj.pose.position.x,obj.pose.position.y)
    print(state[0],state[1])
    rot = obj.pose.orientation
    euler = euler_from_quaternion(rot)
    yaw_cur = math.degrees(euler[2])
    
    return state[0], state[1], yaw_cur


# display the current robot position to the terminal #
def display_position():
    (x_cur, y_cur, yaw_cur) = position2()
    print('Robot current position is: [{}, {}, {}]'.format(x_cur,y_cur,yaw_cur))





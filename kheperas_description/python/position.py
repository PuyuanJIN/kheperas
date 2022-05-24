

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
    model_name=input('input model name>')
    model.model_name=str(model_name)
    obj = get_state_service(model)
    state=(obj.pose.position.x,obj.pose.position.y)
    #print(state[0],state[1])
    rot = (obj.pose.orientation.x,obj.pose.orientation.y,obj.pose.orientation.z,obj.pose.orientation.w)
    euler = euler_from_quaternion(rot)
    yaw_cur = math.degrees(euler[2])
    print('{} position:[{}, {}, {}]'.format(model_name,round(state[0],4), round(state[1],4), round(yaw_cur,4)))
    return round(state[0],4), round(state[1],4), round(yaw_cur,4)

def position_mrobot():
    get_state_service = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    model = GetModelStateRequest()
    model.model_name='mrobot'
    obj = get_state_service(model)
    state=(obj.pose.position.x,obj.pose.position.y)
    #print(state[0],state[1])
    rot = (obj.pose.orientation.x,obj.pose.orientation.y,obj.pose.orientation.z,obj.pose.orientation.w)
    euler = euler_from_quaternion(rot)
    yaw_cur = math.degrees(euler[2])
    print('mrobot current position is: [{}, {}, {}]'.format(round(state[0],4), round(state[1],4), round(yaw_cur,4)))
    return round(state[0],4), round(state[1],4), round(yaw_cur,4)

def position_reference():
    get_state_service = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    model = GetModelStateRequest()
    model.model_name='referenceRobot'
    obj = get_state_service(model)
    state=(obj.pose.position.x,obj.pose.position.y)
    #print(state[0],state[1])
    rot = (obj.pose.orientation.x,obj.pose.orientation.y,obj.pose.orientation.z,obj.pose.orientation.w)
    euler = euler_from_quaternion(rot)
    yaw_cur = math.degrees(euler[2])
    print('reference robot current position is: [{}, {}, {}]'.format(round(state[0],4), round(state[1],4), round(yaw_cur,4)))
    return round(state[0],4), round(state[1],4), round(yaw_cur,4)



# display the current robot position to the terminal #
def display_position():
    (x_cur, y_cur, yaw_cur) = position2()
    print('Robot current position is: [{}, {}, {}]'.format(x_cur,y_cur,yaw_cur))





#! /user/bin/env python

import rospy
from sensor_msgs.msg import Imu
import math


def imu_callback(imu_data):

    #read the IMU quaternion data
    x = imu_data.orientation.x
    y = imu_data.orientation.y
    z = imu_data.orientation.y
    w = imu_data.orientation.w

    #read the IMU angular velocity 
    omega_x = imu_data.angular_velocity.x
    omega_y = imu_data.angular_velocity.y
    omega_z = imu_data.angular_velocity.z

    #read the IMU linear acceleration
    a_x = imu_data.linear_acceleration.x
    a_y = imu_data.linear_acceleration.y
    a_z = imu_data.linear_acceleration.z

    #conver quaternions to Eular_Anglers
    rpy_angle = [0, 0, 0]
    rpy_angle[0] = math.atan2(2 * (w * x + y * z), 1 - 2 * (x**2 + y**2))
    rpy_angle[1] = math.asin(2 * (w * y - z * x))
    rpy_angle[2] = math.atan2(2 * (w * z + x * y), 1 - 2 * (y**2 + z**2))
    return

if __name__ == '__main__':
    rospy.init_node('imu_node', anonymous=True)
    rospy.Subscriber("/mrobot/imu", Imu, imu_callback)
    rospy.spin()

from cmath import sqrt
from re import X
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
from scipy import special
import matplotlib.pyplot as plt
import numpy as np



def eta_calculator():

    x = np.linspace(0.01,100)

    #compute the receving power, transmitter is working at 8W, 2.4GHz
    fspl = [8/((4*math.pi*i*2.4*(10**9)/(3*(10**8)))**2) for i in x]

    N_0 = -174+11+10*math.log(2.4*10**9,10)     #compute the noise spectral power density with respect of 2.4GHz bandwidth, unit dBm
    pN_0 = 10**(N_0/10)     #convert dBm to mW

    energy_ratio = [math.sqrt(i/pN_0) for i in fspl]

    qpsk = special.erfc(energy_ratio)

    log = [math.log(1-i,10) for i in qpsk]
    deliveryfailure = [1 - math.e**(4*100*i) for i in log]
    
    plt.plot(x,deliveryfailure)
    plt.title('probaility versus energy ratro')
    plt.xlabel('sqrt of $Eb/N0$')
    plt.ylabel('probability of delivery failure')
    plt.show()

def FSPL():


    signal_wavelength = 3*10**8/2.4/10**9 #wavelength of a frequency of 2.4GHz

    #distance readings from gazebo
    (x1, y1, yaw1) = position_mrobot()
    (x2, y2, yaw2) = position_reference()
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    print('the distance between the two robots is {}m'.format(dist,3))

    
    eta=1
    #the power of a standard router is 100mW at 2.4GHz 
    print('The receving power is {} mW'.format(eta*((signal_wavelength/math.pi/4/dist)**2)*100))
    return (eta*((signal_wavelength/math.pi/4/dist)**2)*100*(10**(-3)))


def DeliveryFailure():
    byte = 4 * 360      #the rplidar data package is consist of 360 set of floating number


    N_0 = -174+11+10*math.log(2.4*10**9,10)     #compute the noise spectral power density with respect of 2.4GHz bandwidth, unit dBm
    pN_0 = 10**(N_0/10)     #convert dBm to mW
    #   print('the noise power is {}mW'.format(pN_0,3))


    x = math.sqrt(FSPL()/pN_0)  #receiver to noise energy ratio
    #print('the energy ratio between router and noise is {}.'.format(round(x,3)))


    qpsk = special.erfc(x)  #conpute symbol error rate
    #print('the symbol error rate is {}'.format(qpsk))


    log = math.log(1-qpsk,10)
    deliveryfailure = 1 - math.e**(byte*log)
    print('the probability of delivery failure is: {}.'.format(deliveryfailure))
    


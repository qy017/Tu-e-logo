import numpy as np
from pycrazyswarm import *
from pycrazyswarm import Crazyswarm
from numpy.linalg import norm
import math

Z=1.0
TIMESCALE = 1.0
V = 3.0

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf[0] = swarm.allcfs.crazyflies[0]
    cf[1] = swarm.allcfs.crazyflies[1]
    cf[2] = swarm.allcfs.crazyflies[2]
   
    rotation_axis = [0, 0, 0]

    distance = []
    for i in range(0,3):
        distance[i] = norm(np.array(cf[i].position()) - np.array(rotation_axis))
    
    distance_moving = distance[0]   #distance of the drone the is used as relative to

    rotation_factor = []
    for i in range(0,3):
        if distance[i] != distance_moving:
            rotation_factor[i] = distance[i] / distance_moving
        else:
            rotation_factor[i] = 1

    R = 0.5 #specify radius

    circle_position = []

    theta = math.linsapce(0, 2*math.pi, 0.05) 
    circle_position = [R*math.sin(theta), R*math.cos(theta)]
    i=0
    for theta in range(0, 2*math.pi, 0.05):
        circle_position[i] = [R*math.sin(theta), R*math.cos(theta)]
        i=i+1

    for i in range(0,length(rotation_factor)):
       






    allcfs.takeoff(targetHeight=Z, duration=2.0)
    timeHelper.sleep(2.0)

    for cf in allcfs.crazyflies:
        cf.goTo(np.array(cf.position() + translation_factor),0,V)





    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()

    allcfs.land(targetHeight=0.02, duration=2)
    timeHelper.sleep(3.0)

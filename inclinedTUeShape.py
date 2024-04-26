import numpy as np
from pycrazyswarm import *
from pycrazyswarm import Crazyswarmhttps://www.desmos.com/3d/1fcgvz28wn
from numpy.linalg import norm

Z=1.0
V=3.0

if __name__ == "__main__":

    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf1 = swarm.allcfs.crazyflies[0]
    cf2 = swarm.allcfs.crazyflies[1]
    cf3 = swarm.allcfs.crazyflies[2]
    cf4 = swarm.allcfs.crazyflies[3]
    cf5 = swarm.allcfs.crazyflies[4]
    cf6 = swarm.allcfs.crazyflies[5]
    
    allcfs.takeoff(targetHeight=0.2, duration=2.0)
    timeHelper.sleep(2.0)

    pause = 3.0
    #inclined T-shape:
    
    cf1.goTo(np.array([-0.5,0,1.5]),0,V)
    timeHelper.sleep(pause)
    cf2.goTo(np.array([0,0,1.5]),0,V)
    timeHelper.sleep(pause)
    cf3.goTo(np.array([0.5,0,1.5]),0,V)
    timeHelper.sleep(pause)
    cf4.goTo(np.array([0,-0.2,1.1]),0,V)
    timeHelper.sleep(pause)
    cf5.goTo(np.array([0,-0.4,0.7]),0,V)
    timeHelper.sleep(pause)
    cf6.goTo(np.array([0,-0.6, 0.3]),0,V)


    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()
    pause = 1.0;

    #inclined U-shape:
    cf1.goTo(np.array([0.4,0,1]),0,V)
    timeHelper.sleep(pause)
    cf2.goTo(np.array([-0.4,0,1]),0,V)
    timeHelper.sleep(pause)
    cf3.goTo(np.array([0.4,-0.2,0.5]),0,V)
    timeHelper.sleep(pause)
    cf4.goTo(np.array([-0.2,-0.4,0.1]),0,V)
    timeHelper.sleep(pause)
    cf5.goTo(np.array([-0.4,-0.2, 0.5]),0,V)
    timeHelper.sleep(pause)
    cf6.goTo(np.array([0.2,-0.4,0.1]),0,V)
    timeHelper.sleep(pause)


    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()

    allcfs.land(targetHeight=0.02, duration=2)
    timeHelper.sleep(3.0)

    


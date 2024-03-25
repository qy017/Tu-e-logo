import numpy as np
from pycrazyswarm import *
from pycrazyswarm import Crazyswarm
from numpy.linalg import norm

Z=1.0

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf1 = swarm.allcfs.crazyflies[0]
    cf2 = swarm.allcfs.crazyflies[1]
    cf3 = swarm.allcfs.crazyflies[2]
    cf4 = swarm.allcfs.crazyflies[3]
    cf5 = swarm.allcfs.crazyflies[4]
    
    allcfs.takeoff(targetHeight=Z, duration=2.0)
    timeHelper.sleep(2.0)

    #horizontal T shape:
    cf1.goTo(np.array([-0.5,0,0.5]),0,2.0)
    timeHelper.sleep(2.0)
    cf2.goTo(np.array([0,0,0.5]),0,2.0)
    timeHelper.sleep(2.0)
    cf3.goTo(np.array([0.5,0,0.5]),0,5.0)
    timeHelper.sleep(3.0)
    cf4.goTo(np.array([0,-0.5,0.5]),0,5.0)
    timeHelper.sleep(3.0)
    cf5.goTo(np.array([0,-1,0.5]),0,5.0)

    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()

    #stand up:
    cf1.goTo(np.array([-0.5,0,1.5]),0,2.0)
    timeHelper.sleep(2.0)
    cf2.goTo(np.array([0,0,1.5]),0,2.0)
    timeHelper.sleep(2.0)
    cf3.goTo(np.array([0.5,0,1.5]),0,5.0)
    timeHelper.sleep(3.0)
    cf4.goTo(np.array([0,-0.5,1]),0,5.0)

    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()

    allcfs.land(targetHeight=0.02, duration=1.0+Z)
    timeHelper.sleep(3.0)

    

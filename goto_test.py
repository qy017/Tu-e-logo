import numpy as np
from pycrazyswarm import *
from pycrazyswarm import Crazyswarm
from numpy.linalg import norm

V=2.0

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf0 = swarm.allcfs.crazyflies[0]

    # allcfs.takeoff(targetHeight=0.2, duration=2.0)
    # timeHelper.sleep(2.0)


    while True:
        current_pos = cf0.position()
        if ((norm(np.array(current_pos)-np.array([0,0,0.5]),2)>0.05)):
            cf0.goTo(np.array([0,0,1]),0,V)
        else:
            cf0.goTo(np.array(current_pos),0,0)
            timeHelper.sleep(2.0)
            cf0.goTo(np.array([0,0,1]),0,V)
            timeHelper.sleep(4.0)
            allcfs.land(targetHeight=0.02, duration=3.0)
            timeHelper.sleep(3.0)

    # print("press button to continue...")
    # swarm.input.waitUntilButtonPressed()
    # allcfs.land(targetHeight=0.02, duration=3.0)
    # timeHelper.sleep(3.0)

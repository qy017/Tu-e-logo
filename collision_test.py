import numpy as np
from pycrazyswarm import *
from pycrazyswarm import Crazyswarm
from numpy.linalg import norm

V=5.0

safe_distance =0.15

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf0 = swarm.allcfs.crazyflies[0]
    cf1 = swarm.allcfs.crazyflies[1]

    # allcfs.takeoff(targetHeight=0.2, duration=2.0)
    # timeHelper.sleep(2.0)

    while (True):
        # cf[0].goTo(np.array([0,0,1]),0,V)
        # cf[1].goTo(np.array([-1,0,1]),0,V)
        pos0 = cf0.position()
        pos1 = cf1.position()
        current_pos = cf0.position()
        # d = norm(pos0-pos1,2)
        # print(d)
        # land_d0=norm(np.array(pos0)-np.array([0,0,1]),2)
        # land_d1=norm(np.array(pos1)-np.array([-1,0,1]),2)
        if ((norm(np.array(pos0)-np.array(pos1),2))>safe_distance):
            # current_position = cf0.position()
            cf0.goTo(np.array([0,0,1]),0,V)
            cf1.goTo(np.array([-1,0,1]),0,V)
            current_pos = cf0.position()
            # timeHelper.sleep(3.0)
        else:
            current_pos = cf0.position()
            cf0.goTo(np.array(current_pos),0,0)
            timeHelper.sleep(3.0)
        if ((norm(np.array(pos0)-np.array([0,0,1]),2)<0.02)|(norm(np.array(pos1)-np.array([-1,0,1]),2)<0.02)):
            print("press button to continue...")
            swarm.input.waitUntilButtonPressed()
            allcfs.land(targetHeight=0.02, duration=3.0)
            timeHelper.sleep(2.0)
            break
        
    



import numpy as np
from pycrazyswarm import *
from pycrazyswarm import Crazyswarm
from numpy.linalg import norm

V=2.0
pos=[]
cf=[0,0,0,0,0]
safe_distance =0.5

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf[0] = swarm.allcfs.crazyflies[0]
    cf[1] = swarm.allcfs.crazyflies[1]

    allcfs.takeoff(targetHeight=0.2, duration=2.0)
    timeHelper.sleep(2.0)

    while True:
        cf[0].goTo(np.array([0,0,1]),0,V)
        cf[1].goTo(np.array([-1,0,1]),0,V)
        pos[0] = cf[0].position()
        pos[1] = cf[1].position()
        d = norm(pos[0]-pos[1],2)
        if d<safe_distance:
            current_position = cf[0].position()
            cf[0].goTo(np.array(current_position),0,V) #one drone stays in current position while the others go
            timeHelper.sleep(3.0)
        if ((pos[0]==[0,0,1])&(pos[1]==[-1,0,1])):
            break

    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()
    allcfs.land(targetHeight=0.02, duration=1.0)
    timeHelper.sleep(2.0)



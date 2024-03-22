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
    
    allcfs.takeoff(targetHeight=0.1, duration=2.0)
    timeHelper.sleep(3.0)

    in1 = cf1.position()
    in2 = cf2.position()
    in3 = cf3.position()
    in4 = cf4.position()
    in5 = cf5.position()

    cf1.goTo(np.array([-0.5,0,1.5]),0,5.0)
    timeHelper.sleep(3.0)
    cf2.goTo(np.array([0,0,1.5]),0,5.0)
    timeHelper.sleep(3.0)
    cf3.goTo(np.array([0.5,0,1.5]),0,5.0)
    timeHelper.sleep(3.0)
    cf4.goTo(np.array([0,0,1]),0,5.0)
    timeHelper.sleep(3.0)
    cf5.goTo(np.array([0,0,0.5]),0,5.0)

    #pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
    #cf.goTo(pos, 0, 1.0)
    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()

    cf1.goTo(np.array(in1),0,5.0)
    timeHelper.sleep(3.0)
    cf2.goTo(np.array(in2),0,5.0)
    timeHelper.sleep(3.0)
    cf3.goTo(np.array(in3),0,5.0)
    timeHelper.sleep(3.0)
    cf4.goTo(np.array(in4),0,5.0)
    timeHelper.sleep(3.0)
    cf5.goTo(np.array(in5),0,5.0)

    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()

    allcfs.land(targetHeight=0.02, duration=2.0+Z)
    timeHelper.sleep(2.0)

    


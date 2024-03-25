import numpy as np
from pycrazyswarm import *
from pycrazyswarm import Crazyswarm
from numpy.linalg import norm

Z=0.5
TIMESCALE = 1.0

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf1 = swarm.allcfs.crazyflies[0]
    cf2 = swarm.allcfs.crazyflies[1]
    cf3 = swarm.allcfs.crazyflies[2]
    cf4 = swarm.allcfs.crazyflies[3]
    cf5 = swarm.allcfs.crazyflies[4]

    traj1 = uav_trajectory.Trajectory()
    traj1.loadcsv("wave.csv")

    for cf in allcfs.crazyflies:
            cf.uploadTrajectory(0, 0, traj1)    #What are the zeros in the brackets?
    
    allcfs.takeoff(targetHeight=Z, duration=2.0)
    
    cf1.goTo(np.array([-1,0,1]),0,2.0)
    timeHelper.sleep(2.0)
    cf2.goTo(np.array([-0.5,0,1]),0,2.0)
    timeHelper.sleep(2.0)
    cf3.goTo(np.array([0,0,1]),0,2.0)
    timeHelper.sleep(2.0)
    cf4.goTo(np.array([0.5,0,1]),0,2.0)
    timeHelper.sleep(2.0)
    cf5.goTo(np.array([1,0,1]),0,2.0)
    timeHelper.sleep(2.0)

    for cf in allcfs.crazyflies:
            cf.startTrajectory(0, timescale=TIMESCALE)   
            timeHelper.sleep(0.5)

    timeHelper.sleep(traj1.duration * TIMESCALE + 2.0)


    #pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
    #cf.goTo(pos, 0, 1.0)
    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()

    allcfs.land(targetHeight=0.02, duration=1.0+Z)
    timeHelper.sleep(3.0)
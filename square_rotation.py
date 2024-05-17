#!/usr/bin/env python

import numpy as np

from pycrazyswarm import *
import uav_trajectory

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf0 = swarm.allcfs.crazyflies[0]
    cf1 = swarm.allcfs.crazyflies[1]
    cf2 = swarm.allcfs.crazyflies[2]
    cf3 = swarm.allcfs.crazyflies[3]


    #USE FOR ONE DRONE ONLY CAUSE THEY WILL COLIDE
    traj1 = uav_trajectory.Trajectory()
    traj1.loadcsv("D1.csv")
    traj2 = uav_trajectory.Trajectory()
    traj2.loadcsv("D2.csv")
    traj3 = uav_trajectory.Trajectory()
    traj3.loadcsv("D3.csv")
    traj4 = uav_trajectory.Trajectory()
    traj4.loadcsv("D4.csv")

    
    

    #TRIALS = 1
    TRIALS = 1
    TIMESCALE = 1.0
    for i in range(TRIALS):
        
        cf0.uploadTrajectory(0, 0, traj1)
        cf1.uploadTrajectory(0, 0, traj2)
        cf2.uploadTrajectory(0, 0, traj3)
        cf3.uploadTrajectory(0, 0, traj4)

        allcfs.takeoff(targetHeight=1.0, duration=2.0)
        timeHelper.sleep(2.5)

        cf0.goTo(np.array([-0.75, 0, 1]), 0, 2.0)
        cf1.goTo(np.array([0, -0.75, 1]), 0, 2.0)
        cf2.goTo(np.array([0.75, 0, 1]), 0, 2.0)
        cf3.goTo(np.array([0, 0.75, 1]), 0, 2.0)

        timeHelper.sleep(2.0)


        cf0.startTrajectory(0, timescale=TIMESCALE)
        cf1.startTrajectory(0, timescale=TIMESCALE)
        cf2.startTrajectory(0, timescale=TIMESCALE)
        cf3.startTrajectory(0, timescale=TIMESCALE)
        timeHelper.sleep(traj1.duration * TIMESCALE + 2.0)
        
        # allcfs.startTrajectory(0, timescale=TIMESCALE, reverse=True)
        # timeHelper.sleep(traj1.duration * TIMESCALE + 2.0)

        allcfs.land(targetHeight=0.06, duration=2.0)
        timeHelper.sleep(3.0)


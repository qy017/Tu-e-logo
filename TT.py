import numpy as np
from pycrazyswarm import *
import uav_trajectory

initial_pos = np.array([[-0.5,1.0,0],[0.5,1.0,0],[-1.0,0,0],[0,0,0],[1.0,0,0],[-0.5,-1.0,0],[0.5,-1.0,0]])

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf0 = swarm.allcfs.crazyflies[0]
    cf1 = swarm.allcfs.crazyflies[1]
    cf2 = swarm.allcfs.crazyflies[2]
    cf3 = swarm.allcfs.crazyflies[3]
    cf4 = swarm.allcfs.crazyflies[4]
    cf5 = swarm.allcfs.crazyflies[5]

    traj1 = uav_trajectory.Trajectory()
    traj1.loadcsv("T_1.csv")
    traj2 = uav_trajectory.Trajectory()
    traj2.loadcsv("T_2.csv")
    traj3 = uav_trajectory.Trajectory()
    traj3.loadcsv("T_3.csv")
    traj4 = uav_trajectory.Trajectory()
    traj4.loadcsv("T_4.csv")
    traj5 = uav_trajectory.Trajectory()
    traj5.loadcsv("T_5.csv")
    traj6 = uav_trajectory.Trajectory()
    traj6.loadcsv("T_6.csv")


    #TRIALS = 1
    TRIALS = 1
    TIMESCALE = 1.0
    Z = 0.2
    for i in range(TRIALS):
        
        cf0.uploadTrajectory(0, 0, traj1)
        cf1.uploadTrajectory(0, 0, traj2)
        cf2.uploadTrajectory(0, 0, traj3)
        cf3.uploadTrajectory(0, 0, traj4)
        cf4.uploadTrajectory(0, 0, traj5)
        cf5.uploadTrajectory(0, 0, traj6)

        allcfs.takeoff(targetHeight=Z, duration=2.0)
        timeHelper.sleep(2.5)
        
        cf0.goTo(initial_pos[0,:]+np.array([0,0,Z]), 0, 2.0)
        cf1.goTo(initial_pos[1,:]+np.array([0,0,Z]), 0, 2.0)
        cf2.goTo(initial_pos[2,:]+np.array([0,0,Z]), 0, 2.0)
        cf3.goTo(initial_pos[3,:]+np.array([0,0,Z]), 0, 2.0)
        cf4.goTo(initial_pos[4,:]+np.array([0,0,Z]), 0, 2.0)
        cf5.goTo(initial_pos[5,:]+np.array([0,0,Z]), 0, 2.0)

        # for cf in allcfs.crazyflies:
        #     pos = np.array(cf.initialPosition) + np.array([0, 0, 1.0])
        #     cf.goTo(pos, 0, 2.0)
        timeHelper.sleep(2.5)

        # cf0.goTo(np.array([-0.75, 0, 1]), 0, 2.0)
        # cf1.goTo(np.array([0, -0.75, 1]), 0, 2.0)
        # cf2.goTo(np.array([0.75, 0, 1]), 0, 2.0)
        # cf3.goTo(np.array([0, 0.75, 1]), 0, 2.0)
        
        allcfs.startTrajectory(0, timescale=TIMESCALE)
        timeHelper.sleep(traj1.duration * TIMESCALE + 2.0)
        
        print("press button to continue...")
        swarm.input.waitUntilButtonPressed()

        allcfs.land(targetHeight=0.06, duration=4.0)
        timeHelper.sleep(4.0)


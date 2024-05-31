import numpy as np
from pycrazyswarm import *
import uav_trajectory

initial_pos = np.array([[-0.5,1.0,0],[0.5,1.0,0],[-1.0,0,0],[0,0,0],[1.0,0,0],[-0.5,-1.0,0],[0.5,-1.0,0]])
pos_T = np.array([[-0.7,0,1.7],[0,0,1.7],[0.7,0,1.7],[0,-0.2,1.2],[0,-0.4,0.7],[0,-0.6, 0.2]])
pos_U = np.array([[-0.7,-0.2,0.9],[-0.7,0,1.7],[0.6,0,1.7],[0.6,-0.2,0.9],[-0.3,-0.4,0.2],[0.3,-0.4,0.2]])

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
    cf6 = swarm.allcfs.crazyflies[6]

    trajT1 = uav_trajectory.Trajectory()
    trajT1.loadcsv("T_1.csv")
    trajT2 = uav_trajectory.Trajectory()
    trajT2.loadcsv("T_2.csv")
    trajT3 = uav_trajectory.Trajectory()
    trajT3.loadcsv("T_3.csv")
    trajT4 = uav_trajectory.Trajectory()
    trajT4.loadcsv("T_4.csv")
    trajT5 = uav_trajectory.Trajectory()
    trajT5.loadcsv("T_5.csv")
    trajT6 = uav_trajectory.Trajectory()
    trajT6.loadcsv("T_6.csv")

    trajU1 = uav_trajectory.Trajectory()
    trajU1.loadcsv("U_1.csv")
    trajU2 = uav_trajectory.Trajectory()
    trajU2.loadcsv("U_2.csv")
    trajU3 = uav_trajectory.Trajectory()
    trajU3.loadcsv("U_3.csv")
    trajU4 = uav_trajectory.Trajectory()
    trajU4.loadcsv("U_4.csv")
    trajU5 = uav_trajectory.Trajectory()
    trajU5.loadcsv("U_5.csv")
    trajU6 = uav_trajectory.Trajectory()
    trajU6.loadcsv("U_6.csv")

    trajE1 = uav_trajectory.Trajectory()
    trajE1.loadcsv("E_1.csv")
    trajE2 = uav_trajectory.Trajectory()
    trajE2.loadcsv("E_2.csv")
    trajE3 = uav_trajectory.Trajectory()
    trajE3.loadcsv("E_3.csv")
    trajE4 = uav_trajectory.Trajectory()
    trajE4.loadcsv("E_4.csv")
    trajE5 = uav_trajectory.Trajectory()
    trajE5.loadcsv("E_5.csv")
    trajE6 = uav_trajectory.Trajectory()
    trajE6.loadcsv("E_6.csv")
    trajE7 = uav_trajectory.Trajectory()
    trajE7.loadcsv("E_7.csv")


    #TRIALS = 1
    TRIALS = 1
    TIMESCALE = 1.0
    Z = 0.2
    for i in range(TRIALS):

        #T
        cf0.uploadTrajectory(0, 0, trajT1)
        cf1.uploadTrajectory(0, 0, trajT2)
        cf2.uploadTrajectory(0, 0, trajT3)
        cf3.uploadTrajectory(0, 0, trajT4)
        cf4.uploadTrajectory(0, 0, trajT5)
        cf5.uploadTrajectory(0, 0, trajT6)
        cf0.takeoff(targetHeight=Z, duration=2.0)
        cf1.takeoff(targetHeight=Z, duration=2.0)
        cf2.takeoff(targetHeight=Z, duration=2.0)
        cf3.takeoff(targetHeight=Z, duration=2.0)
        cf4.takeoff(targetHeight=Z, duration=2.0)
        cf5.takeoff(targetHeight=Z, duration=2.0)
        timeHelper.sleep(0.5)
        cf0.goTo(initial_pos[0,:]+np.array([0,0,Z]), 0, 1.0)
        cf1.goTo(initial_pos[1,:]+np.array([0,0,Z]), 0, 1.0)
        cf2.goTo(initial_pos[2,:]+np.array([0,0,Z]), 0, 1.0)
        cf3.goTo(initial_pos[3,:]+np.array([0,0,Z]), 0, 1.0)
        cf4.goTo(initial_pos[4,:]+np.array([0,0,Z]), 0, 1.0)
        cf5.goTo(initial_pos[5,:]+np.array([0,0,Z]), 0, 1.0)
        timeHelper.sleep(1.0)       
        allcfs.startTrajectory(0, timescale=TIMESCALE)
        timeHelper.sleep(trajT1.duration * TIMESCALE + 1.0)
        
        #U
        cf0.goTo(pos_T[0,:]+np.array([0,0,Z]), 0, 1.0)
        cf1.goTo(pos_T[1,:]+np.array([0,0,Z]), 0, 1.0)
        cf2.goTo(pos_T[2,:]+np.array([0,0,Z]), 0, 1.0)
        cf3.goTo(pos_T[3,:]+np.array([0,0,Z]), 0, 1.0)
        cf4.goTo(pos_T[4,:]+np.array([0,0,Z]), 0, 1.0)
        cf5.goTo(pos_T[5,:]+np.array([0,0,Z]), 0, 1.0)
        timeHelper.sleep(1.0) 
        cf0.uploadTrajectory(1, 0, trajU1)
        cf1.uploadTrajectory(1, 0, trajU2)
        cf2.uploadTrajectory(1, 0, trajU3)
        cf3.uploadTrajectory(1, 0, trajU4)
        cf4.uploadTrajectory(1, 0, trajU5)
        cf5.uploadTrajectory(1, 0, trajU6)
      #  timeHelper.sleep(1.0)
        allcfs.startTrajectory(1, timescale=TIMESCALE)
        timeHelper.sleep(trajU1.duration * TIMESCALE + 1.0)

        #E
        cf0.goTo(pos_U[0,:]+np.array([0,0,Z]), 0, 1.0)
        cf1.goTo(pos_U[1,:]+np.array([0,0,Z]), 0, 1.0)
        cf2.goTo(pos_U[2,:]+np.array([0,0,Z]), 0, 1.0)
        cf3.goTo(pos_U[3,:]+np.array([0,0,Z]), 0, 1.0)
        cf4.goTo(pos_U[4,:]+np.array([0,0,Z]), 0, 1.0)
        cf5.goTo(pos_U[5,:]+np.array([0,0,Z]), 0, 1.0)
        cf6.takeoff(targetHeight=Z, duration=1.0)
        cf6.goTo(initial_pos[6,:] +np.array([0,0,Z]), 0, 2.0)
        timeHelper.sleep(1.0)
        cf0.uploadTrajectory(2, 0, trajE1)
        cf1.uploadTrajectory(2, 0, trajE2)
        cf2.uploadTrajectory(2, 0, trajE3)
        cf3.uploadTrajectory(2, 0, trajE4)
        cf4.uploadTrajectory(2, 0, trajE5)
        cf5.uploadTrajectory(2, 0, trajE6)
        cf6.uploadTrajectory(2, 0, trajE7)
        timeHelper.sleep(1.0) 
        allcfs.startTrajectory(2, timescale=TIMESCALE)
        timeHelper.sleep(trajE1.duration * TIMESCALE + 1.0)

        print("press button to continue...")
        swarm.input.waitUntilButtonPressed()

        allcfs.land(targetHeight=0.06, duration=4.0)
        timeHelper.sleep(4.0)

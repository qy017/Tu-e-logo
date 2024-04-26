import numpy as np
from pycrazyswarm import *
from pycrazyswarm import Crazyswarm
from numpy.linalg import norm

Z=1.0
TIMESCALE = 1.0
V = 3.0

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf1 = swarm.allcfs.crazyflies[0]
    cf2 = swarm.allcfs.crazyflies[1]
    cf3 = swarm.allcfs.crazyflies[2]
   

    traj1 = uav_trajectory.Trajectory()
    traj1.loadcsv("circle_trajectory.csv")
    

# Initializing the rotation
    rotation_axis = [0, 0, 1]

    distance = []
    for cf in allcfs.crazyflies:
        distance = abs(cf.position() - rotation_axis) 
    
    distance_moving = distance[0]

    rotation_factor = []
    for single_distance in distance:
        if single_distance != distance_moving:
            rotation_factor = single_distance / distance_moving
        else:
            rotation_factor = 1


    for cf in allcfs.crazyflies:
        for factor in rotation_factor:
            cf.uploadTrajectory(0, 0, traj1 / factor) 


    allcfs.takeoff(targetHeight=Z, duration=2.0)
    timeHelper.sleep(2.0)

    #going to the positions suitable for designed trajectory
    cf1.goTo(np.array([-1.5,0,1]),0,V)
    timeHelper.sleep(2.0)
    cf2.goTo(np.array([-1,0,1]),0,V)
    timeHelper.sleep(2.0)
    cf3.goTo(np.array([-0.5,0,1]),0,V)
    timeHelper.sleep(2.0)
    

    allcfs.startTrajectory(0, timescale=TIMESCALE)  # Will it start those different trajectories for different drones?

    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()

    #Translation
    translation_factor = [0.5, 0 , 0]
    for cf in allcfs.crazyflies:
        cf.goTo(np.array(cf.position() + translation_factor),0,V)


    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()

    allcfs.land(targetHeight=0.02, duration=2)
    timeHelper.sleep(3.0)



# This could be made in such a way that it returs rotation_factor e.g.
# def rotation():

#     """Rotates all the drones with respect to the chosen rotation axis"""

#     rotation_axis = [0, 0, 1]

#     distance = []
#     for cf in allcfs.crazyflies:
#         distance = abs(cf.position() - rotation_axis) 
    
#     distance_moving = distance[0]

#     rotation_factor = []
#     for single_distance in distance:
#         if single_distance != distance_moving:
#             rotation_factor = single_distance / distance_moving
#         else:
#             rotation_factor = 1


#     for cf in allcfs.crazyflies:
#         for factor in rotation_factor:
#             cf.uploadTrajectory(0, 0, traj1 / factor) 

#     allcfs.startTrajectory(0, timescale=TIMESCALE)  # Will it start those different trajectories for different drones?
    


# def translation():
#     """Translates all the drones """

#     translation_factor = [1.2, 0 , 0]
#     for cf in allcfs.crazyflies:
#         cf.goTo(np.array(cf.position() + translation_factor),0,2.0)



# TO-DO:
# dodac goTo pozycje poczatkowe
# Napisac caly kod ze sleep i zakomentowanymi funkcjami
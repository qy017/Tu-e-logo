#########################################################################################
#Two Drones: Leading Following
#########################################################################################


#"""Takeoff-hover-land for one CF. Useful to validate hardware config."""
import numpy as np
from pycrazyswarm import Crazyswarm
from numpy.linalg import norm


TAKEOFF_DURATION = 2
HOVER_DURATION = 5
TURN_DURATION = 4

def main():

    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf_1 = swarm.allcfs.crazyflies[0]
    cf_2 = swarm.allcfs.crazyflies[1]
  #  allcfs = swarm.allcfs

    cf_1.takeoff(targetHeight=0.6, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION)
    Safe_Distance=0.5
    Fly_time=5
    # ##################################################################################
    # #Demo 1: Avoid Collision and Back to Station
    # ##################################################################################
    # while True:
    #      Control_Object=cf_1.position()
    #      Obstacle_position=cf_2.position()
    #      Distance= norm(Control_Object-Obstacle_position,2)
    #      if Distance<Safe_Distance:
    #         element_factor=np.sign(Control_Object-Obstacle_position)
    #         pos_cf1 = np.array(Control_Object)+element_factor*np.array([0.5,0.5,0])
    #         Fly_time=5
    #         cf_1.goTo(pos_cf1, 0, Fly_time)
    #         timeHelper.sleep(TAKEOFF_DURATION)
    #
    #         #  # Obtain the current position information
    #         # Control_Object=cf_1.position()
    #         # Obstacle_position=cf_2.position()
    #         # Distance= norm(Control_Object-Obstacle_position,2)
    #         # if Distance>Safe_Distance:
    #         #    fixed_position_cf1=np.array([0,0,0.6])
    #         #    cf_1.goTo(fixed_position_cf1, 0, Fly_time)


    ##################################################################################
    #Demo 2: Following Objects
    ##################################################################################
    while True:
         Control_Object=cf_1.position()
         Obstacle_position=cf_2.position()
         Distance= norm(Control_Object-Obstacle_position,2)
         if Distance>Safe_Distance:
            element_factor=np.sign(Control_Object-Obstacle_position)
            pos_cf1 = np.array(Obstacle_position)-np.array(element_factor)*np.array([0.2,0.2,-0.2])
            Fly_time=2.5
            cf_1.goTo(pos_cf1, 0, Fly_time)
            timeHelper.sleep(TAKEOFF_DURATION)


    ##################################################################################
    #Demo 3: Formation Control
    ##################################################################################
# #"""Takeoff-hover-land for one CF. Useful to validate hardware config."""
# import numpy as np
# from pycrazyswarm import Crazyswarm


# TAKEOFF_DURATION = 2.5
# HOVER_DURATION = 5
# TURN_DURATION = 4

# def main():

#     swarm = Crazyswarm()
#     timeHelper = swarm.timeHelper
#     cf_1 = swarm.allcfs.crazyflies[0]
#     cf_2 = swarm.allcfs.crazyflies[1]
#     cf_3 = swarm.allcfs.crazyflies[2]
#     cf_4 = swarm.allcfs.crazyflies[3]
#   #  allcfs = swarm.allcfs

#     cf_1.takeoff(targetHeight=0.6, duration=TAKEOFF_DURATION)
#     cf_2.takeoff(targetHeight=0.6, duration=TAKEOFF_DURATION)
#     cf_3.takeoff(targetHeight=0.6, duration=TAKEOFF_DURATION)
#     cf_4.takeoff(targetHeight=0.6, duration=TAKEOFF_DURATION)
#     timeHelper.sleep(TAKEOFF_DURATION + HOVER_DURATION)


#     X_radius=1.8
#     Y_radius=1.2
#     Distance_of_Drones=0.5
#     pos_cf1 = np.array(cf_1.initialPosition) + np.array([-X_radius-0.6, 0, 0])
#     pos_cf2 = np.array(cf_2.initialPosition) + np.array([-X_radius+Distance_of_Drones-0.6, 0, 0])
#     pos_cf3 = np.array(cf_3.initialPosition) + np.array([-X_radius+Distance_of_Drones-0.6, Distance_of_Drones, 0])
#     pos_cf4 = np.array(cf_4.initialPosition) + np.array([-X_radius-0.6, Distance_of_Drones, 0])

#     #Flying time
#     Fly_time=8
#     cf_1.goTo(pos_cf1, 0, Fly_time)
#     cf_2.goTo(pos_cf2, 0, Fly_time)
#     cf_3.goTo(pos_cf3, 0, Fly_time)
#     cf_4.goTo(pos_cf4, 0, Fly_time)

#     timeHelper.sleep(TAKEOFF_DURATION)

#     #First Curve
#     pos_cf1 = np.array(cf_1.initialPosition) + np.array([0, Y_radius-Distance_of_Drones, 0])
#     pos_cf2 = np.array(cf_2.initialPosition) + np.array([Distance_of_Drones,Y_radius-Distance_of_Drones, 0])
#     pos_cf3 = np.array(cf_3.initialPosition) + np.array([Distance_of_Drones,Y_radius, 0])
#     pos_cf4 = np.array(cf_4.initialPosition) + np.array([0, Y_radius, 0])


#     cf_1.goTo(pos_cf1, 0, Fly_time)
#     cf_2.goTo(pos_cf2, 0, Fly_time)
#     cf_3.goTo(pos_cf3, 0, Fly_time)
#     cf_4.goTo(pos_cf4, 0, Fly_time)

#     timeHelper.sleep(TURN_DURATION)


#     #Second Curve
#     pos_cf1 = np.array(cf_1.initialPosition) + np.array([X_radius, 0.8, 0])
#     pos_cf2 = np.array(cf_2.initialPosition) + np.array([X_radius+Distance_of_Drones,0.8, 0])
#     pos_cf3 = np.array(cf_3.initialPosition) + np.array([X_radius+Distance_of_Drones,0.8+Distance_of_Drones , 0])
#     pos_cf4 = np.array(cf_4.initialPosition) + np.array([X_radius,0.8+Distance_of_Drones, 0])

#     cf_1.goTo(pos_cf1, 0, Fly_time)
#     cf_2.goTo(pos_cf2, 0, Fly_time)
#     cf_3.goTo(pos_cf3, 0, Fly_time)
#     cf_4.goTo(pos_cf4, 0, Fly_time)

#     timeHelper.sleep(TURN_DURATION)


#     #Second Curve
#     pos_cf1 = np.array(cf_1.initialPosition) + np.array([X_radius, 0, 0])
#     pos_cf2 = np.array(cf_2.initialPosition) + np.array([X_radius+Distance_of_Drones,0.0, 0])
#     pos_cf3 = np.array(cf_3.initialPosition) + np.array([X_radius+Distance_of_Drones,Distance_of_Drones , 0])
#     pos_cf4 = np.array(cf_4.initialPosition) + np.array([X_radius,Distance_of_Drones, 0])

#     cf_1.goTo(pos_cf1, 0, Fly_time)
#     cf_2.goTo(pos_cf2, 0, Fly_time)
#     cf_3.goTo(pos_cf3, 0, Fly_time)
#     cf_4.goTo(pos_cf4, 0, Fly_time)

#     timeHelper.sleep(TURN_DURATION)


#    #Third Curve
#     pos_cf1 = np.array(cf_1.initialPosition) + np.array([0, -Y_radius, 0])
#     pos_cf2 = np.array(cf_2.initialPosition) + np.array([Distance_of_Drones,-Y_radius, 0])
#     pos_cf3 = np.array(cf_3.initialPosition) + np.array([Distance_of_Drones,Distance_of_Drones-Y_radius, 0])
#     pos_cf4 = np.array(cf_4.initialPosition) + np.array([0,Distance_of_Drones-Y_radius, 0])

#     cf_1.goTo(pos_cf1, 0, Fly_time)
#     cf_2.goTo(pos_cf2, 0, Fly_time)
#     cf_3.goTo(pos_cf3, 0, Fly_time)
#     cf_4.goTo(pos_cf4, 0, Fly_time)

#     timeHelper.sleep(TURN_DURATION)


#   #Fourth Curve
#     pos_cf1 = np.array(cf_1.initialPosition) + np.array([-X_radius, 0, 0])
#     pos_cf2 = np.array(cf_2.initialPosition) + np.array([-X_radius+Distance_of_Drones, 0, 0])
#     pos_cf3 = np.array(cf_3.initialPosition) + np.array([-X_radius+Distance_of_Drones, Distance_of_Drones, 0])
#     pos_cf4 = np.array(cf_4.initialPosition) + np.array([-X_radius, Distance_of_Drones, 0])

#     cf_1.goTo(pos_cf1, 0, Fly_time)
#     cf_2.goTo(pos_cf2, 0, Fly_time)
#     cf_3.goTo(pos_cf3, 0, Fly_time)
#     cf_4.goTo(pos_cf4, 0, Fly_time)

#     timeHelper.sleep(TURN_DURATION)

#   #Back to station
#     cf_1.goTo(cf_1.initialPosition+ np.array([0, 0, 0]), 0, Fly_time)
#     cf_2.goTo(cf_2.initialPosition+ np.array([Distance_of_Drones, 0, 0]), 0, Fly_time)
#     cf_3.goTo(cf_3.initialPosition+ np.array([Distance_of_Drones, Distance_of_Drones, 0]), 0, Fly_time)
#     cf_4.goTo(cf_4.initialPosition+ np.array([0, Distance_of_Drones, 0]), 0, Fly_time)

#     timeHelper.sleep(TAKEOFF_DURATION + HOVER_DURATION)

#     cf_1.land(targetHeight=0.04, duration=2.5)
#     cf_2.land(targetHeight=0.04, duration=2.5)
#     cf_3.land(targetHeight=0.04, duration=2.5)
#     cf_4.land(targetHeight=0.04, duration=2.5)
#     timeHelper.sleep(TAKEOFF_DURATION)



if __name__ == "__main__":
    main()

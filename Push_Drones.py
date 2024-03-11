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

    Initial_time_cf = 0
    angular_vel_cf = 0.4

    cf_1.takeoff(targetHeight=0.5, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION)
    Safe_Distance=0.5
    Logic_variable = True; 
    ##################################################################################
    #Demo 1: Avoid Collision and Back to Station
    ##################################################################################
    while Logic_variable==True:
         Control_Object=cf_1.position()
         Obstacle_position=cf_2.position()
         Distance= norm(Control_Object-Obstacle_position,2)
         if Distance<Safe_Distance:
            element_factor=np.sign(Control_Object-Obstacle_position)
            pos_cf1 = np.array(Control_Object)+element_factor*np.array([0.3,0.3,0])
            Fly_time=2
            cf_1.goTo(pos_cf1, 0, Fly_time)
            timeHelper.sleep(TAKEOFF_DURATION)
          
         Land_dis=norm(Control_Object-np.array([2.5,1,0.5]),2)
         if Land_dis < 0.3:
            cf_1.land(targetHeight=0.02, duration=2.0)
            timeHelper.sleep(6) 
            Logic_variable = False

            


    # ##################################################################################
    # #Demo 2: Following Objects
    # ##################################################################################
    # while Logic_variable==True:
    #      Control_Object=cf_1.position()
    #      Obstacle_position=cf_2.position()
    #      Distance= norm(Control_Object-Obstacle_position,2)
    #      if Distance>Safe_Distance:
    #         element_factor=np.sign(Control_Object-Obstacle_position)
    #         pos_cf1 = np.array(Obstacle_position)-np.array(element_factor)*np.array([0.2,0.2,-0.2])
    #         Fly_time=4
    #         cf_1.goTo(pos_cf1, 0, Fly_time)
    #         timeHelper.sleep(TAKEOFF_DURATION)
    #      Land_dis=norm(Control_Object-np.array([2.5,1,0.5]),2)
    #      if Land_dis < 0.2:
    #         cf_1.land(targetHeight=0.02, duration=2.0)
    #         timeHelper.sleep(6) 
    #         Logic_variable = False


if __name__ == "__main__":
    main()

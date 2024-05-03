import numpy as np
from pycrazyswarm import *
from numpy.linalg import norm

Z=1.0
V=3.0

if __name__ == "__main__":

    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf1 = swarm.allcfs.crazyflies[0]
    cf2 = swarm.allcfs.crazyflies[1]
    cf3 = swarm.allcfs.crazyflies[2]
    cf4 = swarm.allcfs.crazyflies[3]
    cf5 = swarm.allcfs.crazyflies[4]
    cf6 = swarm.allcfs.crazyflies[5]
    cf7 = swarm.allcfs.crazyflies[6]
    
    allcfs.takeoff(targetHeight=0.2, duration=2.0)
    timeHelper.sleep(2.0)

    pause = 1.0
    #inclined T-shape:
    
    cf1.goTo(np.array([-0.7,0,2.0]),0,V)
    timeHelper.sleep(pause)
    cf2.goTo(np.array([0,0,2.0]),0,V)
    timeHelper.sleep(pause)
    cf3.goTo(np.array([0.7,0,2.0]),0,V)
    timeHelper.sleep(pause)
    cf4.goTo(np.array([0,-0.2,1.4]),0,V)
    timeHelper.sleep(pause)
    cf5.goTo(np.array([0,-0.4,0.8]),0,V)
    timeHelper.sleep(pause)
    cf6.goTo(np.array([0,-0.6, 0.2]),0,V)


    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()
    pause = 1.0;

    #inclined U-shape:
    cf1.goTo(np.array([-0.7,0,1]),0,V)
    timeHelper.sleep(pause)
    cf2.goTo(np.array([-0.7,0,2]),0,V)
    timeHelper.sleep(pause)
    cf3.goTo(np.array([0.6,0,2]),0,V)
    timeHelper.sleep(pause)
    cf4.goTo(np.array([0.6,-0.2,1]),0,V)
    timeHelper.sleep(pause)
    cf5.goTo(np.array([-0.3,-0.4,0.2]),0,V)
    timeHelper.sleep(pause)
    cf6.goTo(np.array([0.3,-0.4,0.2]),0,V)
    timeHelper.sleep(pause)

    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()
    pause = 1.0;

    #inclined e-shape:
    cf1.goTo(np.array([-0.7,-0.2,1.1]),0,V)
    timeHelper.sleep(pause)
    cf2.goTo(np.array([-0.4,0,1.7]),0,V)
    timeHelper.sleep(pause)
    cf3.goTo(np.array([0.4,0,1.7]),0,V)
    timeHelper.sleep(pause)
    cf4.goTo(np.array([0.7,-0.2,1.1]),0,V)
    timeHelper.sleep(pause)
    cf5.goTo(np.array([-0.55,-0.4,0.6]),0,V)
    timeHelper.sleep(pause)
    cf6.goTo(np.array([0,-0.2,1.05]),0,V)
    timeHelper.sleep(pause)
    cf6.goTo(np.array([0,-0.6,0.4]),0,V)
    timeHelper.sleep(pause)

    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()

    allcfs.land(targetHeight=0.02, duration=2)
    timeHelper.sleep(3.0)

    


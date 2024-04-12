import numpy as np
from pycrazyswarm import *
from pycrazyswarm import Crazyswarm
from numpy.linalg import norm

Z=0.2 #take off height
V=2.0 #velocity
pos=[]
cf=[0,0,0,0,0]
Safe_Distance=0.5

#horizontal T shape:
T1 = [-0.75,0.5,0.5]
T2 = [0,0.5,0.5]
T3 = [0.75,0.5,0.5]
T4 = [0,-0.25,0.5]
T5 = [0,-1,0.5]

#stand up positions:
T1_stand = [-0.75,0.5,1.5]
T2_stand = [0,0.5,1.5]
T3_stand = [0.75,0.5,1.5]
T4_stand = [0,-0.25,1]


if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf[0] = swarm.allcfs.crazyflies[0]
    cf[1] = swarm.allcfs.crazyflies[1]
    cf[2] = swarm.allcfs.crazyflies[2]
    cf[3] = swarm.allcfs.crazyflies[3]
    cf[4] = swarm.allcfs.crazyflies[4]
    
    allcfs.takeoff(targetHeight=Z, duration=2.0)
    timeHelper.sleep(2.0)

    while True:
        #go to T shape:
        cf[0].goTo(np.array(T1),0,V)
        cf[1].goTo(np.array(T2),0,V)
        cf[2].goTo(np.array(T3),0,V)
        cf[3].goTo(np.array(T4),0,V)
        cf[4].goTo(np.array(T5),0,V)
        #get current positions:
        pos[0] = cf[0].position()
        pos[1] = cf[1].position()
        pos[2] = cf[2].position()
        pos[3] = cf[3].position()
        pos[4] = cf[4].position()

        #check distance between each drone:
        for i in range(0,len(pos)-1):
            for j in range(i,len(pos)-1):
                d = norm(pos[i]-pos[j+1],2)
                if d < Safe_Distance:
                    current_position = cf[j+1].position()
                    cf[j+1].goTo(np.array(current_position),0,V) #one drone stays in current position while the others go
                    timeHelper.sleep(3.0)
        if ((pos[0]==T1)&(pos[1]==T2)&(pos[2]==T3)&(pos[3]==T4)&(pos[4]==T5)): #check if they reached desired position
            break


    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()

    #stand up:
    # cf[0].goTo(np.array(T1_stand),0,V)
    # cf[1].goTo(np.array(T2_stand),0,V)
    # cf[2].goTo(np.array(T3_stand),0,V)
    # cf[3].goTo(np.array(T4_stand),0,V)
    # timeHelper.sleep(2.0)

    # print("press button to continue...")
    # swarm.input.waitUntilButtonPressed()

    allcfs.land(targetHeight=0.02, duration=1.0+Z)
    timeHelper.sleep(3.0)

    

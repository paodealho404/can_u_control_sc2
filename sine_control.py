from math import *
from server_base import Server
import numpy as np

from lands_functions import *

# controlSignal = 0.00
uMax = 1
dt = 0.02
filterU = 0.45

class Control:

    def __init__(self, verbose = False):

        self.verbose = verbose
        self.time = 0.0
        self.controlSignal = 0.0

    def constrain(self, val, min_val, max_val):
        return max(min(val, max_val), min_val)
    
    def closestDistanceToPositions(self, targetX, targetY, positions):
        dMin = 100000.0
        
        for (i, value) in enumerate(positions):
            p = value

            d = ((p[0]-targetX)*(p[0]-targetX) + (p[1]-targetY)*(p[1]-targetY)) + 0.001*i

            if d<dMin:
                dMin = d

        return dMin

    def futurePositions(self, x, y, U, land, level, N, dt):
        positions = []
        
        NBlocks = len(U)
        
        U.append(U[NBlocks-1])
        
        p = [x, y]
        for i in range(N):
            positions.append([p[0],p[1]])

            uIndex = floor(NBlocks*i/N)

            u = U[uIndex]
            xp = landsFunctions(land, level, p[0], p[1], u)

            p[0] += xp[0]*dt
            p[1] += xp[1]*dt

        return positions

    def computeBestU(self, x, y, land, level, N, dt, targetX, targetY):
        uStar = 0.0

        # minPos = []
        dMin = 100000.0

        for ut1 in np.arange(-uMax, uMax, uMax/10):
            for ut2 in np.arange(-uMax, uMax, uMax/10) :
                positions = self.futurePositions(x, y, [ut1, ut2], land, level, N, dt)
                d = self.closestDistanceToPositions(targetX, targetY, positions)
                
                if d<dMin:
                    dMin = d
                    uStar = ut1

                    # minPos = positions

        return uStar


    def step(self, received):
        if received:
            try:
                land, level = received[1], received[2]
                player_x, player_y = received[3], received[4]
                target_x, target_y = received[5], received[6]

                self.controlSignal = filterU*self.controlSignal + (1.0 - filterU)*self.computeBestU(player_x, player_y, land, level, 100, 2*dt, target_x, target_y)
                
                self.controlSignal = self.constrain(self.controlSignal, -uMax, uMax)
                
                self.time += dt

                return self.controlSignal
        
            except Exception:
                print('Error in control step')
                pass
            
        # return 0


if __name__=='__main__':

    control = Control()

    server = Server(control)

    server.run()









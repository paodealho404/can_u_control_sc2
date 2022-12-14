from math import *
import numpy as np

from lands_functions import *
from lands_parameters import *

def constrain(val, min_val, max_val):
  return max(min(val, max_val), min_val)

def computeBestDistance(targetX, targetY, positions):
  minDistance = 100000
  
  for (i, position) in enumerate(positions):
    currentDistance = ((position[0] - targetX) * (position[0] - targetX) + (position[1] - targetY)*(position[1] - targetY))

    if currentDistance < minDistance:
      minDistance = currentDistance

  return minDistance

def computePositions(x, y, U, land, level, testDepth, dt):
  positions = []

  uLength = len(U)

  U.append(U[uLength-1])

  p = [x, y]

  for i in range(testDepth):
    positions.append([p[0], p[1]])

    uIndex = floor(uLength * i / testDepth)

    u = U[uIndex]
    xp = landsFunctions(land, level, p[0], p[1], u)

    p[0] += xp[0]*dt
    p[1] += xp[1]*dt

  return positions

def estimateSignal(x, y, land, level, testDepth, dt, targetX, targetY, upperLimit, lowerLimit):
  bestControlSignal = 0

  minDistance = 100000

  signalsToTest = np.arange(lowerLimit, upperLimit, (abs(upperLimit) + abs(lowerLimit)) / 20)

  for i in signalsToTest:
    for j in signalsToTest:
      positions = computePositions(x, y, [i, j], land, level, testDepth, dt)
      currentDistance = computeBestDistance(targetX, targetY, positions)

      if currentDistance < minDistance:
        minDistance = currentDistance
        bestControlSignal = i

  return bestControlSignal
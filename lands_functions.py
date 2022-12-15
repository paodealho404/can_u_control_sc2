from math import *
import numpy as np

def landsFunctions(land, level, x, y, u):
  
  # LinearLand
  if land == 1:
    if level == 1:
      return [-5.2*x + 2.5*y + 3.2*u, -9*x - 0.8*y + 5.0*u]
    elif level == 2:
      return [5.0*y, -0.9*y -9.0*x + 5*u]
    elif level == 3:
      return [2.0*y - 1.2*x, -0.4*y + 3.6*x - 5*u]
    elif level == 4:
      return [1.0*x - 0.4*y + 0.6*u, 1.8*x + 0.2*y - 5.0*u]
  elif land == 2:
  # Non-linearLand
    if level == 1:
      return [3*y + u, -3*sin(8*x) - y]
    elif level == 2:
      f = atan(4*x)
      return [2*y - 2*x + f + 2*u, 2*x - 2*y]
    elif level == 3:
      return [3*x*(0.5*x + 1.5*y) + 2.0*u, 3*(x-y) + u*u]
    elif level == 4:
      return [-(x-0.7)*(x+0.7)/0.1 + 5.0*u, -y + 2*u]
  # SwitchingLand
  elif land == 3:
    if level == 1:
      x *= 10
      y *= 10
      u *= 5
      
      A = np.array([[0, 1], [-0.5, -0.5]])
      B = np.array([0.5, 0.8])
      
      if x > y:
        xp = A[0, 0] * x + A[0, 1] * y + B[0] * u + 3
        yp = A[1, 0] * x + A[1, 1] * y + B[1] * u
      else:
        xp = A[0, 0] * x + A[0, 1] * y + B[0] * u - 3.0
        yp = A[1, 0] * x + A[1, 1] * y + B[1] * u
      
      return [xp/3, yp/3]
    elif level == 2:
      A = np.array([[0, -1], [-0.25, 0]])

      if x > y:
        xp = A[0, 0] * x + A[0, 1] * y
        yp = A[1, 0] * x + A[1, 1] * y + 2 * u
      else:
        xp = A[0, 0] * x + A[0, 1] * y
        yp = A[1, 0] * x + A[1, 1] * y - 2 * u

      return [xp, yp]
    elif level == 3:
      x *= 10
      y *= 10
      u *= 5
      
      A = np.array([[0, -1], [1, 0]])

      if x > y:
        xp = A[0, 0] * x + A[0, 1] * y
        yp = A[1, 0] * x + A[1, 1] * y + 4 + u
      else:
        xp = A[0, 0] * x + A[0, 1] * y
        yp = A[1, 0] * x + A[1, 1] * y - 4 + u
        
      return [xp/4, yp/4]
    elif level == 4:
      x *= 10
      y *= 10
      u *= 5
      
      A = np.array([[0.7578, -1.9796], [1.7454, -0.3350]])
      B = np.array([0.1005, -2.1600])
      V = np.array([-0.1582, 1.8467])
      a = 1.2759
      
      if (V[0] * x + V[1] * y) > 0:
        xp = A[0, 0] * x + A[0, 1] * y + a * B[0] * u
        yp = A[1, 0] * x + A[1, 1] * y + a * B[1] * u
      else:
        xp = A[0, 0] * x + A[0, 1] * y - a * B[0] * u
        yp = A[1, 0] * x + A[1, 1] * y - a * B[1] * u
        
      return [xp/6, yp/6]
  # QuantizedLand
  elif land == 4:
    if level == 1:
      x *= 10
      y *= 10
      u *= 5
      
      A = np.array([[0, 1], [-0.5, -0.5]])
      B = np.array([0.5, 0.8])
      
      xp = A[0, 0] * x + A[0, 1] * y + B[0] * u
      yp = A[1, 0] * x + A[1, 1] * y + B[1] * u
      
      xp = 4 if xp > 0 else -4
      yp = 4 if yp > 0 else -4
      
      return [xp/5, yp/5]
    elif level == 2:
      x *= 10
      y *= 10
      u *= 5

      A = np.array([[0, -1], [1, 0]])
      B = np.array([0, 1])
      
      xp = A[0, 0] * x + A[0, 1] * y + B[0] * u
      yp = A[1, 0] * x + A[1, 1] * y + B[1] * u

      if (xp > 0 and xp < 2):
          xp = 2
      if (xp < 0 and xp > -2):
          xp = -2
      if (xp > 2):
          xp = 4
      if (xp < -2):
          xp = -4

      if (yp > 0 and yp < 2):
          yp = 2
      if (yp < 0 and yp > -2):
          yp = -2
      if (yp > 2):
          yp = 4
      if (yp < -2):
          yp = -4

      return [xp/5, yp/5]

    elif level == 3:
      x *= 10
      y *= 10
      u *= 5

      A = np.array([[0, 1], [1, 0]])
      B = np.array([0, 2])
      
      xp = A[0, 0] * x + A[0, 1] * y + B[0] * u
      yp = A[1, 0] * x + A[1, 1] * y + B[1] * u

      if (xp > 0 and xp < 2):
          xp = 2
      if (xp < 0 and xp > -2):
          xp = -2
      if (xp > 2):
          xp = 4
      if (xp < -2):
          xp = -4

      if (yp > 0 and yp < 2):
          yp = 2
      if (yp < 0 and yp > -2):
          yp = -2
      if (yp > 2):
          yp = 4
      if (yp < -2):
          yp = -4

      return [xp/5, yp/5]

    elif level == 4:
      x *= 10
      y *= 10
      u *= 5
      
      xp = y + u
      yp = -(9.8/1.0) * sin(x) - 0.1 * y
      
      xp = 2 if xp > 0 else -2
      yp = 2 if yp > 0 else -2
      
      return [xp/5, yp/5]
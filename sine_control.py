from math import *
from server_base import Server
import numpy as np

from lands_functions import *

uStar = 0
uMax = 1
dt = 0.06
    
def computeBestU():
	uStar = 0

	dMin = 100000

	# for ut1 in np.arange(-uMax, uMax, uMax / 10):
	# 	for ut2 in np.arange(-uMax, uMax, uMax / 10):
	# 		position = 


print(landsFunctions(1, 5, 6, -0.))
class Control:

	def __init__(self, verbose = False):

		self.verbose = verbose
		self.time = 0.0

	def step(self, received):

		print(received)

		controlSignal = sin(self.time)

		self.time += dt

		return controlSignal


if __name__=='__main__':

	control = Control()

	server = Server(control)

	server.run()









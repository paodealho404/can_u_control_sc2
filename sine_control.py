from math import *
from server_base import Server

dt = 0.06;

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









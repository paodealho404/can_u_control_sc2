from math import *
from serial import Serial
from server_base import Server


class HardwareControl:

	def __init__(self, serialPort, verbose = False):

		self.verbose = verbose
		self.serial = Serial('/dev/'+serialPort, 115200)

	def step(self, received):

		controlSignal = 0.0

		try:
			self.serial.flushInput()
			self.serial.read_until().decode("utf-8") 
			controlSignal = (float(self.serial.read_until().decode("utf-8"))-450.0)/450.0
			print(f'u = {controlSignal}') if self.verbose else None

		except:
			print('Problem with serial or socket...') if self.verbose else None

		return controlSignal


if __name__=='__main__':

	control = HardwareControl('tty.wchusbserial14640', True)

	server = Server(control, True)

	server.run()

import asyncio
import websockets
import time

# time between control signal applications
deltaTime = 0.03



class Server:

	def __init__(self, controller, verbose = False):

		self.verbose = verbose             # verbose flag (true means print debug info)
		self.controller = controller       # controller to be used
		self.received = []                 # buffer with game data to be sent to controller


	async def serverLoop(self, websocket, path):

		while True:
			time.sleep(deltaTime)

			try:

				values = [float(x) if x != '' else 0  for x in self.received]

				# compute control signal based on game data (invoking controller)
				controlSignal = self.controller.step(values)

				# send control signal to the game
				print(f'sending {controlSignal}') if self.verbose else None
				await websocket.send(f'{controlSignal}')


				# get game data from the game (store it to compute next control signal)
				self.received = (await websocket.recv()).split(',')
				print(self.received) if self.verbose else None

			except:
				print('System not active...') if self.verbose else None
				break;


	def run(self):

		while True:
			server = websockets.serve(self.serverLoop, "localhost", 6660)

			asyncio.get_event_loop().run_until_complete(server)
			asyncio.get_event_loop().run_forever()



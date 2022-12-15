from math import *
from server_base import Server
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://dev-mind.blog/apps/CanUControl/index.html")
time.sleep(5)
ok_button = driver.find_element(By.XPATH, "//button[normalize-space()='Ok']")
ok_button.click()
element = driver.find_element(By.ID, "inputImg")
playerInput = ''

while playerInput != "websocket.png":
  element.click()
  playerInput = element.get_attribute("src").split('/')[-1]
  print(playerInput)
  time.sleep(1)

startGameButton = driver.find_element(By.ID, "menu1")
startGameButton.click()

dt = 0.06

class Control:

	def __init__(self, verbose = False):

		self.verbose = verbose
		self.time = 0.0
		self.stage = 0

	def step(self, received):
		print(received)
		print("Stage: ", self.stage)
		time.sleep(2)

		if self.stage % 4 == 0 and self.stage != 0:
			goToMenuStagesButton = driver.find_element(By.ID, 'dialog-confirm')
			goToMenuStagesButton.click()
			time.sleep(2)
			try:
				playNewStage = driver.find_element(By.XPATH, "//img[@id='player']/following-sibling::img")
				playNewStage.click()
			except:
				pass
   #player changeLandButton
		try: 
			playButton = driver.find_element(By.XPATH, "//button[normalize-space()='GO!']")
			playButton.click()
		except:
			print("No play button")
		time.sleep(1)

		driver.execute_script("player.position = target.position")
  
		self.stage += 1
		controlSignal = 0
		# controlSignal = sin(self.time)

		# self.time += dt

		return controlSignal


if __name__=='__main__':

	control = Control()

	server = Server(control)

	server.run()









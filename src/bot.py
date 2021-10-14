import pydirectinput
from time import sleep, time

class Bot:
	state = 'idle'
	reeling = False
	count = 0
	start = time()
	lastCaught = time()

	def fish(self, hookpoints, reelpoints, successpoints):
		if len(hookpoints):
			print('WE GOT ONE CAPTN')
			pydirectinput.click()
			self.state = 'reeling'

		if self.state == 'reeling':
			if len(reelpoints):
				if not self.reeling:
					print('PUUUUULLLLLL')
					self.reeling = True
				pydirectinput.mouseDown()
			else:
				if self.reeling:
					print('wait...')
					self.reeling = False
				pydirectinput.mouseUp()

		if len(successpoints):
			pydirectinput.click()
			self.count += 1
			curTime = time()
			elapsedTime = (curTime-self.start)
			print(f'success in {round(curTime-self.lastCaught, 2)}s! | caught: {self.count} | elapsed time: {round(elapsedTime/60, 2)}m | fish/min: {round(self.count/(elapsedTime/60), 2)} | fish/hr: {round(self.count/(elapsedTime/60/60), 2)}')
			self.lastCaught = curTime
			self.state = 'idle'
			sleep(1)
			self.recast()

	def recast(self):
		print('here we go again...')
		pydirectinput.mouseDown()
		sleep(1.9)
		pydirectinput.mouseUp()

	def getState(self):
		return self.state

	def cleanKeys(self):
		pydirectinput.keyUp('left')
		pydirectinput.keyUp('right')

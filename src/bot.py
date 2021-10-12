import pydirectinput
from time import sleep

class Bot:
	state = 'idle'
	reeling = False

	def fish(self, hookpoints, reelpoints, successpoints):
		if len(hookpoints):
			print('WE GOT ONE CAPTN')
			pydirectinput.click()
			self.state = 'reeling'

		if self.state == 'reeling':
			if len(reelpoints):
				if not self.reeling:
					print('reeling')
					self.reeling = True
				pydirectinput.mouseDown()
			else:
				if self.reeling:
					print('wait...')
					self.reeling = False
				pydirectinput.mouseUp()

		if len(successpoints):
			print('success!')
			self.state = 'idle'
			sleep(6)
			self.recast()

	def recast(self):
		print('casting')
		self.cleanKeys()
		pydirectinput.click()

	def getState(self):
		return self.state

	def cleanKeys(self):
		pydirectinput.keyUp('left')
		pydirectinput.keyUp('right')

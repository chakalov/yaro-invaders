class Level:
	def __init__(self, waves):
		self.waves = waves
		self.current = 0
	
	def prepare(self):
		pass
	
	def isFinished(self):
		return self.waves[self.current].hasEnemies()
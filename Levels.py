import pickle
import Ships

class Levels:
	def __init__(self, allEnemies):
		self.levelIndex = 0
		self.allEnemies = allEnemies
		
		levels = open("levels/standart.lvl", "rb")
		self.levels = pickle.load(levels)
		levels.close()
	
	def nextLevel(self):
		if self.levelIndex < len(self.levels):
			self.loadLevel(self.levels[self.levelIndex])
			self.levelIndex += 1
			return True
		else:
			return False
	
	def loadLevel(self, data):
		self.locations, self.interval, self.startY = data
		for location in self.locations:
			self.allEnemies.add(Ships.BaseShip.BaseShip("images/invader2.png", 50, 1, location, 3.5, Ships.Weapons.BaseWeapon.BaseWeapon((25, -25), 1, 3000, Ships.Weapons.Bullets.AlienBomb.AlienBomb)))
	
	def runPattern(self):
		for ship in self.allEnemies:
			ship.intervalMove(self.interval)
	
	def isFinished(self):
		return len(self.allEnemies) == 0
import pickle
import Ships
import random

class Levels:
	def __init__(self, allEnemies):
		self.levelIndex = 0
		self.allEnemies = allEnemies
		self.startY = 0
		
		levels = open("levels/standart.lvl", "rb")
		self.levels = pickle.load(levels)
		levels.close()
	
	def getBonusPointsForCurrentLevel(self):
		return len(self.levels[self.levelIndex - 1][0] * 5)
	
	def getPointsPerKillForCurrentLevel(self):
		return (self.levelIndex) * 10
	
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
			x, y = location
			self.allEnemies.add(Ships.AlienShips.SimpleShip.SimpleShip(random.choice(["images/invader2.png", "images/invader2a.png", "images/invader3.png"]), 50, (x, y - self.startY), 1.5, Ships.Weapons.BaseWeapon.BaseWeapon((25, -25), 1, 0, 3000, Ships.Weapons.Bullets.AlienBomb.AlienBomb)))
	
	def moveDownSlowly(self):
		if self.startY > 0:
			for ship in self.allEnemies:
				ship.moveDown()
			self.startY -= 1.5
		return self.startY <= 0
	
	def runPattern(self):
		for ship in self.allEnemies:
			ship.intervalMove(self.interval)
	
	def isFinished(self):
		return len(self.allEnemies) == 0
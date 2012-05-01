import Ships

class Wave(object):
	def __init__(self, locations, interval):
		self.ships = []
		self.locations = locations
		self.interval = interval
		for location in self.locations:
			self.ships.append(Ships.BaseShip.BaseShip("images/invader2.png", 50, 1, location, 3.5, Ships.Weapons.BaseWeapon.BaseWeapon((25, -25), 1, 3000, Ships.Weapons.Bullets.AlienBomb.AlienBomb)))
	
	def runPattern(self):
		for i in range(len(self.ships)):
			self.ships[i].randomMove((self.locations[i][0] - self.interval, self.locations[i][0] + self.interval))
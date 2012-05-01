import Ships

class Player(object):
	image = None
	def __init__(self, location):
		self.ship = Ships.BaseShip.BaseShip("images/player_ship.png", 100, 3, location, 3.5, Ships.Weapons.BaseWeapon.BaseWeapon((0, 60), 0.1, 30000, Ships.Weapons.Bullets.BaseBullet.BaseBullet, 10, 1))
	
	def move(self, pos):
		self.ship.move(pos)
	
	def shoot(self):
		return self.ship.shoot()
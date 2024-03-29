import Ships

class Player(object):
	image = None
	def __init__(self, location):
		self.ship = Ships.PlayerShip.PlayerShip("images/player_ship.png", 100, 3, location, 3.5, Ships.Weapons.BaseWeapon.BaseWeapon((0, 40), 0.1, 0.25, 30000, Ships.Weapons.Bullets.BaseBullet.BaseBullet, 10, 1))
	
	def move(self, pos):
		self.ship.move(pos)
	
	def shoot(self):
		return self.ship.shoot()


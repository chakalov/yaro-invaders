import Ships

class Enemy(object):
	image = None
	def __init__(self, location):
		self.ship = Ships.BaseShip.BaseShip("images/invader2.png", 20, 3, location, 3.5, Ships.Weapons.BaseWeapon.BaseWeapon((25, -25), 1, 3000, Ships.Weapons.Bullets.AlienBomb.AlienBomb))
	
	def shoot(self):
		if self.ship.canShoot():
			return self.ship.shoot()
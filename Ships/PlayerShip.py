import Ships.BaseShip

class PlayerShip(Ships.BaseShip.BaseShip):
	def __init__(self, image, maxHealth, lives, location, moveSpeed, weapon, shield = None):
		Ships.BaseShip.BaseShip.__init__(self, image, maxHealth, location, moveSpeed, weapon)
		self.lives = lives
		self.stunned = False
		self.slowed = False
		self.shield = shield
		self.health = maxHealth
	
	def canShoot(self):
		return self.stunned == False and Ships.BaseShip.BaseShip.canShoot(self)
	
	def enemyCollide(self):
		self.health = 0
		return self.kill()

	def kill(self):
		if self.health <= 0:
			if self.lives <= 0:
				return super(PlayerShip, self).kill()
			else:
				self.lives -= 1
				self.health = self.maxHealth
				explosion = self.explode()
				self.position = (512, 700)
				return explosion
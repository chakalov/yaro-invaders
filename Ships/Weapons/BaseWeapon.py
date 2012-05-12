import pygame
from threading import Timer

class BaseWeapon(object):
	sound = None
	def __init__(self, weaponLocation, shootSpeed, reloadTime, maxBullets, Bullet, damage = 10, direction = -1):
		if BaseWeapon.sound is None:
			BaseWeapon.sound = pygame.mixer.Sound("sounds/Shoot.wav")
			BaseWeapon.sound.set_volume(0.1)
			
		
		self.weaponLocation = weaponLocation
		self.shootSpeed = shootSpeed
		self.reloadTime = reloadTime
		
		self.bullets = maxBullets
		self.maxBullets = maxBullets
		
		self.direction = direction
		self.Bullet = Bullet
		self.damage = damage
		
		self.ready = True
	
	def shoot(self, location):
		if self.ready and self.bullets > 0:
			self.ready = False
			self.shootInterval = Timer(self.shootSpeed + self.reloadTime, self.setReady)
			self.shootInterval.start()
			self.bullets = self.bullets - 1
			self.sound.play()
			return self.Bullet((location[0] - self.weaponLocation[0], location[1] - self.weaponLocation[1]), (0, 4 * self.direction), self.damage)
	
	def setReady(self):
		self.ready = True

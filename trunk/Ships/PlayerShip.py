import pygame
import random
import Ships.BaseShip

class PlayerShip(Ships.BaseShip.BaseShip):
	max_x_pos = None
	max_y_pos = None
	def __init__(self, image, maxHealth, lives, location, moveSpeed, weapon, shield = None):
		Ships.BaseShip.BaseShip.__init__(self, image, maxHealth, location, moveSpeed, weapon)
		self.lives = lives
		self.stunned = False
		self.slowed = False
		self.shield = shield
	
	def canShoot(self):
		return self.stunned == False and Ships.BaseShip.BaseShip.canShoot(self)
	
	def takeDamage(self, damage):
		self.health -= damage
		if self.health <= 0 and self.lives <= 0:
			self.kill()
		else:
			self.lives -= 1
			self.health = self.maxHealth

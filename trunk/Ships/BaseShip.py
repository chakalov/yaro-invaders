import pygame
import random

class BaseShip(pygame.sprite.Sprite):
	max_x_pos = None
	max_y_pos = None
	def __init__(self, image, maxHealth, location, moveSpeed, weapon):
		pygame.sprite.Sprite.__init__(self)
		
		if BaseShip.max_x_pos is None:
			BaseShip.max_x_pos = pygame.display.get_surface().get_width()
		if BaseShip.max_y_pos is None:
			BaseShip.max_y_pos = pygame.display.get_surface().get_height()
		
		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		
		self.health = maxHealth
		self.maxHealth = maxHealth
		self.isKilled = False
		
		self.initPosition = location
		self.position = location
		self.moveSpeed = moveSpeed
		
		self.weapon = weapon
		self.weapon.position = ((self.position[0], self.position[1]))
	
	def move(self, rel):
		self.position = (self.position[0] + rel[0], self.position[1] + rel[1])
		self.isOutOfScreen()
	
	def intervalMove(self, offset):
		self.position = (self.position[0] + self.moveSpeed, self.position[1])
		if self.initPosition[0] - offset > self.position[0] or self.position[0] >= self.initPosition[0] + offset:
			self.moveSpeed = self.moveSpeed * (-1)
	
	def takeDamage(self, damage):
		self.health -= damage
		if self.health <= 0:
			self.kill()
	
	def isOutOfScreen(self):
		if 0 > self.position[0]:
			self.position = (0, self.position[1])
		elif self.position[0] > BaseShip.max_x_pos:
			self.position = (BaseShip.max_x_pos, self.position[1])
		if 0 > self.position[1]:
			self.position = (self.position[0], 0)
		elif self.position[1] > BaseShip.max_y_pos:
			self.position = (self.position[0], BaseShip.max_y_pos)
	
	def shoot(self):
		if self.canShoot():
			return self.weapon.shoot(self.position)
	
	def randomShoot(self):
		if random.randint(0, 10) == 0:
			return self.shoot()
	
	def canShoot(self):
		return self.weapon.ready
	
	def update(self):
		self.rect.center = self.position
	
	def kill(self):
		self.isKilled = True
		pygame.sprite.Sprite.kill(self)

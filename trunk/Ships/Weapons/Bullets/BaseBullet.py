import pygame

class BaseBullet(pygame.sprite.Sprite):
	image = None
	max_y_pos = None
	def __init__(self, location, moveSpeed, damage):
		pygame.sprite.Sprite.__init__(self)
		if BaseBullet.image is None:
			BaseBullet.image = pygame.image.load("images/BaseBullet.png").convert_alpha()
		self.image = BaseBullet.image
		if BaseBullet.max_y_pos is None:
			BaseBullet.max_y_pos = pygame.display.get_surface().get_height()
		
		self.rect = self.image.get_rect()
		
		self.damage = damage
		self.moveSpeed = moveSpeed
		
		self.position = location
		self.rect.center = location
	
	def checkOutofScreen(self):
		if self.position[1] <= 0 or self.position[1] >= BaseBullet.max_y_pos:
			self.kill()
	
	def checkCollision(self, targets):
		for target in targets:
			if self.rect.colliderect(target):
				self.hitTarget(target)
				return True
	
	def hitTarget(self, target):
		target.takeDamage(self.damage)
		self.kill()
	
	def update(self):
		self.position = (self.position[0] - self.moveSpeed[0], self.position[1] - self.moveSpeed[1])
		self.checkOutofScreen()
		self.rect.center = self.position
		
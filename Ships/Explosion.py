import pygame

class Explosion(pygame.sprite.Sprite):
	images = None
	sound = None
	def __init__(self, location):
		pygame.sprite.Sprite.__init__(self)
		self.frame = 0
		if Explosion.images is None:
			Explosion.images = []
			master_image = pygame.image.load('images/Explosion.png').convert_alpha()
			 
			master_width, master_height = master_image.get_size()
			for i in range(int(master_width / 97)):
				self.images.append(master_image.subsurface((i * 97, 0, 97, 100)))
		
		if Explosion.sound is None:
			Explosion.sound = pygame.mixer.Sound("sounds/Explosion.wav")
			Explosion.sound.set_volume(0.4)
		
		self.maxFrame = len(self.images)
		
		self._start = pygame.time.get_ticks()
		self._delay = 33
		self._last_update = 0
		
		self.update()
		self.sound.play()
		self.rect = self.image.get_rect()
		self.rect.center = location
	
	def update(self):
		if pygame.time.get_ticks() - self._last_update > self._delay:
			if self.frame >= self.maxFrame:
				self.kill()
			else:
				self.image = self.images[self.frame]
				self.frame += 1
				self._last_update = pygame.time.get_ticks()
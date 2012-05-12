import pygame

class TinyExplosion(pygame.sprite.Sprite):
	images = None
	sound = None
	def __init__(self, location):
		pygame.sprite.Sprite.__init__(self)
		self.frame = 0
		if TinyExplosion.images is None:
			TinyExplosion.images = []
			master_image = pygame.image.load('images/tinyExplosion.png').convert_alpha()
			 
			master_width, master_height = master_image.get_size()
			for i in range(int(master_width / 11)):
				self.images.append(master_image.subsurface((i * 11, 0, 11, 11)))
		
		if TinyExplosion.sound is None:
			TinyExplosion.sound = pygame.mixer.Sound("sounds/TargetHit.wav")
			TinyExplosion.sound.set_volume(1)
		
		self.maxFrame = len(self.images)
		
		self._start = pygame.time.get_ticks()
		self._delay = 30
		self._last_update = 0
		
		self.sound.play()
		self.update()
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
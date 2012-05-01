import pygame
from Ships.Weapons.Bullets.BaseBullet import BaseBullet

class AlienBomb(BaseBullet):
	image = None
	max_y_pos = None
	def __init__(self, location, moveSpeed, damage):
		BaseBullet.__init__(self, location, moveSpeed, damage)
		if AlienBomb.image is None:
			AlienBomb.image = pygame.image.load("images/AlienBomb.png").convert_alpha()
		self.image = AlienBomb.image
	
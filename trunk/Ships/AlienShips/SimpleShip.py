import pygame
import random
import Ships.BaseShip

class SimpleShip(Ships.BaseShip.BaseShip):
	def __init__(self, image, maxHealth, location, moveSpeed, weapon):
		Ships.BaseShip.BaseShip.__init__(self, image, maxHealth, location, moveSpeed, weapon)
		weapon.sound = pygame.mixer.Sound("sounds/EnemyShoot.wav")
		weapon.sound.set_volume(0.1)

import sys, pygame
from Player import Player
from Wave import Wave

class Invaders:
	def __init__(self):
		pygame.init()
		self.setUpDisplay()
		self.setUpSprites()
	
	def setUpDisplay(self, width = 1024, height = 768):
		pygame.mouse.set_visible(False)
		pygame.event.set_grab(True)
		self.resolution = (width, height)
		self.screen = pygame.display.set_mode(self.resolution, pygame.DOUBLEBUF and pygame.HWSURFACE and pygame.FULLSCREEN, 32)
		self.bg_img = pygame.image.load("images/bg_img.jpg").convert()
		self.clock = pygame.time.Clock()
		self.offset = 0
	
	def setUpSprites(self):
		self.allSprites = pygame.sprite.Group()
		self.allPlayers = pygame.sprite.Group() # if 2 players play
		self.allEnemies = pygame.sprite.Group()
		self.allFriendlyBullets = pygame.sprite.Group()
		self.allEnemyBullets = pygame.sprite.Group()
		
		self.player = Player(pygame.mouse.get_pos())
		self.allSprites.add(self.player.ship)
		self.allPlayers.add(self.player.ship)
		
		self.wave = Wave([
						(112, 100), (212, 100), (312, 100), (412, 100), (512, 100), (612, 100), (712, 100), (812, 100), (912, 100),
						(112, 200), (212, 200), (312, 200), (412, 200), (512, 200), (612, 200), (712, 200), (812, 200), (912, 200),
						(112, 300), (212, 300), (312, 300), (412, 300), (512, 300), (612, 300), (712, 300), (812, 300), (912, 300)
						], 100)
		self.allSprites.add(self.wave.ships)
		self.allEnemies.add(self.wave.ships)
	
	def drawBackground(self):
		img_rect = self.bg_img.get_rect()
		nrows = int(self.resolution[1] / img_rect.height) + 1
		ncols = int(self.resolution[0] / img_rect.width) + 1
		
		self.offset = (self.offset + 0.7) % img_rect.height
		
		if self.offset > 0:
			first_row = -1
			last_row = nrows
		else:
			first_row = 0
			last_row = nrows + 1
		
		for y in range(first_row, last_row):
			for x in range(ncols):
				img_rect.topleft = (x * img_rect.width, y * img_rect.height + self.offset)
				self.screen.blit(self.bg_img, img_rect)
	
	def run(self):
		left_button_pressed = False
		while True:
			time_passed = self.clock.tick(50)
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
				elif event.type == pygame.MOUSEMOTION:
					self.player.move(pygame.mouse.get_rel())
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					left_button_pressed = True
				elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
					left_button_pressed = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.quit()
				
			if left_button_pressed:
				bullet = self.player.shoot()
				if not bullet is None:
					self.allSprites.add(bullet)
					self.allFriendlyBullets.add(bullet)
			
			self.drawBackground()
			self.allSprites.update()
			
			for bullet in self.allFriendlyBullets:
				bullet.checkCollision(self.allEnemies)
			
			for bullet in self.allEnemyBullets:
				bullet.checkCollision([self.player.ship])
			
			self.wave.runPattern()
			for enemy in self.allEnemies:
				for player in self.allPlayers:
					if enemy.position[0] >= player.position[0] - 8 and enemy.position[0] <= player.position[0] + 8:
						bullet = enemy.randomShoot()
						if not bullet is None:
							self.allSprites.add(bullet)
							self.allEnemyBullets.add(bullet)
			
			self.allSprites.draw(self.screen)
			pygame.display.flip()
	
	def quit(self):
		sys.exit()

if __name__ == "__main__":
	Invaders().run()

import sys, pygame
from Player import Player
from Levels import Levels

class Invaders:
	def __init__(self):
		pygame.init()
		self.setUpDisplay()
		self.setUpSprites()
		self.setUpLevels()
		self.setUpPlayers()
		self.controls = [{"controller": "mouse", "shoot": 1}]
		self.buttonsPressed = {"mouse": {1: False}, "keyboard": {}}
		self.playerWins = False
	
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
	
	def setUpLevels(self):
		self.levels = Levels(self.allEnemies)
	
	def setUpPlayers(self):
		self.players = [Player((500, 600))] # Single Player for now
		self.allPlayers.add(self.players[0].ship)
		self.allSprites.add(self.players[0].ship)
	
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
	
	def UserEvents(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit()
			else:
				if event.type == pygame.MOUSEMOTION:
					self.players[0].move(pygame.mouse.get_rel()) # TODO: move it outside
				elif event.type == pygame.MOUSEBUTTONDOWN:
					self.buttonsPressed["mouse"][event.button] = True
				elif event.type == pygame.MOUSEBUTTONUP:
					self.buttonsPressed["mouse"][event.button] = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.quit()
		
		if self.buttonsPressed["mouse"][self.controls[0]["shoot"]]:
			bullet = self.players[0].shoot()
			if not bullet is None:
				self.allSprites.add(bullet)
				self.allFriendlyBullets.add(bullet)
	
	def AIEvents(self):
		self.levels.runPattern()
		for enemy in self.allEnemies:
			for player in self.allPlayers:
				if enemy.position[0] >= player.position[0] - 8 and enemy.position[0] <= player.position[0] + 8:
					bullet = enemy.randomShoot()
					if not bullet is None:
						self.allSprites.add(bullet)
						self.allEnemyBullets.add(bullet)
	
	def GameEvents(self):
		# level checks
		if self.levels.isFinished():
			hasNextLevel = self.levels.nextLevel()
			if hasNextLevel == False:
				self.running = False
				self.playerWins = True
			else:
				self.allSprites.add(self.allEnemies)
		
		# update sprites and check for collisions
		self.allSprites.update()
		for bullet in self.allFriendlyBullets:
			bullet.checkCollision(self.allEnemies)
		for bullet in self.allEnemyBullets:
			bullet.checkCollision([self.players[0].ship])
	
	def run(self):
		self.running = True
		while self.running:
			time_passed = self.clock.tick(50)
			
			# check if events occured and process them
			self.UserEvents()
			self.AIEvents()
			self.GameEvents()
			
			# draw
			self.drawBackground()
			self.allSprites.draw(self.screen)
			pygame.display.flip()
		print(self.playerWins)
	
	def quit(self):
		self.running = False

if __name__ == "__main__":
	Invaders().run()

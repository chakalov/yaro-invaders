import os, sys, pygame
from threading import Timer
from Player import Player
from Levels import Levels

class Invaders:
	def __init__(self):
		os.environ["SDL_VIDEO_CENTERED"] = "1"
		pygame.init()
		pygame.mixer.init()
		
		self.setUpDisplay()
		self.setUpSprites()
		self.setUpLevels()
		self.setUpPlayers()
		
		# setup other stuff
		self.controls = [{"controller": "mouse", "shoot": 1}]
		self.buttonsPressed = {"mouse": {1: False}, "keyboard": {}}
		self.playerWins = False
		self.enemiesLoaded = False
		self.pointsPerKill = 1
		self.score = 0
		self.bonusPoints = 0
	
	def setUpDisplay(self, width = 1024, height = 768):
		pygame.mouse.set_visible(False)
		pygame.event.set_grab(True)
		self.resolution = (width, height)
		self.screen = pygame.display.set_mode(self.resolution, pygame.DOUBLEBUF and pygame.HWSURFACE and pygame.FULLSCREEN, 32)
		pygame.display.set_caption('YARO Invaders')
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
		background = pygame.Surface(self.screen.get_size())
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
				background.blit(self.bg_img, img_rect)
		
		font = pygame.font.Font(None, 36)
		font.set_italic(True)
		text = font.render('Lives: ' + str(self.players[0].ship.lives + 1), True, (255, 255, 255))
		textpos = text.get_rect()
		textpos.topleft = background.get_rect().topleft
		background.blit(text, textpos)
		
		font = pygame.font.Font(None, 36)
		font.set_italic(True)
		text = font.render('Score: ' + str(self.score), True, (255, 255, 255))
		textpos = text.get_rect()
		textpos.topright = background.get_rect().topright
		background.blit(text, textpos)
		
		self.screen.blit(background, (0, 0))
	
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
					else:
						self.buttonsPressed["keyboard"][event.key] = True
				elif event.type == pygame.KEYUP:
					self.buttonsPressed["keyboard"][event.key] = False
		
		if self.buttonsPressed["mouse"][self.controls[0]["shoot"]] or (pygame.K_SPACE in self.buttonsPressed["keyboard"] and self.buttonsPressed["keyboard"][pygame.K_SPACE]):
			bullet = self.players[0].shoot()
			if not bullet is None:
				self.allSprites.add(bullet)
				self.allFriendlyBullets.add(bullet)
		
		# for keyboard
		coord_x, coord_y = (0, 0)
		if pygame.K_UP in self.buttonsPressed["keyboard"] and self.buttonsPressed["keyboard"][pygame.K_UP]:
			coord_y -= 5
		if pygame.K_DOWN in self.buttonsPressed["keyboard"] and self.buttonsPressed["keyboard"][pygame.K_DOWN]:
			coord_y += 5
		if pygame.K_LEFT in self.buttonsPressed["keyboard"] and self.buttonsPressed["keyboard"][pygame.K_LEFT]:
			coord_x -= 5
		if pygame.K_RIGHT in self.buttonsPressed["keyboard"] and self.buttonsPressed["keyboard"][pygame.K_RIGHT]:
			coord_x += 5
		
		if coord_x != 0 or coord_y != 0:
			self.players[0].move((coord_x, coord_y))
		
	
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
			self.enemiesLoaded = False
			hasNextLevel = self.levels.nextLevel()
			if hasNextLevel == False:
				self.running = False
				self.playerWins = True
			else:
				if self.bonusPoints > 0:
					self.score += int(self.bonusPoints)
				self.pointsPerKill = self.levels.getPointsPerKillForCurrentLevel()
				self.bonusPoints = self.levels.getBonusPointsForCurrentLevel()
				self.allSprites.add(self.allEnemies)
		
		if len(self.allPlayers) == 0:
			self.running = False
			self.playerWins = False
			return
		
		# update sprites and check for collisions
		self.allSprites.update()
		for bullet in self.allFriendlyBullets:
			explosion = bullet.checkCollision(self.allEnemies)
			if not explosion is None:
				self.allSprites.add(explosion)
				self.score += int(int(explosion.points) * self.pointsPerKill)
		for bullet in self.allEnemyBullets:
			explosion = bullet.checkCollision([self.players[0].ship])
			if not explosion is None:
				self.allSprites.add(explosion)
				self.bonusPoints -= explosion.points
		if pygame.sprite.spritecollide(self.players[0].ship, self.allEnemies, False):
			explosion = self.players[0].ship.enemyCollide()
			if not explosion is None:
				self.allSprites.add(explosion)
				self.bonusPoints -= explosion.points
	
	def run(self):
		self.running = True
		while self.running:
			time_passed = self.clock.tick(50)
			
			# check if events occured and process them
			self.UserEvents()
			if self.enemiesLoaded:
				self.AIEvents()
			elif len(self.allEnemies) > 0 :
				self.enemiesLoaded = self.levels.moveDownSlowly()
				
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

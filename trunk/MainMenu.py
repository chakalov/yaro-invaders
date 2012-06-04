import os, sys, pygame
from Invaders import Invaders
from Label import Label

class MainMenu:
	def __init__(self):
		os.environ["SDL_VIDEO_CENTERED"] = "1"
		pygame.init()
		pygame.mixer.init()
		self.setUpDisplay()
	
	def setUpDisplay(self, width = 713, height = 400):
		pygame.mouse.set_visible(True)
		pygame.event.set_grab(False)
		self.resolution = (width, height)
		self.screen = pygame.display.set_mode(self.resolution, pygame.DOUBLEBUF and pygame.HWSURFACE, 32)
		pygame.display.set_caption('YARO Invaders')
		self.bg_img = pygame.image.load("images/menu.png").convert()
		self.clock = pygame.time.Clock()
		self.offset = 0
		self.labels = pygame.sprite.Group()
		self.labels.add(Label("Start Game", (386, 280), self.StartGame));
		self.labels.add(Label("Quit", (386, 320), self.Quit));
	
	def StartGame(self):
		Invaders().run()
		self.__init__()
	
	def Quit(self):
		self.running = False
		
	def UserEvents(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit()
			elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.quit()
			elif event.type == pygame.MOUSEMOTION:
				x,y = event.pos
				for label in self.labels:
					label.highlight(label.rect.collidepoint(x,y))
			elif event.type == pygame.MOUSEBUTTONDOWN:
				for label in self.labels:
					if label.isMouseOver():
						label.action()
	
	def run(self):
		self.running = True
		while self.running:
			time_passed = self.clock.tick(30)
			self.UserEvents()
			
			# draw
			self.screen.blit(self.bg_img, (0, 0))
			self.labels.draw(self.screen)
			pygame.display.flip()
	
	def quit(self):
		self.running = False

if __name__ == "__main__":
	MainMenu().run()

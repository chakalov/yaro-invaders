import pygame

class Label(pygame.sprite.Sprite):
	def __init__(self, label, location, action):
		pygame.sprite.Sprite.__init__(self)
		
		self.font = pygame.font.Font(None, 36)
		self.font.set_italic(True)
		self.text = label
		self.position = location
		self.isHighlightSet = None
		self.command = action
		self.highlight(False)
	
	def highlight(self, isSet):
		if isSet != self.isHighlightSet:
			self.isHighlightSet = isSet
			if self.isHighlightSet:
				self.color = (255, 255, 0)
			else:
				self.color = (255, 255, 255)
			self.update()
		
	def update(self):
		self.image = self.font.render(self.text, True, self.color)
		self.rect = self.image.get_rect()
		self.rect.center = self.position

	def isMouseOver(self):
		return self.isHighlightSet
	
	def action(self):
		self.command()
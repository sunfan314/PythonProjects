import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self,ai_settings,screen):
		super(Alien,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#load alien image
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#set alien initial position
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
	def blitme(self):
		self.screen.blit(self.image,self.rect)
	def update(self):
		self.x += self.ai_settings.alien_speed_factor
		self.rect.x = self.x

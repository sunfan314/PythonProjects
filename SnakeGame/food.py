from settings import Settings
import random
import pygame

class Food():
	def __init__(self):
		self.settings = Settings()
		self.food_size = self.settings.food_size

		self.rect = pygame.Rect(-1,-1,self.food_size,self.food_size)

	def remove(self):
		self.rect.x = -1

	def add(self):
		if self.rect.x < 0:
			random_x = []
			random_y = []
			for x in range(20,self.settings.screen_width-20,self.food_size):
				random_x.append(x)
			for x in range(20,self.settings.screen_height-20,self.food_size):
				random_y.append(x)
			self.rect.left = random.choice(random_x)
			self.rect.top = random.choice(random_y)



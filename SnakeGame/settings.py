import pygame

class Settings():
	def __init__(self):
		#screen settings
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (255,255,255)

		#snake settings
		self.snake_init_direction = pygame.K_RIGHT
		self.snake_init_length = 5
		self.snake_init_pos_x = 60
		self.snake_init_pos_y = 60
		self.snake_size = 20
		self.snake_color = (0,0,0)

		#food settings
		self.food_color = (0,0,0)
		self.food_size = 20
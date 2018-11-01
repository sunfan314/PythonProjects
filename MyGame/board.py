import pygame
from pygame.sprite import Sprite

class Board(Sprite):
	def __init__(self,settings,screen,ifBottom):
		super(Board,self).__init__()
		self.settings = settings
		self.screen = screen
		self.screen_rect = screen.get_rect()

		#create a board
		self.rect = pygame.Rect(0,0,settings.board_width,settings.board_height)
		self.rect.centerx = self.screen_rect.centerx
		if ifBottom:
			self.rect.bottom = self.screen_rect.bottom - 20
		else:
			self.rect.bottom = self.screen_rect.top + 20
	
		self.centerx = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)

		self.color =settings.board_color
		self.speed_x_factor = settings.board_speed_x_factor
		self.speed_y_factor = settings.board_speed_y_factor

		self.moving_left = False
		self.moving_right = False
		self.moving_up = False
		self.moving_down = False

	def draw_board(self):
		pygame.draw.rect(self.screen,self.color,self.rect)

	def update(self):
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.settings.board_speed_x_factor
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.settings.board_speed_x_factor
		if self.moving_up and self.rect.top > 5:
			self.bottom -= self.settings.board_speed_y_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.bottom += self.settings.board_speed_y_factor
		self.rect.centerx = self.centerx
		self.rect.bottom = self.bottom
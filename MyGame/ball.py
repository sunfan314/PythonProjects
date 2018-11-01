import pygame
from pygame.sprite import Sprite
import random

class Ball(Sprite):
	def __init__(self,settings,screen):
		super(Ball,self).__init__()
		self.settings = settings
		self.color = settings.ball_color
		self.radius = settings.ball_radius
		self.rect = pygame.Rect(0,0,settings.ball_radius,settings.ball_radius)
		self.screen = screen
		self.screen_rect = screen.get_rect()

		#create a ball
		self.x = 80
		self.y = 80
		self.rect.centerx = self.x
		self.rect.bottom = self.y
		self.pos = (self.x,self.y)
		self.speed_x_factor =  0
		while self.speed_x_factor == 0:
			self.speed_x_factor = settings.ball_max_speed_x_factor * random.random()
		self.speed_y_factor = 0
		while self.speed_y_factor == 0:
			self.speed_y_factor = settings.ball_max_speed_y_factor * random.random()

	def update(self):
		if self.speed_x_factor > 0 and self.x + self.speed_x_factor > self.screen_rect.right:
			self.speed_x_factor *= -1
		if self.speed_x_factor < 0 and self.x + self.speed_x_factor < 0:
			self.speed_x_factor *= -1
		if self.speed_y_factor > 0 and self.y + self.speed_y_factor > self.screen_rect.bottom:
			self.speed_y_factor *= -1
		if self.speed_y_factor < 0 and self.y + self.speed_y_factor < 0:
			self.speed_y_factor *= -1
		self.x += self.speed_x_factor
		self.y += self.speed_y_factor
		self.pos = (int(self.x),int(self.y))
		self.rect.centerx = self.x
		self.rect.bottom = self.y

	def draw_ball(self):
		pygame.draw.circle(self.screen,self.color,self.pos,self.radius) 

	def turn(self):
		self.speed_y_factor *= -1


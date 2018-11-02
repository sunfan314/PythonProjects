import pygame
import sys
from settings import Settings

class Snake():
	#initialize the snake
	def __init__(self):
		self.settings = Settings()
		self.length = self.settings.snake_init_length
		self.direction = self.settings.snake_init_direction
		self.snake_size = self.settings.snake_size
		self.body = []
		for x in range(self.length):
			self.addNode()
	def addNode(self):
		#body is not empty
		if self.body:
			left = self.body[0].left
			top = self.body[0].top
			if self.direction == pygame.K_RIGHT:
				left += self.snake_size
			elif self.direction == pygame.K_LEFT:
				left -= self.snake_size
			elif self.direction == pygame.K_UP:
				top -= self.snake_size
			elif self.direction == pygame.K_DOWN:
				top += self.snake_size
			self.body.insert(0,pygame.Rect(left,top,self.snake_size,self.snake_size))
		#body is empty
		else:
			left = self.settings.snake_init_pos_x
			top = self.settings.snake_init_pos_y
			self.body.append(pygame.Rect(left,top,self.snake_size,self.snake_size))
	def removeNode(self):
		self.body.pop()

	def move(self):
		self.addNode()
		self.removeNode()

	def isDead(self):
		#hit the wall
		if self.body[0].x not in range(self.settings.screen_width):
			return True
		if self.body[0].y not in range(self.settings.screen_height):
			return True
		#hit self
		if self.body[0] in self.body[1:]:
			return True
		return False

	def changeDirection(self,key):
		LR = [pygame.K_LEFT,pygame.K_RIGHT]
		UD = [pygame.K_UP,pygame.K_DOWN]
		if key in LR+UD:
			if key in LR and self.direction in LR:
				return
			if key in UD and self.direction in UD:
				return
			self.direction = key



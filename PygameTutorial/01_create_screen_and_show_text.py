import pygame
import sys

pygame.init()
white = 255,255,255
black = 0,0,0
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("My Test")
screen.fill(white)
my_font = pygame.font.Font(None,40)
text_image = my_font.render("hello world!",True,black)
while(True):
	for event in pygame.event.get():
		if event.type in (pygame.QUIT,pygame.KEYDOWN):
			sys.exit()
	screen.fill(white)
	screen.blit(text_image,(300,200))
	pygame.display.update()

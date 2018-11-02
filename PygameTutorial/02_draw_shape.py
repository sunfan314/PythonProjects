import pygame
import sys


screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Draw a circle")
white = 255,255,255
black = 0,0,0

while True:
	for event in pygame.event.get():
		if event.type in (pygame.QUIT,pygame.KEYDOWN):
			sys.exit()

		screen.fill(white)
		pygame.draw.circle(screen,black,(300,200),50,2)
		pygame.draw.rect(screen,black,((450,200),(50,50)),2)
		pygame.draw.line(screen,black,(200,400),(200,500),2)
		pygame.draw.lines(screen,black,True,((250,300),(250,350),(300,350)),2)
		pygame.display.update()
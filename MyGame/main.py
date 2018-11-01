import sys
import pygame
from settings import Settings
import game_functions as gf
from board import Board
from ball import Ball


def run_game():
	settings = Settings()
	screen = pygame.display.set_mode(
		(settings.screen_width,settings.screen_height))
	board1 = Board(settings,screen,True)
	board2 = Board(settings,screen,False)
	ball = Ball(settings,screen)
	pygame.display.set_caption("My Game") 

	#game main loop
	while True:
		gf.check_events(screen,board1,board2)
		board1.update()
		board2.update()
		gf.update_ball(settings,screen,board1,board2,ball)
		gf.update_screen(settings,screen,board1,board2,ball)

run_game()
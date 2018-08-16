import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#init pygame, settings and screen
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#create a ship
	ship = Ship(ai_settings,screen)

	#game main loop
	while True:
		#monitor keyboard and mouse event
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings,screen,ship)
run_game()
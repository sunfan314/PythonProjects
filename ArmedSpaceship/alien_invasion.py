import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_status import GameStatus

def run_game():
	#init pygame, settings and screen
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	status = GameStatus(ai_settings)
	#create a ship
	ship = Ship(ai_settings,screen)
	#create alien groups
	aliens = Group()
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#create bullet groups
	bullets = Group()

	#game main loop
	while True: 
		#monitor keyboard and mouse event
		gf.check_events(ai_settings,screen,ship,bullets)
		if status.game_active:
			ship.update()
			#update bullets first to check if bullets meet any alien
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
			gf.update_aliens(ai_settings,status,screen,ship,aliens,bullets)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
run_game()
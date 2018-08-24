import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_status import GameStatus
from button import Button
from scoreboard import ScoreBoard

def run_game():
	#init pygame, settings and screen
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	play_button = Button(ai_settings,screen,"Play")

	stats = GameStatus(ai_settings)
	sb = ScoreBoard(ai_settings,screen,stats)
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
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			ship.update()
			#update bullets first to check if bullets meet any alien
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
run_game()
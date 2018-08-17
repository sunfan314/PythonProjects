import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings,screen,ship,bullets):
	# response to keyboard and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)


def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True	
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False
def create_fleet(ai_settings,screen,ship,aliens):
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_aliens_y = get_number_aliens_y(ai_settings,ship.rect.height,alien.rect.height)
	for row_number in range(number_aliens_y):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)
def get_number_aliens_x(ai_settings,alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x
def get_number_aliens_y(ai_settings,ship_height,alien_height):
	available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
	number_alien_y = int(available_space_y / (2 * alien_height))
	return number_alien_y
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien_height = alien.rect.height
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.y = alien_height + 2 * alien_height * row_number
	alien.rect.x = alien.x
	alien.rect.y = alien.y
	aliens.add(alien) 
def update_screen(ai_settings,screen,ship,aliens,bullets):
		#re-draw screen
		screen.fill(ai_settings.bg_color)
		#draw bullets
		for bullet in bullets.sprites():
			bullet.draw_bullet()
		ship.blitme()
		aliens.draw(screen)
		#make recently drawed screen visible
		pygame.display.flip()
def update_bullets(bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
def update_aliens(aliens):
	aliens.update()
		
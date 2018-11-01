import sys
import pygame

def check_events(screen,board1,board2):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,board1,board2)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,board1,board2)
def check_keydown_events(event,board1,board2):
	if event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_LEFT:
		board1.moving_left = True
	elif event.key == pygame.K_RIGHT:
		board1.moving_right = True
	elif event.key == pygame.K_UP:
		board1.moving_up = True
	elif event.key == pygame.K_DOWN:
		board1.moving_down = True
	elif event.key == pygame.K_a:
		board2.moving_left = True
	elif event.key == pygame.K_d:
		board2.moving_right = True
	elif event.key == pygame.K_w:
		board2.moving_up = True
	elif event.key == pygame.K_s:
		board2.moving_down = True

def check_keyup_events(event,board1,board2):
	if event.key == pygame.K_LEFT:
		board1.moving_left = False
	elif event.key == pygame.K_RIGHT:
		board1.moving_right = False
	elif event.key == pygame.K_UP:
		board1.moving_up = False
	elif event.key == pygame.K_DOWN:
		board1.moving_down = False
	elif event.key == pygame.K_a:
		board2.moving_left = False
	elif event.key == pygame.K_d:
		board2.moving_right = False
	elif event.key == pygame.K_w:
		board2.moving_up = False
	elif event.key == pygame.K_s:
		board2.moving_down = False

def update_screen(settings,screen,board1,board2,ball):
	screen.fill(settings.bg_color)
	board1.draw_board()
	board2.draw_board()
	ball.draw_ball()
	pygame.display.flip()

def update_ball(settings,screen,board1,board2,ball):
	ball.update()
	check_board_ball_collisions(settings,screen,board1,board2,ball)

def check_board_ball_collisions(settings,screen,board1,board2,ball):
	if pygame.sprite.collide_rect(board1,ball) or pygame.sprite.collide_rect(board2,ball):
		ball.turn()

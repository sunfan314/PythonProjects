import pygame
import sys
from settings import Settings
from snake import Snake
from food import Food

def main():
	#initialize the font
	pygame.init()
	settings = Settings()
	screen_size = (settings.screen_width,settings.screen_height)
	screen = pygame.display.set_mode(screen_size)
	clock = pygame.time.Clock()

	snake = Snake()
	food = Food()

	isDead = False

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				snake.changeDirection(event.key)
				if event.key == pygame.K_SPACE and isDead:
					return main()

		screen.fill(settings.bg_color)

		if not isDead:
			snake.move()
			for rect in snake.body:
				pygame.draw.rect(screen,settings.snake_color,rect)

		isDead = snake.isDead()

		if isDead:
			show_text(screen,(100,200),'YOU ARE DEAD!',(227,29,18),False,20)

		if food.rect == snake.body[0]:
			food.remove()
			snake.addNode()

		food.add()
		pygame.draw.rect(screen,settings.food_color,food.rect)

		pygame.display.update()
		clock.tick(500)
def show_text(screen, pos, text, color, font_bold = False, font_size = 20, font_italic = False):   
    #获取系统字体，并设置文字大小  
    cur_font = pygame.font.SysFont("Arial", font_size)  
    #设置是否加粗属性  
    cur_font.set_bold(font_bold)  
    #设置是否斜体属性  
    cur_font.set_italic(font_italic)  
    #设置文字内容  
    text_fmt = cur_font.render(text, 1, color)  
    #绘制文字  
    screen.blit(text_fmt, pos)
main()

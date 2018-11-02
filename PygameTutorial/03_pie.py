import sys
import pygame

def main():
	pygame.init()
	screen = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Pie")

	pies = [False,False,False,False]
	black = (0,0,0)
	white = (255,255,255)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			#if event.type == pygame.KEYDOWN and event.key in (pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4):
				#if event.key == pygame.K_1 and not pies[0]:
					#pygame.draw.lines(screen,black,True,((),(),()),2)


		my_font = pygame.font.Font(None,20)
		text_image_1 = my_font.render("1",True,black)
		text_image_2 = my_font.render("2",True,black)
		text_image_3 = my_font.render("3",True,black)
		text_image_4 = my_font.render("4",True,black)
		screen.fill(white)
		screen.blit(text_image_1,(300,200))
		screen.blit(text_image_2,(350,200))
		screen.blit(text_image_3,(350,250))
		screen.blit(text_image_4,(300,250))

		pygame.display.update()
main()
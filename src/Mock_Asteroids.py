import pygame, random, math, sys, time

#-----------------------------------------------------------------------------------
#	base code to get a screen with background and some text
#-----------------------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((640,480))

background = pygame.image.load("../images/background.bmp")

dialog_Box = pygame.image.load("../images/dialog_Box.bmp").convert(24)
dialog_Box.set_colorkey((135,254,255))
alpha = 255
step = -50

test_rect = dialog_Box.get_rect()
print(test_rect)

test = pygame.Surface((dialog_Box.x,dialog_Box.y))
test.fill((255,255,255))

a = []

'font for the specified text'
text_font = pygame.font.Font("../fonts/trench100free.ttf",30)
text_color = (90,90,90)

seconds = 0
tempo = pygame.time.get_ticks()
cont = 1
while True:
	pressed_Keys = pygame.key.get_pressed()

	if (pygame.time.get_ticks() - tempo) >= 1000:
		seconds += 1
		tempo = pygame.time.get_ticks()
		cont = 1
	if seconds % 2 == 0:
		dialog_Box.set_alpha(alpha)
		alpha += step
		if seconds % 6 == 0:
			step *= -1
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if pressed_Keys[pygame.K_q]:
				sys.exit()

	screen.blit(background,(0,0))

	screen.blit(dialog_Box,(40,390))
	screen.blit(test,(0,0))

	screen.blit(text_font.render("Time: " + str(seconds), True, (255,255,255)),(10,0))

	pygame.display.flip()

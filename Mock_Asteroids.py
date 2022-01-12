import pygame, random, math, sys, time

'mock asteroid works'
'making change to test commit'
def create_Asteroid(name, color):
	'name will be the path of the image file'
	asteroid = pygame.image.load(name)

	'set colorkey will be for ignore the ciano pixels that were used in the asteroid drawing'
	asteroid.set_colorkey(color)

	'get_rect will get the rectangle of the image'
	asteroidrect = asteroid.get_rect()

	'zeros in the velocities is because they start not moving at all'
	a_velocity_x = 0
	a_velocity_y = 0

	'now we have to calculate the angle that this particular asteroid will move'
	'chosing were the asteroid will spawn of the screen'
	random.seed()

	position = random.choice([1,2])

	if position == 1:
		pos_x = random.randint(1,640)
		pos_y = 0

		if pos_x <= 320:
			asteroid_Angle = random.randint(91,180)
		elif pos_x > 320:
			asteroid_Angle = random.randint(1,90)

	elif position == 2:
		pos_x = random.randint(1,640)
		pos_y = 480

		if pos_x <= 320:
			asteroid_Angle = random.randint(181,270)
		elif pos_x > 320:
			asteroid_Angle = random.randint(270,359)

	elif position == 3:
		pos_x = 0
		pos_y = random.randint(1,480)

		if pos_y <= 240:
			asteroid_Angle = random.randint(181,270)
		elif pos_y > 240:
			asteroid_Angle = random.randint(91,180)

	elif position == 4:
		pos_x = 640
		pos_y = random.randint(1,480)

		if pos_y <= 240:
			asteroid_Angle = random.randint(270,359)
		elif pos_y > 240:
			asteroid_Angle = random.randint(1,90)

	asteroidrect.center = (pos_x,pos_y)

	'now we return'
	return asteroid, asteroidrect, asteroid_Angle, a_velocity_x, a_velocity_y

def moveasteroid(cont, asteroid_Angle, a_velocity_x, a_velocity_y):
	if cont == 1:
		a_velocity_x += (-math.cos(math.radians(asteroid_Angle)))
		a_velocity_y += (math.sin(math.radians(asteroid_Angle)))
	else:
		pass

	return a_velocity_x, a_velocity_y


pygame.init()
screen = pygame.display.set_mode((640,480))

background = pygame.image.load("background.bmp")

a = []

'font for the specified text'
text_font = pygame.font.Font("fonts/trench100free.ttf",30)
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
	
	if seconds % 1 == 0 and cont == 1:
		a.append(list(create_Asteroid("asteroid.bmp",(135,254,255))))
		cont = 0


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if pressed_Keys[pygame.K_q]:
				sys.exit()

	screen.blit(background,(0,0))

	for i in a:
		i[3], i[4] = moveasteroid(1,i[2],i[3],i[4])
		new_a_x = i[1].center[0] + (i[3]*1.5)
		new_a_y = i[1].center[1] + (i[4]*1.5)

		'conditional to see if the asteroid escaped'
		if new_a_x > 640 or new_a_x < 0 or new_a_y > 480 or new_a_y < 0:
			a.pop(a.index(i))
			conti = 0
		else:
			center = (new_a_x, new_a_y)
			asteroid_copy = i[0].copy()
			asteroid_copy = pygame.transform.rotate(asteroid_copy, i[2]+90)
			asteroid_copy_rect = asteroid_copy.get_rect()
			asteroid_copy_rect.center = center
			screen.blit(asteroid_copy,asteroid_copy_rect)


	screen.blit(text_font.render("Time: " + str(seconds), True, (255,255,255)),(10,0))

	pygame.display.flip()

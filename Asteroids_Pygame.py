import pygame, sys, math, time, random
from os import path

# Constants
WIDTH = 640
HEIGHT = 480
FPS = 60

# Colors
BLACK = (0, 0, 0)

# Game paths
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.angle = 0
		self.original_image = ship_img
		self.image = pygame.transform.rotate(self.original_image, self.angle)
		self.rect = self.image.get_rect()
		
		# Start ship at the center
		self.rect.centerx = WIDTH / 2
		self.rect.bottom = HEIGHT / 2
		self.speedx = 0
		self.speedy = 0		
	
	def update(self):
		keystate = pygame.key.get_pressed()

		# if the left key is pressed, the ship will rotate to the left
		if keystate[pygame.K_LEFT]:
			self.angle += 3.5
		if keystate[pygame.K_RIGHT]:
			self.angle -= 3.5		
		if keystate[pygame.K_a]:
			self.angle -= 3.5
		if keystate[pygame.K_d]:
			self.angle += 3.5
		if keystate[pygame.K_SPACE]:
			ship.shoot()

		# Rotate
		self.image = pygame.transform.rotate(self.original_image, ship.angle)
		self.rect = self.image.get_rect()

		# Center ship
		self.rect.centerx = WIDTH / 2
		self.rect.centery = HEIGHT / 2

		# Set velocity of moviment back to zero
		self.speedx = 0
		self.speedy = 0
	
	def shoot(self):
		bullet = Bullet(self.angle + 90, self.rect.center, self.rect.top)
		all_sprites.add(bullet)
		bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
	def __init__(self, angle, center, bottom):
		pygame.sprite.Sprite.__init__(self)
		self.angle = angle
		self.original_image = bullet_img
		self.image = pygame.transform.rotate(self.original_image, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = center
		#self.rect.bottom = bottom
		self.speedx = 0
		self.speedy = 0

	def update(self):
		# Set velocity of moviment back to zero
		self.speedx = 6
		self.speedy = -6

		self.rect.x += (self.speedx * math.cos(math.radians(self.angle)))
		self.rect.y += (self.speedy * math.sin(math.radians(self.angle)))

		# Check if is still in the screen
		if self.rect.x > WIDTH or self.rect.x < 0 or self.rect.y > HEIGHT or self.rect.y < 0:
			self.kill()

				
'''
# Move at an angle
self.rect.x += (self.speedx * -math.cos(math.radians(self.angle)))
self.rect.y += (self.speedy * math.sin(math.radians(self.angle)))
		'''	

def moveship(pressed_Keys, ship_Angle):
	'if the left key is pressed, the ship will rotate to the left'
	if pressed_Keys[pygame.K_LEFT]:
		ship_Angle += 2.5

	if pressed_Keys[pygame.K_RIGHT]:
		ship_Angle -= 2.5
	return ship_Angle

def movebullet(cont, bullet_Angle, b_velocity_x, b_velocity_y):
	if cont == 1:
		b_velocity_x += (-math.cos(math.radians(bullet_Angle)))
		b_velocity_y += (math.sin(math.radians(bullet_Angle)))
	else:
		pass

	return b_velocity_x, b_velocity_y


def moveasteroid(cont, asteroidrect):
	if cont == 1:
		asteroidrect.x += 1
	else:
		pass


def create_Bullet(name, color, ship_Angle):
	'bullet'
	bullet = pygame.image.load('img/' + name)
	bullet.set_colorkey(color)
	bulletrect = bullet.get_rect()
	bulletrect.center = (320,240)
	bullet_Angle = ship_Angle
	b_velocity_x = 0
	b_velocity_y = 0

	return bullet, bulletrect, bullet_Angle, b_velocity_x, b_velocity_y

def create_Asteroid(name, color):
	'name will be the path of the image file'
	asteroid = pygame.image.load('img/' + name)

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


# Init pygame, set title and init clock
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()

# Load game graphics
background = pygame.image.load(path.join(img_folder, 'background.bmp')).convert()
background_rect = background.get_rect()

main_menu = pygame.image.load(path.join(img_folder, 'main_menu.bmp')).convert()
main_menu = main_menu.get_rect()

ship_img = pygame.image.load(path.join(img_folder, 'ship-0001.png')).convert_alpha()
asteroid_img = pygame.image.load(path.join(img_folder, 'asteroid-0001.png')).convert_alpha()
bullet_img = pygame.image.load(path.join(img_folder, 'bullet-0001.png')).convert_alpha()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

ship = Player()
all_sprites.add(ship)

'game state'
state = "main menu"

# Game loop
running = True
while running:
	# Process input
	for event in pygame.event.get():
		# check for closing window
		if event.type == pygame.QUIT:
			running = False
		
		# check pressed keys
		keystate = pygame.key.get_pressed()

		if keystate[pygame.K_SPACE]:
			ship.shoot()

	# Draw / render
	screen.fill(BLACK)
	screen.blit(background, background_rect)
	all_sprites.draw(screen)	

	#ship.rotated_image.blit(screen, ship.rotated_rect)

	# Update
	all_sprites.update()

	'''
	'ship'
	ship = pygame.image.load("img/Ship-0001.png")
	#ship.set_colorkey((135,254,255))
	shiprect = ship.get_rect()
	shiprect.center = (320,240)
	ship_Angle = 270
	#shiprect.x = 320
	#shiprect.y = 240

	'one asteroid'
	asteroid = pygame.image.load("img/asteroid-0001.png")
	asteroid.set_colorkey((135,254,255))
	asteroidrect = asteroid.get_rect()
	asteroidrect.center = (0,240)

	'special buttons'
	awesome_Button = pygame.image.load("img/awesome-button-0001.png")
	awesome_Button.set_colorkey((135,254,255))
	awesome_Button_rect = awesome_Button.get_rect()

	hot_Button = pygame.image.load("img/hot-button-0001.png")
	hot_Button.set_colorkey((135,254,255))
	hot_Button_rect = hot_Button.get_rect()
	
	force_Button = pygame.image.load("img/force-button-0001.png")
	force_Button.set_colorkey((135,254,255))
	force_Button_rect = force_Button.get_rect()
	
	bounce_Button = pygame.image.load("img/bounce-button-0001.png")
	bounce_Button.set_colorkey((135,254,255))
	bounce_Button_rect = bounce_Button.get_rect()
	
	'main menu'
	menu = pygame.image.load("img/main_menu.bmp")

	'bullets list'
	b = []

	'asteroids list'
	a = []
	cont = 1
	conti = 1

	'play and exit text'
	pygame.font.init()
	main_menu_text = "Press P key to play"
	exit_text = "Press Q to exit"
	point_Score = "Your SCORE is... : "
	score = 0

	'font for the specified text'
	text_font = pygame.font.Font("fonts/trench100free.ttf",30)
	text_color = (90,90,90)


	clock = pygame.time.Clock()

	if state == "playing":
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			if pressed_Keys[pygame.K_q]:
				sys.exit()

			if pressed_Keys[pygame.K_m]:
				state = "main menu"
				break

			'get all pressed keys'
			pressed_Keys = pygame.key.get_pressed()

			'send to function to move player'
			ship_Angle = moveship(pressed_Keys, ship_Angle)

			'every time the player press space, create a bullet if the array is not full'
			#shot = pygame.mixer.Sound("sons\shot.ogg")

			if pressed_Keys[pygame.K_SPACE]:
				# change here to increase the max amount of bullets in the screen
				if len(b) < 30:
					b.append(list(create_Bullet("bullet-0001.png",(135,254,255), ship_Angle)))					
					#shot.set_volume(0.1)
					#shot.play()
				else:
					pass

			'start creating asteroids from time to time'
			if (pygame.time.get_ticks() - tempo) >= 1000:
				seconds += 1
				tempo = pygame.time.get_ticks()
				cont = 1
	
			if seconds % 3 == 0 and cont == 1:
				a.append(list(create_Asteroid("asteroid-0001.png",(135,254,255))))
				cont = 0

			screen.blit(background, (0,0))

			ind = []

			'show bullets'
			for i in b:
				i[3], i[4] = movebullet(1,i[2],i[3],i[4])
				new_b_x = i[1].center[0] + (i[3]*1.5)
				new_b_y = i[1].center[1] + (i[4]*1.5)

				'conditional to see if the bullet escaped'
				if new_b_x > 640 or new_b_x < 0 or new_b_y > 480 or new_b_y < 0:
					b.pop(b.index(i))
					conti = 0
				else:
					center = (new_b_x, new_b_y)
					bullet_copy = i[0].copy()
					bullet_copy = pygame.transform.rotate(bullet_copy, i[2]+90)
					bullet_copy_rect = bullet_copy.get_rect()
					bullet_copy_rect.center = center
					screen.blit(bullet_copy,bullet_copy_rect)

			
			'move the asteroids'
			for j in a:
				j[3], j[4] = moveasteroid(1,j[2],j[3],j[4])
				new_a_x = j[1].center[0] + (j[3]*0.7)
				new_a_y = j[1].center[1] + (j[4]*0.7)

				'conditional to see if the asteroid escaped'
				if new_a_x > 640 or new_a_x < 0 or new_a_y > 480 or new_a_y < 0:
					a.pop(a.index(j))
					cont = 0
				else:
					center = (new_a_x, new_a_y)
					asteroid_copy = j[0].copy()
					asteroid_copy = pygame.transform.rotate(asteroid_copy, j[2]+90)
					asteroid_copy_rect = asteroid_copy.get_rect()
					asteroid_copy_rect.center = center
					screen.blit(asteroid_copy,asteroid_copy_rect)	


			for i in b:
				for j in a:
					'get real bullet rect'
					center = (new_b_x, new_b_y)
					bullet_copy = i[0].copy()
					bullet_copy = pygame.transform.rotate(bullet_copy, i[2]+90)
					bullet_copy_rect = bullet_copy.get_rect()
					bullet_copy_rect.center = center

					'get real asteroid rect'
					center = (new_a_x, new_a_y)
					asteroid_copy = j[0].copy()
					asteroid_copy = pygame.transform.rotate(asteroid_copy, j[2]+90)
					asteroid_copy_rect = asteroid_copy.get_rect()
					asteroid_copy_rect.center = center

					if bullet_copy_rect.colliderect(asteroid_copy_rect):
						b.pop(b.index(i))
						a.pop(a.index(j))
						score += 100

			#if bullet_copy_rect.colliderect(asteroid_copy_rect) and conti == 1:
			#	b.pop(b.index(i))
			#	a.pop(b.index(j))
			#	cont = 0
			

			'rotate the ship'
			center = shiprect.center
			ship_copy = ship.copy()
			ship_copy = pygame.transform.rotate(ship_copy,ship_Angle+90)
			ship_copy_rect = ship_copy.get_rect()
			ship_copy_rect.center = center

			

			screen.blit(ship_copy,ship_copy_rect)

			screen.blit(text_font.render("Press Q to exit", True, (255,255,255)),(10,0))
			screen.blit(text_font.render("Press M to menu", True, (255,255,255)),(10,30))
			screen.blit(text_font.render(point_Score + str(score), True, (255,255,255)),(10,430))
			
			pygame.display.flip()
			clock.tick(60)
			pygame.display.set_caption(str(clock.get_fps()))
	elif state == "main menu":
		'main menu music'
		#pygame.mixer.music.load("sons\main_menu.ogg")
		
		while True:
			pressed_Keys = pygame.key.get_pressed()

			'even in the main menu the player have to be able to leave the game'
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			if pressed_Keys[pygame.K_p]:
				state = "playing"
				#pygame.mixer.music.fadeout(100)
				break

			if pressed_Keys[pygame.K_q]:
				sys.exit()

			#if not pygame.mixer.music.get_busy():
				#pygame.mixer.music.set_volume(1.0)
				#pygame.mixer.music.play()

			screen.blit(menu, (-15,0))

			'showing options'
			screen.blit(text_font.render("Press P to play", True, text_color),(240,370))
			screen.blit(text_font.render("Press Q to exit", True, text_color),(240,400))
			pygame.display.flip()
			clock.tick(60)
			pygame.display.set_caption(str(clock.get_fps()))
			'''
	# *after* drawing everything, flip the display
	pygame.display.flip()

	# keep loop running at the right speed
	clock.tick(FPS)

# When the game stops running, quit
pygame.quit()
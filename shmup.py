# Pygame template
import pygame
import random
from os import path

# Constants
WIDTH = 480
HEIGHT = 640
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Paths
game_folder = path.dirname(__file__)
img_folder = path.join(path.dirname(__file__), 'img')

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.radius = 15
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    # Move it
    def update(self):
        # Set velocity of moviment back to zero
        self.speedx = 0

        # Get keys pressed
        keystate = pygame.key.get_pressed()

        # Update the velocity based on the keys pressed
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_d]:
            self.speedx = 8

        # Shoot endlessly
        # if keystate[pygame.K_SPACE]:
        #     self.shoot()                

        # Move
        self.rect.x += self.speedx

        # Check if player is out of bounds
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = random.choice(meteor_images)
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-3, 3)

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            # do rotation here YAY
            self.rot = (self.rot + self.rot_speed) % 360
            
            # Center the rotated image at the old center
            new_image = pygame.transform.rotate(self.image_original, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # Kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MEU JOGO")
clock = pygame.time.Clock()

# Load game graphics
background = pygame.image.load(path.join(img_folder, 'background(1).jpg')).convert()
background_rect = background.get_rect()

player_img = pygame.image.load(path.join(img_folder, 'ship-0001.png')).convert_alpha()
#meteor_img = pygame.image.load(path.join(img_folder, 'asteroid-0001.png')).convert_alpha()
bullet_img = pygame.image.load(path.join(img_folder, 'bullet-0001.png')).convert_alpha()

meteor_images = []
meteor_list = ['asteroid-0001.png', 'asteroid2-0001.png', 'asteroid3-0001.png']
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_folder, img)).convert_alpha())


# Group to hold all the sprites of the game
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


# Game loop
running = True
while running:
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: # Shoot with each keystroke
            if event.key == pygame.K_SPACE:
                player.shoot()
    
    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    # Update
    all_sprites.update()

    # Check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)

    if hits:
        running = False

    # Check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)

    # Repopulate the mobs that got shot
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # *after* drawing everything, flip the display
    pygame.display.flip()

    # keep loop running at the right speed
    clock.tick(FPS)

pygame.quit()
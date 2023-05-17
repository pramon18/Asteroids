# Pygame template
import pygame
import random

# Constants
WIDTH = 640
HEIGHT = 480
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


class Mob(pygame.sprite.Sprite):
    # Initially this mob will spawn above the screen 
    # and in a random horizontal location
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
    
    # If the mob goes out of the screen (bottom) move it above 
    # the screen again (basically a respawn)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy - random.randrange(1, 8)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MEU JOGO")
clock = pygame.time.Clock()

# Group to hold all the sprites of the game
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Update
    all_sprites.update()

    # *after* drawing everything, flip the display
    pygame.display.flip()

    # keep loop running at the right speed
    clock.tick(FPS)
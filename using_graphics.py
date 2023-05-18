# Pygame template
import pygame
import random
import os

# set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

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
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MEU JOGO")
clock = pygame.time.Clock()

# Carregar imagem do jogador
player_img = pygame.image.load(os.path.join(img_folder, 'ship-0001.png')).convert_alpha()

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

pygame.quit()
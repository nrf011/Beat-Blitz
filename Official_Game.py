import pygame
from random import choice
import sys
import time
from Object import *
from Still import *

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 1200, 720
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('assets/City.GIF').convert()
pygame.display.set_caption("Beat Blitz")
SCORE = 0

# Create Sprites
UP_ARROW = Arrow("assets/up_arrow.png", 250, 710)

DOWN_ARROW = Arrow("assets/down_arrow.png", 500, 710)

LEFT_ARROW = Arrow("assets/left_arrow.png", 750, 710)

RIGHT_ARROW = Arrow("assets/right_arrow.png", 1000, 710)



STILL_RIGHT = Still("assets/right_arrow.png", 1000, 50)

STILL_LEFT = Still("assets/left_arrow.png", 750, 50)

STILL_UP = Still("assets/up_arrow.png", 250, 50)

STILL_DOWN = Still("assets/down_arrow.png", 500, 50)


# Create a group to hold the sprites
all_still =  pygame.sprite.Group()
all_still.add(STILL_UP, STILL_DOWN, STILL_LEFT, STILL_RIGHT)

all_sprites = pygame.sprite.Group()
sprites = [UP_ARROW, DOWN_ARROW, RIGHT_ARROW, LEFT_ARROW]

# Game loop
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Spawn a random sprite
                random_arrow = choice(sprites)
                all_sprites.add(random_arrow)
            if event.key == pygame.K_a: 
                if UP_ARROW.rect.y > 10 and UP_ARROW.rect.y < 80:
                    SCORE += 1
                    UP_ARROW.kill()
                else:
                    UP_ARROW.kill()
            if event.key == pygame.K_s: 
                if DOWN_ARROW.rect.y > 10 and DOWN_ARROW.rect.y < 80:
                    SCORE += 1
                    DOWN_ARROW.kill()
                else:
                    DOWN_ARROW.kill()
            if event.key == pygame.K_d: 
                if LEFT_ARROW.rect.y > 10 and LEFT_ARROW.rect.y < 80:
                    SCORE += 1
                    LEFT_ARROW.kill()
                else:
                    LEFT_ARROW.kill()
            if event.key == pygame.K_f: 
                if RIGHT_ARROW.rect.y < 10 and RIGHT_ARROW.rect.y  < 80:
                    SCORE += 1
                    RIGHT_ARROW.kill()
                else:
                    RIGHT_ARROW.kill()

    # Update
    all_still.update()
    all_sprites.update()

    print(all_still)
    print(all_sprites)
    print(SCORE)

    # Draw
    screen.blit(background, (0, 0))
    all_still.draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)


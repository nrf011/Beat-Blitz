import pygame
import sys

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((255, 0, 0)) 
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)

    def update(self):
        self.rect.y -= 10  # Bullet Speed
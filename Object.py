import pygame
import sys


# Define the player sprite class
class Arrow(pygame.sprite.Sprite):
    def __init__(self, image, x_pos, y_pos):
        super().__init__()
        # Load an image with transparency
        original_image = pygame.image.load(image).convert_alpha()
        
        # Scale the image
        scale_factor = 0.15
        self.image = pygame.transform.scale(original_image, (int(original_image.get_width() * scale_factor),
                                                             int(original_image.get_height() * scale_factor)))
        
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
    

    def update(self):
        self.rect.y -= 5  # Adjust the value for the desired speed
        if self.rect.y < 5:
            self.kill()
            self.rect.y == 710

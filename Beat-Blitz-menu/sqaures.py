import pygame
import sys
import os
import atexit

pygame.init()
pygame.font.init()

score = 0
score_increment = 10

# Set up the window
screen = pygame.display.set_mode((750, 450))

# Set up the game clock
clock = pygame.time.Clock()

# Set up the player character
player = pygame.Rect(100, 200, 50, 50)

# Set up the obstacle
obstacle = pygame.Rect(200, 200, 50, 50)

# Get player's name
player_name = input("Enter your name (3 characters max): ").upper()[:3]

# Function to save the score
def save_score():
    with open("scoreboard.txt", "a") as f:
        f.write(f"{player_name}: {score}\n")

# Register the save_score function to be called when the program exits
atexit.register(save_score)

# Set up the game loop
while True:
    font = pygame.font.Font(None, 36)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -= 10
            elif event.key == pygame.K_RIGHT:
                player.x += 10

    # Update the game state
    if player.colliderect(obstacle):
        score += score_increment

    # Draw the game
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 255, 0), obstacle)

    # Draw the score to the screen
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

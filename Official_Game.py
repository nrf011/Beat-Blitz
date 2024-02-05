import pygame
from pygame import mixer
from random import choice
import sys
import time
from Object import *
from Still import *
from Main import *

def SONG1_EASY():
    # Initialize Pygame
    pygame.init()

    # Set up display
    screen_width, screen_height = 1200, 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    background = pygame.image.load('assets/game_city.png').convert()
    font = pygame.font.Font(None, 36)
    pygame.display.set_caption("Beat Blitz")
    icon = pygame.image.load("assets/B.png")
    pygame.display.set_icon(icon)
    SCORE = 0

    # MUSIC
    mixer.music.load("assets/ybmf.mp3")
    mixer.music.play(1)
    volume = mixer.music.set_volume(1.0)

    # DEFINE SAVE
    def save_score(player_name, score, difficulty):
        filename = f"scoreboard_{difficulty}.txt"
        with open(filename, "a") as f:
            f.write(f"{player_name}: {score}\n")

    # Create Sprites
    UP_ARROW = Arrow("assets/up_arrow.png", 250, 710)

    DOWN_ARROW = Arrow("assets/down_arrow.png", 500, 710)

    LEFT_ARROW = Arrow("assets/left_arrow.png", 750, 710)

    RIGHT_ARROW = Arrow("assets/right_arrow.png", 1000, 710)



    STILL_RIGHT = Still("assets/right_arrow.png", 1000, 50)

    STILL_LEFT = Still("assets/left_arrow.png", 750, 50)

    STILL_UP = Still("assets/up_arrow.png", 250, 50)

    STILL_DOWN = Still("assets/down_arrow.png", 500, 50)


    # GREEN AND GOLD DOWN ARROW
    grn_d = pygame.image.load('assets/green_down_arrow.png').convert_alpha()
    grn_d = pygame.transform.scale(grn_d, (int(grn_d.get_width() * 0.15),
                                    int(grn_d.get_height() * 0.15)))

    gld_d = pygame.image.load('assets/gold_down_arrow.png').convert_alpha()
    gld_d = pygame.transform.scale(gld_d, (int(gld_d.get_width() * 0.15),
                                    int(gld_d.get_height() * 0.15)))

    blu_d = pygame.image.load('assets/down_arrow.png').convert_alpha()
    blu_d = pygame.transform.scale(blu_d, (int(blu_d.get_width() * 0.15),
                                    int(blu_d.get_height() * 0.15)))





    # GREEN & GOLD UP ARROWS
    grn_u = pygame.image.load('assets/green_up_arrow.png').convert_alpha()
    grn_u = pygame.transform.scale(grn_u, (int(grn_u.get_width() * 0.15),
                                    int(grn_u.get_height() * 0.15)))

    gld_u = pygame.image.load('assets/gold_up_arrow.png').convert_alpha()
    gld_u = pygame.transform.scale(gld_u, (int(gld_u.get_width() * 0.15),
                                    int(gld_u.get_height() * 0.15)))

    blu_u = pygame.image.load('assets/up_arrow.png').convert_alpha()
    blu_u = pygame.transform.scale(blu_u, (int(blu_u.get_width() * 0.15),
                                    int(blu_u.get_height() * 0.15)))



    # GREEN AND GOLD RIGHT ARROW
    grn_r = pygame.image.load('assets/green_right_arrow.png').convert_alpha()
    grn_r = pygame.transform.scale(grn_r, (int(grn_r.get_width() * 0.15),
                                    int(grn_r.get_height() * 0.15)))

    gld_r = pygame.image.load('assets/gold_right_arrow.png').convert_alpha()
    gld_r = pygame.transform.scale(gld_r, (int(gld_r.get_width() * 0.15),
                                    int(gld_r.get_height() * 0.15)))

    blu_r = pygame.image.load('assets/right_arrow.png').convert_alpha()
    blu_r = pygame.transform.scale(blu_r, (int(blu_r.get_width() * 0.15),
                                    int(blu_r.get_height() * 0.15)))


    # GREEN AND GOLD LEFT ARROW
    grn_l = pygame.image.load('assets/green_left_arrow.png').convert_alpha()
    grn_l = pygame.transform.scale(grn_l, (int(grn_l.get_width() * 0.15),
                                    int(grn_l.get_height() * 0.15)))

    gld_l = pygame.image.load('assets/gold_left_arrow.png').convert_alpha()
    gld_l = pygame.transform.scale(gld_l, (int(gld_l.get_width() * 0.15),
                                    int(gld_l.get_height() * 0.15)))

    blu_l = pygame.image.load('assets/left_arrow.png').convert_alpha()
    blu_l = pygame.transform.scale(blu_l, (int(blu_l.get_width() * 0.15),
                                    int(blu_l.get_height() * 0.15)))

    # Create a group to hold the sprites
    all_still =  pygame.sprite.Group()
    all_still.add(STILL_UP, STILL_DOWN, STILL_LEFT, STILL_RIGHT)

    all_sprites = pygame.sprite.Group()
    sprites = [UP_ARROW, DOWN_ARROW, RIGHT_ARROW, LEFT_ARROW]

    # Game loop
    clock = pygame.time.Clock()
    time_last_color_change = 0
    time_last_arrow_spawn = pygame.time.get_ticks()


    while True:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_SPACE:
                    # Spawn a random sprite
                    #random_arrow = choice(sprites)
                    #all_sprites.add(random_arrow)
                
                # UP ARROW
                if event.key == pygame.K_a: 
                    if UP_ARROW.rect.y >  20 and UP_ARROW.rect.y < 45 :
                        SCORE += 100
                        STILL_UP.image = gld_u
                        UP_ARROW.rect.y = 710
                        UP_ARROW.kill()
                    elif UP_ARROW.rect.y > 10 and UP_ARROW.rect.y < 65 :
                        SCORE += 50
                        STILL_UP.image = grn_u
                        UP_ARROW.rect.y = 710
                        UP_ARROW.kill()
                    else:
                        UP_ARROW.rect.y = 710
                        UP_ARROW.kill()
                        if SCORE > 0:
                            SCORE -= 25
                        
                

                # DOWN ARROW
                if event.key == pygame.K_s: 
                    if DOWN_ARROW.rect.y > 20 and DOWN_ARROW.rect.y < 45 :
                        SCORE += 100
                        DOWN_ARROW.rect.y = 710
                        DOWN_ARROW.kill()
                        STILL_DOWN.image = gld_d
                    
                    elif DOWN_ARROW.rect.y > 10 and DOWN_ARROW.rect.y <65 :
                        SCORE += 50
                        DOWN_ARROW.rect.y = 710
                        DOWN_ARROW.kill()
                        STILL_DOWN.image = grn_d
        
                    else:
                        DOWN_ARROW.rect.y = 710
                        DOWN_ARROW.kill()
                        if SCORE > 0:
                            SCORE -= 25
                        
                    
                # LEFT ARROW
                if event.key == pygame.K_d: 
                    if LEFT_ARROW.rect.y > 20 and LEFT_ARROW.rect.y < 45 :
                        SCORE += 100
                        STILL_LEFT.image = gld_l
                        LEFT_ARROW.rect.y = 710
                        LEFT_ARROW.kill()
                    elif LEFT_ARROW.rect.y > 10 and LEFT_ARROW.rect.y < 65 :
                        SCORE += 50
                        STILL_LEFT.image = grn_l
                        LEFT_ARROW.rect.y = 710
                        LEFT_ARROW.kill()
                    else:
                        LEFT_ARROW.rect.y = 710
                        LEFT_ARROW.kill()
                        if SCORE > 0:
                            SCORE -= 25
                        
               
                # RIGHT ARROW
                if event.key == pygame.K_f: 
                    if RIGHT_ARROW.rect.y > 20 and RIGHT_ARROW.rect.y < 45 :
                        SCORE += 100
                        STILL_RIGHT.image = gld_r
                        RIGHT_ARROW.rect.y = 710
                        RIGHT_ARROW.kill()
                    elif RIGHT_ARROW.rect.y > 10 and RIGHT_ARROW.rect.y < 65 :
                        SCORE += 50
                        STILL_RIGHT.image = grn_r
                        RIGHT_ARROW.rect.y = 710
                        RIGHT_ARROW.kill()
                    else:
                        RIGHT_ARROW.rect.y = 710
                        RIGHT_ARROW.kill()
                        if SCORE > 0:
                            SCORE -= 25
                        
        
        if current_time - time_last_arrow_spawn >= 1000: # ARROW SPAWN RATE
            random_arrow = choice(sprites)
            all_sprites.add(random_arrow)
            time_last_arrow_spawn = current_time
        
        # Update
        all_still.update()
        all_sprites.update()

        for arrow in all_sprites:
            if arrow.rect.y <= 10:
                arrow.rect.y = 710
                if SCORE > 0:
                            SCORE -= 25
                        
        
        if not mixer.music.get_busy():
            pygame.quit()
            sys.exit()

        print(all_still)
        print(all_sprites)
        print(SCORE)

        current_time = pygame.time.get_ticks()
        if current_time - time_last_color_change >= 500:  # milliseconds (1 second)
            STILL_UP.image = blu_u
            STILL_DOWN.image = blu_d
            STILL_LEFT.image = blu_l
            STILL_RIGHT.image = blu_r
            time_last_color_change = current_time
        
        # Draw
        screen.blit(background, (0, 0))
        all_still.draw(screen)
        all_sprites.draw(screen)

        # Render and display the score
        score_text = font.render(f"Score: {SCORE}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

         # Save the score before exiting
        #save_score(player_name, score, difficulty)
        #pygame.quit()
        #sys.exit()


        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

SONG1_EASY()


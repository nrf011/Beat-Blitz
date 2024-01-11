#song 1 file
import pygame, sys
from pygame import mixer
from button import Button
from Main import *

pygame.init()

SCREEN = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Menu")

#Background
BG = pygame.image.load("assets/City.GIF")

#Background Music
mixer.music.load("assets/Beat Blitz.mp3")
mixer.music.play(-1)
volume = mixer.music.set_volume(1.0)

#Sounds
click = mixer.Sound("assets/click.wav")
hover = mixer.Sound("assets/hover.wav")

pygame.init()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def SONG1_EASY():
    pygame.display.set_caption("Play")
    while True:
        
        SONG1_EASY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(60).render("NAME AND CHARCTER", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(SONG1_EASY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        # Male player button
        MALE_BUTTON=Button(image=pygame.image.load("assets/male.player.jpg"),pos=(300,400), text_input="Male",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        MALE_BUTTON.changeColor(SONG1_EASY_MOUSE_POS)
        MALE_BUTTON.update(SCREEN)

        # Female player button
        EASY1_BUTTON=Button(image=pygame.image.load("assets/female.player.jpg"),pos=(900,400), text_input="Female",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EASY1_BUTTON.changeColor(SONG1_EASY_MOUSE_POS)
        EASY1_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(SONG1_EASY_MOUSE_POS):
                    SONG1()

        pygame.display.update()


def song1_med():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def song1_exp():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

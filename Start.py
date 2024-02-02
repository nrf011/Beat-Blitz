import pygame, sys
from pygame import mixer
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Menu")
icon = pygame.image.load("assets/B.png")
pygame.display.set_icon(icon)

#Background
BG = pygame.image.load("assets/City.GIF")

#Background Music
mixer.music.load("assets/Beat Blitz.mp3")
mixer.music.play(-1)
volume = mixer.music.set_volume(1.0)

#Sounds
click = mixer.Sound("assets/click.wav")
hover = mixer.Sound("assets/hover.wav")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
        
        exec(open("GAME.py").read())
    

        pygame.display.update()
    


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Beat Blitz", True, "#f000fb")
        MENU_RECT = MENU_TEXT.get_rect(center=(600, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(600, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(600, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                click.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click.play()
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
import pygame, sys
from pygame import mixer
from button import Button

SCREEN = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Options")

BG = pygame.image.load("City.GIF")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

#Sounds
#click = mixer.Sound("click.wav")
#hover = mixer.Sound("hover.wav")

def options():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Beat Blitz", True, "#f000fb")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #click.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
               # if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #click.play()
                   # play()
               # if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #click.play()
                   # options()
               # if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #click.play()
                   # pygame.quit()
                    sys.exit()

        pygame.display.update()

options()
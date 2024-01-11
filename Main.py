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
    pygame.display.set_caption("Play")
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
                click.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    click.play()
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0,0))

        MUSIC_TEXT = get_font(45).render("MUSIC", True, "White")
        MUSIC_RECT = MUSIC_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(MUSIC_TEXT, MUSIC_RECT)

        EFFECTS_TEXT = get_font(45).render("EFFECTS", True, "White")
        EFFECTS_RECT = EFFECTS_TEXT.get_rect(center=(600, 350))
        SCREEN.blit(EFFECTS_TEXT, EFFECTS_RECT)

        #MUSIC SETTINGS
        MUSIC_ON = Button(image=None, pos=(300, 200), text_input="ON", font=get_font(50), base_color="White", hovering_color="Green")

        MUSIC_ON.changeColor(OPTIONS_MOUSE_POS)
        MUSIC_ON.update(SCREEN)

        MUSIC_OFF = Button(image=None, pos=(900, 200), text_input="OFF", font=get_font(50), base_color="White", hovering_color="Green")

        MUSIC_OFF.changeColor(OPTIONS_MOUSE_POS)
        MUSIC_OFF.update(SCREEN)

        #EFFECTS SETTINGS
        EFFECTS_ON = Button(image=None, pos=(300, 450), text_input="ON", font=get_font(50), base_color="White", hovering_color="Green")

        EFFECTS_ON.changeColor(OPTIONS_MOUSE_POS)
        EFFECTS_ON.update(SCREEN)

        EFFECTS_OFF = Button(image=None, pos=(900, 450), text_input="OFF", font=get_font(50), base_color="White", hovering_color="Green")

        EFFECTS_OFF.changeColor(OPTIONS_MOUSE_POS)
        EFFECTS_OFF.update(SCREEN)


        #Back Button
        OPTIONS_BACK = Button(image=None, pos=(600, 650), 
                            text_input="BACK", font=get_font(30), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                click.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    click.play()
                    main_menu()

                if MUSIC_ON.checkForInput(OPTIONS_MOUSE_POS):
                    click.play()
                    mixer.music.set_volume(1.0)
                    options()

                if MUSIC_OFF.checkForInput(OPTIONS_MOUSE_POS):
                    click.play()
                    mixer.music.set_volume(0.0)
                    options()

                if EFFECTS_ON.checkForInput(OPTIONS_MOUSE_POS):
                    click.play()
                    click.set_volume(1.0)
                    options()

                if EFFECTS_OFF.checkForInput(OPTIONS_MOUSE_POS):
                    click.play()
                    click.set_volume(0.0)
                    options()


        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Beat Blitz", True, "#f000fb")
        MENU_RECT = MENU_TEXT.get_rect(center=(600, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(600, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(600, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(600, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
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
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click.play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
 

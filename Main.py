import pygame, sys
from pygame import mixer
from button import Button

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

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play(): # the play screen
    pygame.display.set_caption("Play")
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(100).render("Song select", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        
        #SONG SELECTION OPTIONS

        #SONG 1
        SONG1_BUTTON=Button(image=pygame.image.load("assets/Play Rect.png"),pos=(200,300), text_input="Song 1",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        SONG1_BUTTON.changeColor(PLAY_MOUSE_POS)
        SONG1_BUTTON.update(SCREEN)




        #SONG 2
        SONG2_BUTTON=Button(image=pygame.image.load("assets/Play Rect.png"),pos=(600,350), text_input="Song 2",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        SONG2_BUTTON.changeColor(PLAY_MOUSE_POS)
        SONG2_BUTTON.update(SCREEN)

        #SONG 3
        SONG3_BUTTON=Button(image=pygame.image.load("assets/Play Rect.png"),pos=(1000,400), text_input="Song 3",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        SONG3_BUTTON.changeColor(PLAY_MOUSE_POS)
        SONG3_BUTTON.update(SCREEN)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                click.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SONG1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    click.play()
                    SONG1()
                if SONG2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    click.play()
                    SONG2()
                if SONG3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    click.play()
                    SONG3()
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    click.play()
                    main_menu()

        pygame.display.update()

def options(): #the options screen
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

def main_menu(): #the main menu
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

def SONG1(): #song one menu
    while True:
        SONG1_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(50).render("Select difficulty", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        SONG1_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        SONG1_BACK.changeColor(SONG1_MOUSE_POS)
        SONG1_BACK.update(SCREEN)

        # EASY difficulty selet
        EASY1_BUTTON=Button(image=pygame.image.load("assets/Play Rect.png"),pos=(600,200), text_input="EASY",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EASY1_BUTTON.changeColor(SONG1_MOUSE_POS)
        EASY1_BUTTON.update(SCREEN)

        # MEDIUM difficulty select
        MED1_BUTTON=Button(image=pygame.image.load("assets/Play Rect.png"),pos=(600,350), text_input="MEDIUM",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        MED1_BUTTON.changeColor(SONG1_MOUSE_POS)
        MED1_BUTTON.update(SCREEN)

        # EXPERT difficulty select
        EXP1_BUTTON=Button(image=pygame.image.load("assets/Play Rect.png"),pos=(600,500), text_input="EXPERT",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EXP1_BUTTON.changeColor(SONG1_MOUSE_POS)
        EXP1_BUTTON.update(SCREEN)

        #leaderbaord 1
        LEADERBOARD1_BUTTON=Button(image=pygame.image.load("assets/Options Rect.png"),pos=(600,650), text_input="Leaderbaord",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        LEADERBOARD1_BUTTON.changeColor(SONG1_MOUSE_POS)
        LEADERBOARD1_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY1_BUTTON.checkForInput(SONG1_MOUSE_POS):
                    SONG1_EASY()

                if MED1_BUTTON.checkForInput(SONG1_MOUSE_POS):
                    SONG1_MED()

                if EXP1_BUTTON.checkForInput(SONG1_MOUSE_POS):
                    SONG1_EXP()

                if SONG1_BACK.checkForInput(SONG1_MOUSE_POS):
                    play()


        pygame.display.update()
        
def SONG2(): #song 2 menu
    while True:
        SONG2_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(50).render("Select difficulty", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        SONG2_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        SONG2_BACK.changeColor(SONG2_MOUSE_POS)
        SONG2_BACK.update(SCREEN)

        # EASY difficulty selet
        EASY2_BUTTON=Button(image=pygame.image.load("assets/Play Rect.png"),pos=(600,200), text_input="EASY",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EASY2_BUTTON.changeColor(SONG2_MOUSE_POS)
        EASY2_BUTTON.update(SCREEN)

        # MEDIUM difficulty select
        MED2_BUTTON=Button(image=pygame.image.load("assets/Play Rect.png"),pos=(600,350), text_input="MEDIUM",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        MED2_BUTTON.changeColor(SONG2_MOUSE_POS)
        MED2_BUTTON.update(SCREEN)

        # EXPERT difficulty select
        EXP2_BUTTON=Button(image=pygame.image.load("assets/Play Rect.png"),pos=(600,500), text_input="EXPERT",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EXP2_BUTTON.changeColor(SONG2_MOUSE_POS)
        EXP2_BUTTON.update(SCREEN)

        #leaderbaord 
        LEADERBOARD2_BUTTON=Button(image=pygame.image.load("assets/Options Rect.png"),pos=(600,650), text_input="Leaderbaord",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        LEADERBOARD2_BUTTON.changeColor(SONG2_MOUSE_POS)
        LEADERBOARD2_BUTTON.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY2_BUTTON.checkForInput(SONG2_MOUSE_POS):
                    SONG2_EASY()

                if MED2_BUTTON.checkForInput(SONG2_MOUSE_POS):
                    SONG2_MED()

                if EXP2_BUTTON.checkForInput(SONG2_MOUSE_POS):
                    SONG2_EXP()

                if SONG2_BACK.checkForInput(SONG2_MOUSE_POS):
                    play()

        pygame.display.update()

def SONG3(): #song 3 menu
    while True:
        SONG3_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(50).render("Select difficulty", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        SONG3_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        SONG3_BACK.changeColor(SONG3_MOUSE_POS)
        SONG3_BACK.update(SCREEN)

        # EASY difficulty selet
        EASY3_BUTTON=Button(image=pygame.image.load("assets/Play Rect.png"),pos=(600,200), text_input="EASY",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EASY3_BUTTON.changeColor(SONG3_MOUSE_POS)
        EASY3_BUTTON.update(SCREEN)

        # MEDIUM difficulty select
        MED3_BUTTON=Button(image=pygame.image.load("assets/Play Rect.png"),pos=(600,350), text_input="MEDIUM",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        MED3_BUTTON.changeColor(SONG3_MOUSE_POS)
        MED3_BUTTON.update(SCREEN)

        # EXPERT difficulty select
        EXP3_BUTTON=Button(image=pygame.image.load("assets/Play Rect.png"),pos=(600,500), text_input="EXPERT",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EXP3_BUTTON.changeColor(SONG3_MOUSE_POS)
        EXP3_BUTTON.update(SCREEN)

        #leaderbaord 
        LEADERBOARD3_BUTTON=Button(image=pygame.image.load("assets/Options Rect.png"),pos=(600,650), text_input="Leaderbaord",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        LEADERBOARD3_BUTTON.changeColor(SONG3_MOUSE_POS)
        LEADERBOARD3_BUTTON.update(SCREEN)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY3_BUTTON.checkForInput(SONG3_MOUSE_POS):
                    SONG3_EASY()

                if MED3_BUTTON.checkForInput(SONG3_MOUSE_POS):
                    SONG3_MED()

                if EXP3_BUTTON.checkForInput(SONG3_MOUSE_POS):
                    SONG3_EXP()

                if SONG3_BACK.checkForInput(SONG3_MOUSE_POS):
                    play()

        pygame.display.update()

def LEADERBOARD(): #leaderbaord menu
    while True:
        LEADERBOARD_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the lb screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(LEADERBOARD_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(LEADERBOARD_MOUSE_POS):
                    play()

        pygame.display.update()

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

def SONG1_MED():
     while True:
        
        SONG1_MED_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(60).render("NAME AND CHARCTER", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        SONG1_MED_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        SONG1_MED_BACK.changeColor(SONG1_MED_MOUSE_POS)
        SONG1_MED_BACK.update(SCREEN)

        # Male player button
        MALE_BUTTON=Button(image=pygame.image.load("assets/male.player.jpg"),pos=(300,400), text_input="Male",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        MALE_BUTTON.changeColor(SONG1_MED_MOUSE_POS)
        MALE_BUTTON.update(SCREEN)

        # Female player button
        EASY1_BUTTON=Button(image=pygame.image.load("assets/female.player.jpg"),pos=(900,400), text_input="Female",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EASY1_BUTTON.changeColor(SONG1_MED_MOUSE_POS)
        EASY1_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SONG1_MED_BACK.checkForInput(SONG1_MED_MOUSE_POS):
                    SONG1()

        pygame.display.update()

def SONG1_EXP():
     while True:
        
        SONG1_EXP_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(60).render("NAME AND CHARCTER", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        SONG1_EXP_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        SONG1_EXP_BACK.changeColor(SONG1_EXP_MOUSE_POS)
        SONG1_EXP_BACK.update(SCREEN)

        # Male player button
        MALE_BUTTON=Button(image=pygame.image.load("assets/male.player.jpg"),pos=(300,400), text_input="Male",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        MALE_BUTTON.changeColor(SONG1_EXP_MOUSE_POS)
        MALE_BUTTON.update(SCREEN)

        # Female player button
        EASY1_BUTTON=Button(image=pygame.image.load("assets/female.player.jpg"),pos=(900,400), text_input="Female",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EASY1_BUTTON.changeColor(SONG1_EXP_MOUSE_POS)
        EASY1_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SONG1_EXP_BACK.checkForInput(SONG1_EXP_MOUSE_POS):
                    SONG1()

        pygame.display.update()

def SONG2_EASY():
    pygame.display.set_caption("Play")
    while True:
        
        SONG2_EASY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(60).render("NAME AND CHARCTER", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        SONG2_EASY_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        SONG2_EASY_BACK.changeColor(SONG2_EASY_MOUSE_POS)
        SONG2_EASY_BACK.update(SCREEN)

        # Male player button
        MALE_BUTTON=Button(image=pygame.image.load("assets/male.player.jpg"),pos=(300,400), text_input="Male",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        MALE_BUTTON.changeColor(SONG2_EASY_MOUSE_POS)
        MALE_BUTTON.update(SCREEN)

        # Female player button
        EASY1_BUTTON=Button(image=pygame.image.load("assets/female.player.jpg"),pos=(900,400), text_input="Female",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EASY1_BUTTON.changeColor(SONG2_EASY_MOUSE_POS)
        EASY1_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SONG2_EASY_BACK.checkForInput(SONG2_EASY_MOUSE_POS):
                    SONG2()

        pygame.display.update()

def SONG2_MED():
    pygame.display.set_caption("Play")
    while True:
        
        SONG2_MED_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(60).render("NAME AND CHARCTER", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        SONG2_MED_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        SONG2_MED_BACK.changeColor(SONG2_MED_MOUSE_POS)
        SONG2_MED_BACK.update(SCREEN)

        # Male player button
        MALE_BUTTON=Button(image=pygame.image.load("assets/male.player.jpg"),pos=(300,400), text_input="Male",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        MALE_BUTTON.changeColor(SONG2_MED_MOUSE_POS)
        MALE_BUTTON.update(SCREEN)

        # Female player button
        EASY1_BUTTON=Button(image=pygame.image.load("assets/female.player.jpg"),pos=(900,400), text_input="Female",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EASY1_BUTTON.changeColor(SONG2_MED_MOUSE_POS)
        EASY1_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SONG2_MED_BACK.checkForInput(SONG2_MED_MOUSE_POS):
                    SONG2()

        pygame.display.update()

def SONG2_EXP():
    pygame.display.set_caption("Play")
    while True:
        
        SONG2_EXP_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(60).render("NAME AND CHARCTER", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        SONG2_EXP_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")
        
        SONG2_EXP_BACK.changeColor(SONG2_EXP_MOUSE_POS)
        SONG2_EXP_BACK.update(SCREEN)

        # Male player button
        MALE_BUTTON=Button(image=pygame.image.load("assets/male.player.jpg"),pos=(300,400), text_input="Male",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        MALE_BUTTON.changeColor(SONG2_EXP_MOUSE_POS)
        MALE_BUTTON.update(SCREEN)

        # Female player button
        EASY1_BUTTON=Button(image=pygame.image.load("assets/female.player.jpg"),pos=(900,400), text_input="Female",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EASY1_BUTTON.changeColor(SONG2_EXP_MOUSE_POS)
        EASY1_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  SONG2_EXP_BACK.checkForInput(SONG2_EXP_MOUSE_POS):
                    SONG2()

        pygame.display.update()

def SONG3_EASY():
    while True:
        
        SONG3_EASY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(60).render("NAME AND CHARCTER", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        SONG3_EASY_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        SONG3_EASY_BACK.changeColor(SONG3_EASY_MOUSE_POS)
        SONG3_EASY_BACK.update(SCREEN)

        # Male player button
        MALE_BUTTON=Button(image=pygame.image.load("assets/male.player.jpg"),pos=(300,400), text_input="Male",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        MALE_BUTTON.changeColor(SONG3_EASY_MOUSE_POS)
        MALE_BUTTON.update(SCREEN)

        # Female player button
        EASY1_BUTTON=Button(image=pygame.image.load("assets/female.player.jpg"),pos=(900,400), text_input="Female",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EASY1_BUTTON.changeColor(SONG3_EASY_MOUSE_POS)
        EASY1_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SONG3_EASY_BACK.checkForInput(SONG3_EASY_MOUSE_POS):
                    SONG3()

        pygame.display.update()

def SONG3_MED():
    while True:
        
        SONG3_MED_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(60).render("NAME AND CHARCTER", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        SONG3_MED_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        SONG3_MED_BACK.changeColor(SONG3_MED_MOUSE_POS)
        SONG3_MED_BACK.update(SCREEN)

        # Male player button
        MALE_BUTTON=Button(image=pygame.image.load("assets/male.player.jpg"),pos=(300,400), text_input="Male",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        MALE_BUTTON.changeColor(SONG3_MED_MOUSE_POS)
        MALE_BUTTON.update(SCREEN)

        # Female player button
        EASY1_BUTTON=Button(image=pygame.image.load("assets/female.player.jpg"),pos=(900,400), text_input="Female",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EASY1_BUTTON.changeColor(SONG3_MED_MOUSE_POS)
        EASY1_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SONG3_MED_BACK.checkForInput(SONG3_MED_MOUSE_POS):
                    SONG3()

        pygame.display.update()

def SONG3_EXP():
    while True:
        
        SONG3_EXP_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(60).render("NAME AND CHARCTER", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        SONG3_EXP_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        SONG3_EXP_BACK.changeColor(SONG3_EXP_MOUSE_POS)
        SONG3_EXP_BACK.update(SCREEN)

        # Male player button
        MALE_BUTTON=Button(image=pygame.image.load("assets/male.player.jpg"),pos=(300,400), text_input="Male",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        MALE_BUTTON.changeColor(SONG3_EXP_MOUSE_POS)
        MALE_BUTTON.update(SCREEN)

        # Female player button
        EASY1_BUTTON=Button(image=pygame.image.load("assets/female.player.jpg"),pos=(900,400), text_input="Female",font=get_font(50),base_color="#d7fcd4",hovering_color="white")
        EASY1_BUTTON.changeColor(SONG3_EXP_MOUSE_POS)
        EASY1_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SONG3_EXP_BACK.checkForInput(SONG3_EXP_MOUSE_POS):
                    SONG3()

        pygame.display.update()



main_menu()
#song1_Mode()
 

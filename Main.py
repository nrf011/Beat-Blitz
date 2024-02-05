import pygame, sys
from pygame import mixer
from button import Button
import threading
import random
import atexit
from Object import *
from Still import *
from random import choice

pygame.init()

SCREEN = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Menu")

#Background
BG = pygame.image.load("assets/retro.GIF")

#Background Music
mixer.music.load("assets/Beat Blitz.mp3")
mixer.music.play(-1)
volume = mixer.music.set_volume(1.0)

#Sounds
click = mixer.Sound("assets/click.wav")
hover = mixer.Sound("assets/hover.wav")

# loading image
loading_image = pygame.image.load("assets/loading2.png")
loading_image_rect = loading_image.get_rect(center=(640, 360))
loading_finished = False
loading_progress = 0
rotation_speed = 1  # Adjust this value for slower or faster rotation

#Clock
CLOCK = pygame.time.Clock()

#work
WORK = 100000000


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

# finished text
finished_font = get_font(30)
finished_text = finished_font.render("Loading your next track...", True, "white")
finished_rect = finished_text.get_rect(center=(640, 450))  # Adjusted position

def play(): # the play screen
    pygame.display.set_caption("Play")
    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(100).render("Song select", True, "#6A1B9A")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY2_TEXT = get_font(100).render("Song select", True, "#BA68C8")
        PLAY2_RECT = PLAY2_TEXT.get_rect(center=(594, 100))
        SCREEN.blit(PLAY2_TEXT, PLAY2_RECT)

        PLAY_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        
        #SONG SELECTION OPTIONS

        #SONG 1
        EASY_BUTTON = Button(image=None, pos=(200, 300),
                           text_input="EASY", font=get_font(50), base_color="#6A1B9A", hovering_color="#6A1B9A")
        EASY_BUTTON.changeColor(PLAY_MOUSE_POS)
        EASY_BUTTON.update(SCREEN)
        
        EASY2_BUTTON = Button(image=None, pos=(190, 300),
                           text_input="EASY", font=get_font(50), base_color="#BA68C8", hovering_color="#FF44CC")
        EASY2_BUTTON.changeColor(PLAY_MOUSE_POS)
        EASY2_BUTTON.update(SCREEN)





        #SONG 2
        MED_BUTTON = Button(image=None, pos=(600, 300),
                           text_input="MEDIUM", font=get_font(50), base_color="#6A1B9A", hovering_color="#6A1B9A")
        MED_BUTTON.changeColor(PLAY_MOUSE_POS)
        MED_BUTTON.update(SCREEN)
        
        MED2_BUTTON = Button(image=None, pos=(590, 300),
                           text_input="MEDIUM", font=get_font(50), base_color="#BA68C8", hovering_color="#FF44CC")
        MED2_BUTTON.changeColor(PLAY_MOUSE_POS)
        MED2_BUTTON.update(SCREEN)


        #SONG 3
        EXP_BUTTON = Button(image=None, pos=(1000, 300),
                           text_input="EXPERT", font=get_font(50), base_color="#6A1B9A", hovering_color="#6A1B9A")
        EXP_BUTTON.changeColor(PLAY_MOUSE_POS)
        EXP_BUTTON.update(SCREEN)
        
        EXP2_BUTTON = Button(image=None, pos=(990, 300),
                           text_input="EXPERT", font=get_font(50), base_color="#BA68C8", hovering_color="#FF44CC")
        EXP2_BUTTON.changeColor(PLAY_MOUSE_POS)
        EXP2_BUTTON.update(SCREEN)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                click.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    click.play()
                    loadingscreen()
                    SONG1_EASY()
                if MED_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    click.play()
                    loadingscreen()
                    SONG1_MED()
                if EXP_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    click.play()
                    loadingscreen()
                    SONG1_EXP()
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    click.play()
                    loadingscreen()
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

        MENU_BEAT_TEXT = get_font(100).render("Beat", True, "#6A1B9A")
        MENU_BEAT_RECT = MENU_BEAT_TEXT.get_rect(center=(630, 65))

        MENU_BLITZ_TEXT=get_font(100).render("Blitz",True, ("#6A1B9A"))
        MENU_BLITZ_RECT= MENU_BLITZ_TEXT.get_rect(center=(630,155))

        MENU2_BEAT_TEXT = get_font(100).render("Beat", True, "#BA68C8")
        MENU2_BEAT_RECT = MENU2_BEAT_TEXT.get_rect(center=(630, 55))

        MENU2_BLITZ_TEXT=get_font(100).render("Blitz",True, ("#BA68C8"))
        MENU2_BLITZ_RECT= MENU2_BLITZ_TEXT.get_rect(center=(630,145))


        PLAY_BUTTON = Button(image=None, pos=(600, 325),
                           text_input="PLAY", font=get_font(75), base_color="#BA68C8", hovering_color="#FF44CC")
        PLAY_BUTTON.changeColor(MENU_MOUSE_POS)
        PLAY_BUTTON.update(SCREEN)

        PLAY2_BUTTON = Button(image=None, pos=(600, 315),
                           text_input="PLAY", font=get_font(75), base_color="#6A1B9A", hovering_color="#6A1B9A")
        PLAY2_BUTTON.changeColor(MENU_MOUSE_POS)
        PLAY2_BUTTON.update(SCREEN)
        
        OPTIONS_BUTTON = Button(image=None, pos=(600, 440),
                           text_input="OPTIONS", font=get_font(75), base_color="#BA68C8", hovering_color="#FF44CC")
        OPTIONS_BUTTON.changeColor(MENU_MOUSE_POS)
        OPTIONS_BUTTON.update(SCREEN)

        OPTIONS2_BUTTON = Button(image=None, pos=(600, 430),
                           text_input="OPTIONS", font=get_font(75), base_color="#6A1B9A", hovering_color="#6A1B9A")
        OPTIONS2_BUTTON.changeColor(MENU_MOUSE_POS)
        OPTIONS2_BUTTON.update(SCREEN)

        QUIT_BUTTON = Button(image=None, pos=(600, 575),
                           text_input="QUIT", font=get_font(75), base_color="#BA68C8", hovering_color="#FF44CC")
        QUIT_BUTTON.changeColor(MENU_MOUSE_POS)
        QUIT_BUTTON.update(SCREEN)

        QUIT2_BUTTON = Button(image=None, pos=(600, 565),
                           text_input="QUIT", font=get_font(75), base_color="#6A1B9A", hovering_color="#6A1B9A")
        QUIT2_BUTTON.changeColor(MENU_MOUSE_POS)
        QUIT2_BUTTON.update(SCREEN)
        
        logo_image = pygame.image.load("assets/logo.png")
        logo_image_rect = logo_image.get_rect(center=(270, 100))
        
        SCREEN.blit(logo_image, logo_image_rect)

        SCREEN.blit(MENU_BEAT_TEXT, MENU_BEAT_RECT)
        
        SCREEN.blit(MENU_BLITZ_TEXT,MENU_BLITZ_RECT)

        SCREEN.blit(MENU2_BEAT_TEXT, MENU2_BEAT_RECT)
        
        SCREEN.blit(MENU2_BLITZ_TEXT,MENU2_BLITZ_RECT)

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
                    loadingscreen()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click.play()
                    loadingscreen()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def LEADERBOARD(score): #leaderbaord menu
    while True:
        LEADERBOARD_MOUSE_POS = pygame.mouse.get_pos()

        SCORE_TEXT = get_font(45).render(f"Beat: {score}", True, "white")  # Display the score on the leaderboard

        SCREEN.blit(BG,(0,0))

        NAME_TEXT = get_font(45).render("Dancer:", True, "White")
        NAME_RECT = NAME_TEXT.get_rect(center=(235, 200))
       

        SCORE_TEXT=get_font(45).render("Beat:",True, "white")
        SCORE_RECT=SCORE_TEXT.get_rect(center=(800,200))
        
        LEADERBOARD_BACK = Button(image=None, pos=(125, 640), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        LEADERBOARD_BACK.changeColor(LEADERBOARD_MOUSE_POS)
        LEADERBOARD_BACK.update(SCREEN)

        LEADERBOARD_HEADER_TEXT=get_font(50).render("LEADERBOARD",True,"#f000fb")
        LEADERBOARD_HEADER_RECT=SCORE_TEXT.get_rect(center=(415,100))
        SCREEN.blit(LEADERBOARD_HEADER_TEXT,LEADERBOARD_HEADER_RECT)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEADERBOARD_BACK.checkForInput(LEADERBOARD_MOUSE_POS):
                    play()

        pygame.display.update()

class TextInputBox:
    def __init__(self, rect, font=None, text_color=(0, 0, 0), cursor_color=(0, 0, 0), max_length=3):
        # Update the rect to the desired position (600, 300)
        self.rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])
        self.rect.topleft = (450, 300)
        self.text = ""
        self.font = font or pygame.font.Font(None, self.rect.height - 4)
        self.text_color = text_color
        self.cursor_color = cursor_color
        self.cursor_visible = True
        self.cursor_timer = 0
        self.max_length = max_length

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                # Limit the text length to max_length
                self.text = self.text[:self.max_length]

        # Update cursor visibility
        self.cursor_timer += 1
        if self.cursor_timer % 30 == 0:
            self.cursor_visible = not self.cursor_visible

    def render(self, screen):
        # Render the text
        text_surface = self.font.render(self.text, True, self.text_color)

        # Update the rect position to (600, 300)
        self.rect.topleft = (450, 300)

        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        screen.blit(text_surface, (self.rect.x + 2, self.rect.y + 2))

        # Render the cursor
        if self.cursor_visible:
            cursor_x = self.rect.x + 2 + text_surface.get_width()
            cursor_y = self.rect.y + 2
            cursor_height = self.rect.height - 4
            pygame.draw.rect(screen, self.cursor_color, (cursor_x, cursor_y, 2, cursor_height))

def SONG1_EASY():
    pygame.display.set_caption("Play")

    # Get player's name
    player_name_input = TextInputBox((400, 300, 300, 50), font=get_font(40), max_length=3)

    while True:
        SONG1_EASY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(60).render("ENTER YOUR NAME", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(125, 640),
                           text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(SONG1_EASY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        LEADERBOARD1_EASY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(600, 650),
                                          text_input="Leaderboard", font=get_font(50), base_color="#d7fcd4",
                                          hovering_color="white")
        LEADERBOARD1_EASY_BUTTON.changeColor(SONG1_EASY_MOUSE_POS)
        LEADERBOARD1_EASY_BUTTON.update(SCREEN)

        READY1_EASY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(600,500),
                                          text_input="READY!", font=get_font(50), base_color="#d7fcd4",
                                          hovering_color="white")

        READY1_EASY_BUTTON.changeColor(SONG1_EASY_MOUSE_POS)
        READY1_EASY_BUTTON.update(SCREEN)

        # Get events once and store them
        events = pygame.event.get()

        # Update the text input box
        player_name_input.update(events)
        # Render the text input box
        player_name_input.render(SCREEN)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(SONG1_EASY_MOUSE_POS):
                    play()
                elif LEADERBOARD1_EASY_BUTTON.checkForInput(SONG1_EASY_MOUSE_POS):
                    LEADERBOARD()
                elif READY1_EASY_BUTTON.checkForInput(SONG1_EASY_MOUSE_POS):
                    # Call the game function with the player's name
                    game(player_name_input.text,"easy")

        pygame.display.update()

def SONG1_MED():
    pygame.display.set_caption("MEDIUM")

    # Get player's name
    player_name_input = TextInputBox((400, 300, 300, 50), font=get_font(40), max_length=3)

    while True:
        SONG1_MED_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(60).render("ENTER YOUR NAME", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(125, 640),
                           text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(SONG1_MED_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        LEADERBOARD1_MED_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(600, 650),
                                          text_input="Leaderboard", font=get_font(50), base_color="#d7fcd4",
                                          hovering_color="white")
        LEADERBOARD1_MED_BUTTON.changeColor(SONG1_MED_MOUSE_POS)
        LEADERBOARD1_MED_BUTTON.update(SCREEN)

        READY1_MED_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400,500),
                                          text_input="READY!", font=get_font(50), base_color="#d7fcd4",
                                          hovering_color="white")

        READY1_MED_BUTTON.changeColor(SONG1_MED_MOUSE_POS)
        READY1_MED_BUTTON.update(SCREEN)

        # Get events once and store them
        events = pygame.event.get()

        # Update the text input box
        player_name_input.update(events)
        # Render the text input box
        player_name_input.render(SCREEN)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(SONG1_MED_MOUSE_POS):
                    play()
                elif LEADERBOARD1_MED_BUTTON.checkForInput(SONG1_MED_MOUSE_POS):
                    LEADERBOARD()
                elif READY1_MED_BUTTON.checkForInput(SONG1_MED_MOUSE_POS):
                    # Call the game function with the player's name
                    game(player_name_input.text,"med")

        pygame.display.update()

def SONG1_EXP():
    pygame.display.set_caption("Play")

    # Get player's name
    player_name_input = TextInputBox((400, 300, 300, 50), font=get_font(40), max_length=3)

    while True:
        SONG1_EXP_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(60).render("ENTER YOUR NAME", True, "#f000fb")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(125, 640),
                           text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(SONG1_EXP_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        LEADERBOARD1_EXP_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(600, 650),
                                          text_input="Leaderboard", font=get_font(50), base_color="#d7fcd4",
                                          hovering_color="white")
        LEADERBOARD1_EXP_BUTTON.changeColor(SONG1_EXP_MOUSE_POS)
        LEADERBOARD1_EXP_BUTTON.update(SCREEN)

        READY1_EXP_BUTTON = Button(image=None, pos=(600, 500),
                           text_input="READY", font=get_font(50), base_color="#6A1B9A", hovering_color="#6A1B9A")
        READY1_EXP_BUTTON.changeColor(SONG1_EXP_MOUSE_POS)
        READY1_EXP_BUTTON.update(SCREEN)

        READY_EXP_BUTTON = Button(image=None, pos=(590, 500),
                           text_input="READY", font=get_font(50), base_color="#BA68C8", hovering_color="#FF44CC")
        READY_EXP_BUTTON.changeColor(SONG1_EXP_MOUSE_POS)
        READY_EXP_BUTTON.update(SCREEN)

        # Get events once and store them
        events = pygame.event.get()

        # Update the text input box
        player_name_input.update(events)
        # Render the text input box
        player_name_input.render(SCREEN)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(SONG1_EXP_MOUSE_POS):
                    play()
                elif LEADERBOARD1_EXP_BUTTON.checkForInput(SONG1_EXP_MOUSE_POS):
                    LEADERBOARD()
                elif READY1_EXP_BUTTON.checkForInput(SONG1_EXP_MOUSE_POS):
                    # Call the game function with the player's name
                    game(player_name_input.text,"exp")

        pygame.display.update()

def doWork():
    # do some math work for a certain amount of time
    global loading_finished, loading_progress

    for i in range(WORK):
        math_equation = 523687 / 756397 * 52803
        loading_progress += 1  # Increment loading progress
        pygame.time.delay(2)  # Introduce a small delay to slow down the loop

    loading_finished = True

def loadingscreen():
    global loading_finished, loading_progress

    loading_time = pygame.time.get_ticks() + random.randint(1000, 2000)  # Set the end time

    while not loading_finished and pygame.time.get_ticks() < loading_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.blit(BG, (0, 0))

        # Rotate the loading image
        loading_image_rotated = pygame.transform.rotate(loading_image, loading_progress % 360)
        loading_image_rect = loading_image_rotated.get_rect(center=(640, 360))

        SCREEN.blit(loading_image_rotated, loading_image_rect)
        SCREEN.blit(finished_text, finished_rect)

        pygame.display.update()
        CLOCK.tick(60)

def game(player_name,difficulty):
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
    score = 0

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
                        score += 100
                        STILL_UP.image = gld_u
                        UP_ARROW.rect.y = 710
                        UP_ARROW.kill()
                    elif UP_ARROW.rect.y > 10 and UP_ARROW.rect.y < 65 :
                        score += 50
                        STILL_UP.image = grn_u
                        UP_ARROW.rect.y = 710
                        UP_ARROW.kill()
                    else:
                        UP_ARROW.rect.y = 710
                        UP_ARROW.kill()
                        if score > 0:
                            score -= 25
                        
                

                # DOWN ARROW
                if event.key == pygame.K_s: 
                    if DOWN_ARROW.rect.y > 20 and DOWN_ARROW.rect.y < 45 :
                        score += 100
                        DOWN_ARROW.rect.y = 710
                        DOWN_ARROW.kill()
                        STILL_DOWN.image = gld_d
                    
                    elif DOWN_ARROW.rect.y > 10 and DOWN_ARROW.rect.y <65 :
                        score += 50
                        DOWN_ARROW.rect.y = 710
                        DOWN_ARROW.kill()
                        STILL_DOWN.image = grn_d
        
                    else:
                        DOWN_ARROW.rect.y = 710
                        DOWN_ARROW.kill()
                        if score > 0:
                            score -= 25
                        
                    
                # LEFT ARROW
                if event.key == pygame.K_d: 
                    if LEFT_ARROW.rect.y > 20 and LEFT_ARROW.rect.y < 45 :
                        score += 100
                        STILL_LEFT.image = gld_l
                        LEFT_ARROW.rect.y = 710
                        LEFT_ARROW.kill()
                    elif LEFT_ARROW.rect.y > 10 and LEFT_ARROW.rect.y < 65 :
                        score += 50
                        STILL_LEFT.image = grn_l
                        LEFT_ARROW.rect.y = 710
                        LEFT_ARROW.kill()
                    else:
                        LEFT_ARROW.rect.y = 710
                        LEFT_ARROW.kill()
                        if score > 0:
                            score -= 25
                        
               
                # RIGHT ARROW
                if event.key == pygame.K_f: 
                    if RIGHT_ARROW.rect.y > 20 and RIGHT_ARROW.rect.y < 45 :
                        score += 100
                        STILL_RIGHT.image = gld_r
                        RIGHT_ARROW.rect.y = 710
                        RIGHT_ARROW.kill()
                    elif RIGHT_ARROW.rect.y > 10 and RIGHT_ARROW.rect.y < 65 :
                        score += 50
                        STILL_RIGHT.image = grn_r
                        RIGHT_ARROW.rect.y = 710
                        RIGHT_ARROW.kill()
                    else:
                        RIGHT_ARROW.rect.y = 710
                        RIGHT_ARROW.kill()
                        if score > 0:
                            score -= 25
                        
        
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
                if score > 0:
                            score -= 25
                        
        
        if not mixer.music.get_busy():
            pygame.quit()
            sys.exit()

        print(all_still)
        print(all_sprites)
        print(score)

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
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

         # Save the score before exiting
        save_score(player_name, score, difficulty)
        


        pygame.display.flip()

        # Cap the frame rate
        CLOCK.tick(144)


# Example usage:

# threading
threading.Thread(target=lambda: doWork()).start()

main_menu()
 

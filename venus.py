import pygame, sys, random
from pygame.locals import *
pygame.init()

#Load Assets
BACKGROUND = pygame.image.load(r'assets\backgrounds\Sitting_Room.png')
SMILE = pygame.image.load(r'assets\sprites\wisteria_school_smile.png')
SAD = pygame.image.load(r'assets\sprites\wisteria_school_sad.png')
UPSET = pygame.image.load(r'assets\sprites\wisteria_school_upset.png')
WONDER = pygame.image.load(r'assets\sprites\wisteria_school_wonder.png')
FLUSTERED = pygame.image.load(r'assets\sprites\wisteria_school_embarrassed.png')
EMBARRASED = pygame.image.load(r'assets\sprites\wisteria_school_embarrassed.png')
ICON = pygame.image.load(r'assets\sprites\icon.png')
MUSIC = pygame.mixer.music.load(r'assets\bgm.mp3')
DIALOGUE_BOX = pygame.image.load(r'assets\DialogueBox.png')
CALCULATOR = pygame.image.load(r'assets\Calculator.png')

#Settings
pygame.display.set_caption('Project Venus')
pygame.display.set_icon(ICON)
mainClock = pygame.time.Clock()
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

CURRENT_FACE = UPSET

#Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VIOLET = (238, 130, 238)
SIZE = WIDTH, HEIGHT = (1920, 1080)
DESIGN_CENTER_X = 1920/2
DESIGN_CENTER_Y =  1080/2
PACING_SPEED = [10,0]
ENTER = 0
TRIES = 0
TEXT = ['...', 'Ah you must be Player.', 'My name is Venus. I\'m really excited to finally meet you.', 'Ah! Venus would like to play a game with Player.', 'The game is as follows..', 'Venus will think of a number between 0 and 100 and Player will guess', ' Ready?', 'What number am I thinking of?']
CURRENT_TEXT = TEXT[ENTER]
GUESS = []
GUESS_STRING = 0
ANSWER = random.randint(0, 100)

#Flags
PACING = True
INTRO = False
MAIN = False
RESULT = False
POINT_FLAG = False

#Artificial Surfaces and Rectangles
BACKGROUND_RECT = BACKGROUND.get_rect()
CURRENT_FACE_RECT = CURRENT_FACE.get_rect()

DIALOGUE_BOX_RECT = DIALOGUE_BOX.get_rect(center = [DESIGN_CENTER_X, 900])

#Miscellaneous Functions
def text(string, fontsize, colour=BLACK):
    font = pygame.font.Font(r'assets\font.ttf', fontsize)
    message = font.render(string, True, colour)
    return message

#Object Creation
PRESS_W = text('Press W to wave', 100)
PRESS_W_RECT = PRESS_W.get_rect(center = [BACKGROUND_RECT.centerx + 575, 200])

NAME = text('Venus', 50, VIOLET)
NAME_RECT = NAME.get_rect(topleft = [DIALOGUE_BOX_RECT.topleft[0] + 100, DIALOGUE_BOX_RECT.topleft[1] + 75])

DIALOGUE = text(CURRENT_TEXT, 20, BLACK)
DIALOGUE_RECT = DIALOGUE.get_rect(topleft = [DIALOGUE_BOX_RECT.topleft[0] + 100, DIALOGUE_BOX_RECT.topleft[1] + 225])

CALCULATOR_RECT = CALCULATOR.get_rect(center = [DESIGN_CENTER_X + 578, DESIGN_CENTER_Y - 150])

CALCULATOR_SCREEN = pygame.Surface((425, 150))
CALCULATOR_SCREEN.fill(WHITE)
CALCULATOR_SCREEN_RECT = CALCULATOR_SCREEN.get_rect(center = [CALCULATOR_RECT.centerx, CALCULATOR_RECT.centery - 150])



#Main Game Loop. Screen is the real layer and Dummy is the design layer.
screen = pygame.display.set_mode(SIZE, HWSURFACE|DOUBLEBUF|RESIZABLE)
dummy = pygame.Surface((1920, 1080))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == VIDEORESIZE:
            SIZE = (event.w, event.h)
         
        if event.type == pygame.KEYDOWN:

            if PACING:
                if event.key == K_w:
                    CURRENT_FACE = WONDER
                    PACING_SPEED  = [0,0]
                    INTRO = True
                    PACING = False
                    print("Pacing exited, Intro entered")

            if INTRO:
                if event.key == K_RETURN:
                    if ENTER != 7:
                        ENTER += 1
                    if ENTER == 7:
                        MAIN = True
                        INTRO = False
                        print("Intro exited, Main entered")
            
            if MAIN:
                if len(GUESS) <= 3:
                    if event.key == K_0 or event.key == K_KP_0:
                        GUESS.append('0')
                    if event.key == K_1 or event.key == K_KP_1:
                        GUESS.append('1')
                    if event.key == K_2 or event.key == K_KP_2:
                        GUESS.append('2')
                    if event.key == K_3 or event.key == K_KP_3:
                        GUESS.append('3')
                    if event.key == K_4 or event.key == K_KP_4:
                        GUESS.append('4')
                    if event.key == K_5 or event.key == K_KP_5:
                        GUESS.append('5')
                    if event.key == K_6 or event.key == K_KP_6:
                        GUESS.append('6')
                    if event.key == K_7 or event.key == K_KP_7:
                        GUESS.append('7')
                    if event.key == K_8 or event.key == K_KP_8:
                        GUESS.append('8')
                    if event.key == K_9 or event.key == K_KP_9:
                        GUESS.append('9')
                if len(GUESS) >= 1:
                    if event.key == K_BACKSPACE:
                        GUESS.pop()
                    if event.key == K_RETURN:
                        RESULT = True
                        TRIES += 1
                        if int(GUESS_STRING) == ANSWER:
                            CURRENT_FACE = SMILE
                            if TRIES == 1:
                                CURRENT_FACE = WONDER
                                CURRENT_TEXT = 'WOW! It only took Player one try to guess that. Will Player promise to make Venus as smart as them one day?'
                            if TRIES <= 7:
                                CURRENT_FACE = SMILE    
                                CURRENT_TEXT = 'You got it! It only took Player ' + str(TRIES) + ' tries.'
                            if TRIES > 7:
                                CURRENT_FACE = SAD
                                CURRENT_TEXT = 'Oh gosh. It took Player a while to figure that one out. Maybe someday Venus will teach Player how to be as smart as her.'

                        elif int(GUESS_STRING) < ANSWER:
                            CURRENT_FACE = SAD
                            CURRENT_TEXT = 'Try a little higher.'
                            
                        else:
                            CURRENT_FACE = SAD
                            CURRENT_TEXT = 'Try a little lower.'
                            

    #Always visible
    dummy.blit(BACKGROUND, BACKGROUND_RECT)
    dummy.blit(CURRENT_FACE, CURRENT_FACE_RECT)

    #Visible if a condition is met.
    if PACING:
        dummy.blit(PRESS_W, PRESS_W_RECT)
        CURRENT_FACE_RECT = CURRENT_FACE_RECT.move(PACING_SPEED)
        if CURRENT_FACE_RECT.left < 0 or CURRENT_FACE_RECT.right > 1320:
            PACING_SPEED[0] = -PACING_SPEED[0]
            CURRENT_FACE = pygame.transform.flip(CURRENT_FACE, True, False)

    if not PACING:
        DIALOGUE = text(CURRENT_TEXT, 30, BLACK)
        dummy.blit(DIALOGUE_BOX, DIALOGUE_BOX_RECT)
        dummy.blit(DIALOGUE, DIALOGUE_RECT)
        dummy.blit(NAME, NAME_RECT)

    if INTRO:
        if ENTER == 1:
            CURRENT_FACE = SMILE
        CURRENT_TEXT = TEXT[ENTER]
        if ENTER == 3:
            CURRENT_FACE = WONDER
        if ENTER == 4:
            CURRENT_FACE = SMILE

    if MAIN or RESULT:
        GUESS_STRING = "".join(GUESS)
        GUESS_OBJECT = text(GUESS_STRING, 65, BLACK)
        dummy.blit(CALCULATOR, CALCULATOR_RECT)
        dummy.blit(CALCULATOR_SCREEN, CALCULATOR_SCREEN_RECT)
        dummy.blit(GUESS_OBJECT, GUESS_OBJECT.get_rect(center = CALCULATOR_SCREEN_RECT.center))

    if MAIN:
        CURRENT_FACE = WONDER
        if GUESS == []:
            CURRENT_TEXT = 'What number am I thinking of?'
        
    if RESULT:
        if len(GUESS) >= 1:
            if int(GUESS_STRING) == ANSWER:
                if TRIES == 1:
                    CURRENT_FACE = WONDER
                                    
                if TRIES <= 7:
                    CURRENT_FACE = SMILE    
                                    
                if TRIES > 7:
                    CURRENT_FACE = SAD
                                
            
            elif int(GUESS_STRING) < ANSWER:
                CURRENT_FACE = SAD
                                        
            else:
                CURRENT_FACE = SAD
                            
    
    


    #Resolution scaling and screen refresh.
    frame = pygame.transform.scale(dummy, SIZE)
    screen.blit(frame, frame.get_rect())
    pygame.display.flip()
    mainClock.tick(60)
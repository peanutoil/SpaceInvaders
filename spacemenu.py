import pygame
import random
import time
from pygame.locals import*

pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()
screen=pygame.display.set_mode((800,675))
pygame.display.set_caption("M E N U")
run = 1
5
green=(0,255,0)
white = (255,255,255)
red=(255,0,0)
blue=(0,0,255)
black = (0,0,0)
cy = 295
dots = []

title = pygame.image.load("SPACE-INVADERS.png").convert_alpha()
start = pygame.image.load("START-GAME.png").convert_alpha()
stop = pygame.image.load("QUIT.png").convert_alpha()
instructions = pygame.image.load("INSTRUCTIONS.png").convert_alpha()
store = pygame.image.load("SHOP.png").convert_alpha()

coin1 = pygame.image.load("coin1.png").convert_alpha()
coin1 = pygame.transform.scale(coin1, (50,50))
coin2 = pygame.image.load("coin2.png").convert_alpha()
coin2 = pygame.transform.scale(coin2, (50,50))
coin3 = pygame.image.load("coin3.png").convert_alpha()
coin3 = pygame.transform.scale(coin3, (50,50))
coin4 = pygame.image.load("coin4.png").convert_alpha()
coin4 = pygame.transform.scale(coin4, (50,50))
coin5 = pygame.image.load("coin5.png").convert_alpha()
coin5 = pygame.transform.scale(coin5, (50,50))
coin6 = pygame.image.load("coin6.png").convert_alpha()
coin6 = pygame.transform.scale(coin6, (50,50))
coins = [coin1,coin2,coin3,coin4,coin5,coin6]

for a in range(500):
    x = random.randrange(0,800)
    y = random.randrange(0,675)
    dots.append([x,y])
    
def rotate(gamemusic):
    global cy
    global x
    global screen

            
    for coin in coins:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type==KEYDOWN:
                if event.key==K_DOWN:
                    cy = cy + 75
                    if cy>520:
                        cy = 295
                if event.key==K_UP:
                    cy = cy - 75
                    if cy<290:
                        cy = 520
                if event.key==K_RETURN:
                    #insert some sort of sound here
                    if cy==295:
                        screen = pygame.display.set_mode((600,700))
                        pygame.display.set_caption("Space Invaders")
                        import spaceshop
                        spaceshop.rungame()
                    if cy==370:
                        print("Instructions")
                    if cy==445:
                        run = 0
                        screen = pygame.display.set_mode((800,675))
                        pygame.display.set_caption("S H O P")
                        import spaceshop
                        spaceshop.shop(gamemusic)
                    if cy==520:
                        print("Quit")             
                        
        screen.blit(title,(5,75))
        screen.blit(start,(250,300))
        screen.blit(instructions,(250,375))
        screen.blit(store,(250,450))
        screen.blit(stop,(250,525))
        screen.blit(coin,(200,cy))
        for dot in range(len(dots)):
            pygame.draw.circle(screen,white,dots[dot],1)
            dots[dot][0] -= 5
            if dots[dot][0]<0:
                x = random.randrange(810,850)
                dots[dot][0] = x
                y = random.randrange(0,675)
                dots[dot][1] = y
        pygame.display.update()
        time.sleep(0.1)
        screen.fill(black)

sounds = pygame.mixer.music.load("playingwithfire.mp3")

def menu(gamesound):
    global screen
    global cy
    pygame.display.set_caption("M E N U")
    pygame.mixer.music.set_volume(500)
    pygame.mixer.music.play(0)
    print(gamesound)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type==KEYDOWN:
                if event.type==K_DOWN:
                    print("KEY IS DOWN",cy)
                    cy = cy + 75
                    if cy>520:
                        cy = 295                
        pygame.display.update()
        clock.tick(30)
        rotate(gamesound)

if run == 0:
    run = 0
    print("ok")
if run == 1:
    gamesound = "Power.mp3"
    menu(gamesound)


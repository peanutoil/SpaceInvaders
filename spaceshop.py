import pygame
import random
import time
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((800,675))
green = (0,255,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
purple = (186,85,211)
backColor = purple
musicColor = white

heading = pygame.image.load("STORE.png")
note = pygame.image.load("bluemusic.png")
note = pygame.transform.scale(note,(75,75))
plzwork = "Power.mp3"

screen.fill(black)

def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freeans",60)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

def words(msg,x,y,color):
    fontobj=pygame.font.SysFont("freeans",40)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
    
def shop(gamesong):
    global screen
    global plzwork
    global backColor
    global musicColor
    pygame.display.set_caption("S H O P")
    music = pygame.mixer.music.load("TT.mp3")
    pygame.mixer.music.set_volume(500)
    pygame.mixer.music.play(0)
    print(gamesong)
    
    while True:
        pygame.display.update()
        
        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEMOTION:
                xm,ym = event.pos
                if 325<=xm<=475 and 475<=ym<=565:
                    backColor = green
                else:
                    backColor = purple
                if 90<=xm<=200 and 150<=ym<=300:
                    musicColor = blue
                else:
                    musicColor = white
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                x,y=event.pos
                
##                if 5<=x<=93 and 70<=y<=170:
##                    import game
##                    if game.coins >= 10:
##                        game.coins = game.coins - 10
##                        print("You have bought: Caveman Spongebob!")
##                        print("Coins:",game.coins)
##                        game.plane = game.cavebob
##                        
##                if 200<=x<=300 and 70<=y<170:
##                    import game
##                    if game.coins >= 10:
##                        game.coins = game.coins - 10
##                        print("You have bought: Pepe!")
##                        print("Coins:",game.coins)
##                        game.plane = game.pepe
##                        
##                if 350<=x<=438 and 70<=y<=170:
##                    import game
##                    if game.coins >= 10:
##                        game.coins = game.coins - 10
##                        print("You have bought: Shrek!")
##                        print("Coins:",game.coins)
##                        game.plane = game.shrek
##                        
##                if 50<=x<=138 and 220<=y<=320:
##                    import game
##                    if game.coins >= 50:
##                        game.coins = game.coins - 50
##                        print("You have bought: Donald Trump!")
##                        print("Coins:",game.coins)
##                        game.plane = game.trump
##                        
##                if 300<=x<=388 and 220<=y<=320:
##                    import game
##                    if game.coins >= 50:
##                        game.coins = game.coins - 50
##                        print("You have bought: Ugandan Knuckles!")
##                        print("Coins:",game.coins)
##                        game.plane = game.ugandanKnuckles
                        
                if 325<=x<=475 and 475<=y<=565:
                        x = 0
                        y = 0
                        screen.fill(black)
                        screen = pygame.display.set_mode((800,675))
                        pygame.display.set_caption("M E N U")
                        plzwork = gamesong
                        import spacemenu
                        spacemenu.menu(gamesong)

                if 90<=x<=200 and 150<=y<=300:
                        print("MUSIC SHOP")
                        x = 0
                        y = 0
                        screen.fill(black)
                        screen = pygame.display.set_mode((800,675))
                        pygame.display.set_caption("S H O P")
                        import spacemusic
                        spacemusic.musicshop()
        pygame.draw.rect(screen,white,(325,475,150,90))
        show_text("BACK",340,500,backColor)               
        screen.blit(heading,(300,75))
        screen.blit(note,(100,190))
        words("M U S I C",90,270,musicColor)

def rungame():
    global plzwork
    import SpaceInvaders
    SpaceInvaders.game(plzwork)

import pygame
import random
import time
from pygame.locals import *
pygame.init()
#add sound for when item is purchased
screen = pygame.display.set_mode((800,675))
white = (255,255,255)
black = (0,0,0)
purple = (186,85,211)
green = (0,255,0)
backColor = purple

heading = pygame.image.load("STORE.png")
notes = [1,2,3,4,5,6,7,8,9,10]
songs = ["Power $30","Lotto $30","Suit $20","Boss: $20","Cream: $30","Oof: $50","Boo: $30","Likey $30","Signal $30","Super $20"]
x = 0
y = 0
run = 1

for i in range(1,11):
    notes[i-1] = pygame.image.load("note"+str(i)+".png")

def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freeans",60)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

def words(msg,x,y,color):
    fontobj=pygame.font.SysFont("freeans",30)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

def hide(x,y):
    pygame.draw.rect(screen,black,(x,y,100,150))

def displays():
    mx = 90
    my = 200
    global screen
    for i in range(0,5):
        screen.blit(notes[i],(mx,my))
        words(songs[i],mx-10,my+50,white)
        mx = mx + 150

    mx = 90
    my = 350

    for i in range(5,10):
        screen.blit(notes[i],(mx,my))
        words(songs[i],mx-50,my+50,white)
        mx = mx + 150

oof = pygame.mixer.music.load("oof.mp3")
peekaboo = pygame.mixer.music.load("peekaboo.mp3")
likey = pygame.mixer.music.load("likey.mp3")
signal = pygame.mixer.music.load("signal.mp3")
superfly = pygame.mixer.music.load("superfly.mp3")

mainsong = pygame.mixer.music.load("power.mp3")
  
def musicshop():
    global screen
    displays()
    music = pygame.mixer.music.load("asifitsurlast.mp3")
    pygame.mixer.music.set_volume(500)
    pygame.mixer.music.play(0)
    global mainsong
    global backColor
    message = ""   
    screen.blit(heading,(300,75))
    pygame.draw.rect(screen,white,(325,475,150,90))
    pygame.display.set_caption("S H O P")
    while True:
        pygame.display.update()
        global x
        global y
        
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
                
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                x,y=event.pos
                
                if 325<=x<=475 and 475<=y<=565:
                    x = 0
                    y = 0
                    screen.fill(black)
                    screen = pygame.display.set_mode((800,675))
                    pygame.display.set_caption("S H O P")
                    import spaceshop
                    spaceshop.shop(mainsong)

                if 90<=x<=122 and 200<=y<=232:
                    x = 0
                    y = 0
                    print("You bought the song 'Power' for $30")
                    message = "You bought 'Power' for $30"
                    mainsong = "Power.mp3"

                if 240<=x<=272 and 200<=y<=232:
                    x = 0
                    y = 0
                    print("You bought the song 'Lotto' for $30")
                    message = "You bought 'Lotto' for $30"
                    mainsong = "Lotto.mp3"

                if 390<=x<=422 and 200<=y<=232:
                    x = 0
                    y = 0
                    print("You bought the song 'Black Suit' for $20")
                    message = "You bought 'Black Suit' for $20"
                    mainsong = "Black Suit.mp3"

                if 540<=x<=572 and 200<=y<=232:
                    x = 0
                    y = 0
                    print("You bought the song 'Boss' for $20")
                    message = "You bought 'Boss' for $20"
                    mainsong = "Boss.mp3"

                if 690<=x<=722 and 200<=y<=232:
                    x = 0
                    y = 0
                    print("You bought the song 'Ice Cream Cake' for $30")
                    message = "You bought 'Ice Cream Cake' for $30"
                    mainsong = "Ice Cream Cake.mp3"

                if 90<=x<=122 and 350<=y<=382:
                    x = 0
                    y = 0
                    print("You bought the sound 'Oof' for $50")
                    message = "You bought the sound 'Oof' for $50"

                if 240<=x<=272 and 350<=y<=382:
                    x = 0
                    y = 0
                    print("You bought the song 'Peek A Boo' for $30")
                    message = "You bought 'Peek A Boo' for $30"
                    mainsong = "Peek A Boo.mp3"

                if 390<=x<=422 and 350<=y<=382:
                    x = 0
                    y = 0
                    print("You bought the song 'Likey' for $30")
                    message = "You bought 'Likey' for $30"
                    mainsong = "Likey.mp3"

                if 540<=x<=572 and 350<=y<=382:
                    x = 0
                    y = 0
                    print("You bought the song 'Signal' for $30")
                    message = "You bought 'Signal' for $30"
                    mainsong = "Signal.mp3"

                if 690<=x<=722 and 350<=y<=382:
                    x = 0
                    y = 0
                    print("You bought the song 'Superfly' for $20")
                    message = "You bought 'Superfly' for $20"
                    mainsong = "Superfly.mp3"
            show_text("BACK",340,500,backColor)

if run == 1:
    musicshop()

#ALLOW USER TO CHOOSE SHIP (store?)
#ALLOW USE TO CHOOSE BULLETS (store?)
#ALLOW USER TO BUY DIFF AMMO (store?)
#ALLOW USER TO BUY DIFF MUSIC (store?)
#MAKE GAME MENU W/INSTRUCTIONS PAGE

import pygame
from pygame.locals import *
pygame.init()
import time
import random
import threading
clock = pygame.time.Clock()
fps = 100

a1 = pygame.image.load("a1.png").convert_alpha()
a2 = pygame.image.load("a2.png").convert_alpha()
a3 = pygame.image.load("a3.png").convert_alpha()
h1 = pygame.image.load("heart1.jpg").convert_alpha()
h2 = pygame.image.load("heart2.jpg").convert_alpha()
h3 = pygame.image.load("heart3.jpg").convert_alpha()
h1 = pygame.transform.scale(h1,(20,20))
h2 = pygame.transform.scale(h2,(20,20))
h3 = pygame.transform.scale(h3,(20,20))
ground = pygame.image.load("ground.jpg").convert_alpha()
afire = pygame.image.load("afire.jpg").convert_alpha()

a4 = a2
xco = 20
yco = 20
sx = 250
sy = 500
alien = pygame.image.load("crater1.png")
aliens = []
bullet_list = []
abullet_list = []
bx = 0
by = 20

ship = pygame.image.load("ship.png").convert_alpha()
shoot = pygame.image.load("bluebomb.png").convert_alpha()
shoot = pygame.transform.scale(shoot,(30,30))
shooter = pygame.image.load("shooter.jpg").convert_alpha()
shooter = pygame.transform.scale(shooter,(50,50))
afire = pygame.transform.scale(afire,(25,25))

class Alien:
    
    def __init__(self,xco,yco,alien):
        self.x = xco
        self.y = yco
        self.image = alien
        self.start = time.time()

    def draw(self):
        screen.blit(self.image,(self.x,self.y))
#        self.move()
        stop = time.time()
        if stop-self.start>10:
            self.y=self.y+50
            self.start = time.time()
            
##    def move(self):
##        xchange = random.randint(-10,10)
##        self.x = self.x + xchange

##Boss shoots plane when they are aligned
##Boss randomly moves left to right and random speeds
        
class Boss:

    def __init__(self,bx,by,shooter):
        self.x = bx
        self.y = by
        self.image = shooter
        self.start = time.time()
        self.right = 0
        self.left = 0
        
    def draw(self):
        screen.blit(self.image,(self.x,self.y))

        if self.right==1 and self.x<=500:
            self.x=self.x+10
        if self.left==1 and self.x>=0:
            self.x=self.x-10

        for abullet in abullet_list:
            screen.blit(afire,(abullet+[5,10]))
            abullet[1] += 10
            if abullet[1] == 700:
                abullet_list.remove(abullet)

    def move(self,event,abullet_list):
        if event.type==KEYDOWN:
            if event.key==K_l:
                self.right=1
            if event.key==K_j:
                self.left=1
            if event.key==K_b:
               abullet_list.append([self.x+10, self.y+40])
               
        elif event.type==KEYUP:
            if event.key==K_l:
                self.right=0
            if event.key==K_j:
                self.left=0
            if event.key==K_b:
                abullet=False
    
class Ship():

    def __init__(self,sx,sy):
        self.x = sx
        self.y = sy
        self.image = ship
        self.right = 0
        self.left = 0
        self.lives = 3
        
    def draw(self):
        screen.blit(self.image,(self.x,self.y))

        if self.right==1 and self.x<=500:
            self.x=self.x+10
        if self.left==1 and self.x>=0:
            self.x=self.x-10

        for bullet in bullet_list:
            #pygame.draw.rect(screen,(255,0,0),bullet + [5,10])
            screen.blit(shoot,(bullet + [5,10]))
            bullet[1]= bullet[1]- 10
            if bullet[1]==700:
                bullet_list.remove(bullet)
##            if bullet[0] in range(xco,xco+50) and bullet[1] in range(yco,yco+7):
##                bullet_list.remove(bullet)
##                print("oof")
                
    def move(self,event,bullet_list):
        if event.type==KEYDOWN:
            if event.key==K_RIGHT or event.key==K_d:
                self.right=1
            if event.key==K_LEFT or event.key==K_a:
                self.left=1
            if event.key==K_SPACE or event.key==K_UP:
               bullet_list.append([self.x+40, self.y])
               
        elif event.type==KEYUP:
            if event.key==K_RIGHT or event.key==K_d:
                self.right=0
            if event.key==K_LEFT or event.key==K_a:
                self.left=0
            if event.key==K_SPACE or event.key==K_UP:
                bullet=False

            

ship = Ship(sx,sy)
music = pygame.mixer.music.load("power.mp3")

for y in range(0,3):
    if y == 0:
        a4 = a1
    if y == 1:
        xco = 25
        a4 = a2
        yco = yco + 50
    if y == 2:
        a4 = a3
        yco = yco + 60
    for x in range(0,5):
            alien1 = Alien(xco,yco,a4)
            xco = xco + 120
            aliens.append(alien1)
    xco = 0

##t1 = threading.Thread(target = ship.move)
##t2 = threading.Thread(target = aliens_print)
##t3 = threading.Thread(target = ship.draw)
##t1.start()
##t2.start()
##t3.start()

class Hearts():
    def __init__(self):
        self.stage = h1
    def showLives(self,hx,hy):
        screen.blit(self.stage,(hx,hy))

life1 = Hearts()
life2 = Hearts()
life3 = Hearts()
killem = Boss(bx,by,shooter)

def game(abtime):
    global screen
    global music
    print(abtime)
    if abtime == "Boss.mp3":
        music = pygame.mixer.music.load("boss.mp3")
    if abtime == "Power.mp3":
        music = pygame.mixer.music.load("power.mp3")
    if abtime == "Lotto.mp3":
        music = pygame.mixer.music.load("lotto.mp3")
    if abtime == "Black Suit.mp3":
        music = pygame.mixer.music.load("black suit.mp3")
    if abtime == "Ice Cream Cake.mp3":
        music = pygame.mixer.music.load("icecreamcake.mp3")
    if abtime == "Peek A Boo.mp3":
        music = pygame.mixer.music.load("peekaboo.mp3")
    if abtime == "Likey.mp3":
        music = pygame.mixer.music.load("likey.mp3")
    if abtime == "Signal.mp3":
        music = pygame.mixer.music.load("signal.mp3")
    if abtime == "Superfly.mp3":
        music = pygame.mixer.music.load("superfly.mp3")
    screen = pygame.display.set_mode((600,700))
    pygame.display.set_caption("Space Invaders")
    pygame.mixer.music.set_volume(500)
    pygame.mixer.music.play(0)
    pygame.draw.rect(screen,(255,0,0),(0,0,5,10))
    redrawCount = random.randint(15,35)
    drawaliens = random.sample(aliens,3)  
    
    while True:
        screen.fill((0,0,0))
        clock.tick(50)
        life1.showLives(575,20)
        life2.showLives(545,20)
        life3.showLives(515,20)
        screen.blit(ground,(0,605))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            ship.move(event,bullet_list)
            killem.move(event,abullet_list)
        ship.draw()
        killem.draw()
  
        redrawCount = redrawCount - 1
        if redrawCount == 0:
            if len(aliens)<3:
                drawaliens = random.sample(aliens,len(aliens))
            else:
                drawaliens = random.sample(aliens,3)
            redrawCount = random.randint(20,50)
        #for a in range(0,len(aliens)):
        for a in drawaliens:
            a.draw()
            if(len(aliens))<3:
               if a.x<10:
                   a.x = 10
               if a.x>590:
                   a.x = 590
               a.x = a.x + random.randint(-10,10)
               if a.y<10:
                   a.y = 10
               if a.y > 590:
                   a.y = 590
               a.y = a.y+random.randint(-10,10)
            for bullets in bullet_list:
                if bullets[0] in range (a.x,a.x+50) and bullets[1] in range (a.y,a.y+7):
                    aliens.remove(a)
                    drawaliens.remove(a)
                    bullet_list.remove(bullets)
                    print(len(aliens))
                    print("oof")
                    
            #time.sleep(0.3)
            #newa = random.randint(1,10)
            #screen.fill((0,0,0))
            #aliens[a].draw()
##            if a<(15-newa):
##                aliens[a+newa].draw()
##            aliens[a].move()
##            if a<(15-newa):
##                aliens[a+newa].move()
            #pygame.display.update()
        pygame.display.update()
    ##    t1.join()
    ##    t2.join()
    ##    t3.join()

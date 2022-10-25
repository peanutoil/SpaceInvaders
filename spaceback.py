import pygame
import random
import time
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((800,675))
black = (0,0,0)
white = (255,255,255)
pygame.display.set_caption("Testing")
dots = []
clock = pygame.time.Clock()

for a in range(500):
    x = random.randrange(0,800)
    y = random.randrange(0,675)
    dots.append([x,y])

def woah():
    global x
    for dot in range(len(dots)):
            pygame.draw.circle(screen,white,dots[dot],1)
            dots[dot][0] -= 1
            if dots[dot][0]<0:
                x = random.randrange(810,850)
                dots[dot][0] = x
                y = random.randrange(0,675)
                dots[dot][1] = y
    pygame.display.update()
    clock.tick(50)
    screen.fill(black)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    woah()
    pygame.display.update()

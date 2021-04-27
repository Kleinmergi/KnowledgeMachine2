import pygame
from pygame.locals import *
import sys
#import pythonforandroid
import math

from Szene import Szene

pygame.init()
screen = pygame.display.set_mode([800, 800])
pygame.mouse.set_visible(1)

x = 300
y = 300
time = pygame.time.Clock()

w, h = pygame.display.get_surface().get_size()

dx = 5
dy = 7

S = Szene("E-Lehre")
bColor = S.config["Farbe"]
print(bColor)

def abst(x, y, u, w):
    return math.sqrt(math.pow(x - u, 2) + math.pow(y - w, 2))


def sign(x):
    if x < 0:
        return -1
    return 1


go = True
while go:
    screen.fill((bColor[0], bColor[1], bColor[2]))
    mpx, mpy = pygame.mouse.get_pos()
    r = abst(x, y, mpx, mpy)
    ax = sign(mpx - x) * math.pow(mpx - x, 2) / (100 * r)
    ay = sign(mpy - y) * math.pow(mpy - y, 2) / (100 * r)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    gdr = pygame.key.get_pressed()
    # print(gdr)
    if gdr[K_UP]:
        ay = -2
    if gdr[K_DOWN]:
        ay = 2
    if gdr[K_RIGHT]:
        ax = 2
    if gdr[K_LEFT]:
        ax = -2
    dx += ax - dx / 100
    dy += ay - dy / 100

    x = (x + dx)
    if x < 0:
        x += w
    elif x > w:
        x -= w

    y = (y + dy) % h
    if y < 0:
        y += h
    elif y > h:
        y -= h

    pygame.draw.circle(screen, (0, 255, 255), (mpx, mpy), 10)

    pygame.draw.rect(screen, (255, 0, 0), (x-20, y-20, 40, 40))
    pygame.display.update()
    time.tick(60)
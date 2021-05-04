
import pygame
from pygame.locals import *

RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
w, h = 640, 640
screen = pygame.display.set_mode((w, h))
running = True

img = pygame.image.load('bernstein.png')
img.convert()

moving = False
t = 0
while running:
    t = (t+0.1)
    k = min(15,t//1)
    ev = pygame.event.get()

    # proceed events
    for event in ev:

        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            t = 0



    rect = pygame.Rect((15*512-k*512,0),(512,512))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False

        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
    
    screen.fill(GRAY)
    screen.blit(img,(0,0), rect)

    pygame.display.update()

pygame.quit()
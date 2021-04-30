import math
import sys
from pygame.locals import *
import OwnMath

import OwnMath
import pygame

class MausFolgen():

    def __init__(self, screen):
        self.x = 300
        self.y = 300
        self.dx = 5
        self.dy = 7
        self.screen = screen

    def play(self, mpx, mpy, w, h):
        r = self.abst(self.x, self.y, mpx, mpy)
        ax = OwnMath.sign(mpx - self.x) * math.pow(mpx - self.x , 2) / (100 * r)
        ay = OwnMath.sign(mpy - self.y) * math.pow(mpy - self.y, 2) / (100 * r)
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
        self.dx += ax - self.dx / 100
        self.dy += ay - self.dy / 100

        x = (self.x + self.dx)
        if x < 0:
            x += w
        elif x > w:
            x -= w

        y = (self.y + self.dy) % self.h
        if y < 0:
            y += h
        elif y > h:
            y -= h

        pygame.draw.circle(screen, (0, 255, 255), (mpx, mpy), 10)

        pygame.draw.rect(screen, (255, 0, 0), (x - 20, y - 20, 40, 40))
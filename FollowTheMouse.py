import pygame
from pygame.locals import *

from MySprite import MySprite
from SpielVerwaltung import SpielVerwaltung
from Events.InputEvents import *

pygame.init()
screen = pygame.display.set_mode((600,600))

Verwaltung = SpielVerwaltung("Test")

clock = pygame.time.Clock()

w, h = pygame.display.get_surface().get_size()

aktuellesKapitel = Verwaltung.KapitelLaden("E-Lehre")

testsprite = MySprite("bernstein.png", (50,50),512,512,5)


go = True
while go:
    screen.fill(Verwaltung.bColor)
    mpx, mpy = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    testsprite.setFrame((clock.get_time()//100)%15)
    testsprite.print(screen)

    #e.animation(screen, Verwaltung.bColor, pygame.time.get_ticks(), 100)

    pygame.display.update()



    clock.tick(30)

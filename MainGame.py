
# -*- encoding: utf-8 -*-
import pygame
from pygame.locals import *
from SpielVerwaltung import SpielVerwaltung

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1500, 1000))

Verwaltung = SpielVerwaltung("Test")

clock = pygame.time.Clock()

w, h = pygame.display.get_surface().get_size()

Verwaltung.KapitelLaden("E-Lehre", clock)


# klick = Klicken((100,100))
go = True
while go:
    screen.fill(Verwaltung.bColor)
    mpx, mpy = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            Verwaltung.aktuelleSzene().playAnimation()

    Verwaltung.draw(screen)


    pygame.display.update()

    clock.tick(30)

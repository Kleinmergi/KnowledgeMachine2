import pygame
from SpielVerwaltung import SpielVerwaltung
from Events.InputEvents import *

pygame.init()
screen = pygame.display.set_mode((600,600))

Verwaltung = SpielVerwaltung("Test")

clock = pygame.time.Clock()

w, h = pygame.display.get_surface().get_size()

aktuellesKapitel = Verwaltung.KapitelLaden("E-Lehre")



go = True
while go:
    screen.fill(Verwaltung.bColor)
    mpx, mpy = pygame.mouse.get_pos()


    #e.animation(screen, Verwaltung.bColor, pygame.time.get_ticks(), 100)

    pygame.display.update()



    clock.tick(30)

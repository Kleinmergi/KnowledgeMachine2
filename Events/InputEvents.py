import math

import pygame

from Events.UIAnimationen import Ring
from OwnDebug import printDebug


def neuesEvent(type, koordinaten, einzugsbereich = (100,100)):
    if type == "Klicken":
        return Klicken(koordinaten, einzugsbereich)
    elif type == "Ziehen":
        return Klicken(koordinaten,einzugsbereich)


def obenLinks(koordinaten: (int, int), einzugsbereich: (int, int)):
    return ((koordinaten[0] + einzugsbereich[0] / 2, koordinaten[1] + einzugsbereich[1] / 2))


class InputEvent:
    def __init__(self, koordinaten: (int, int), einzugsbereich: (int, int)):
        """

        :param (int, int) koordinaten:
        :param (int, int) einzugsbereich:
        """
        self.koordinaten = koordinaten
        self.einzugsbereich = einzugsbereich

    def mouseIn(self):
        mousePos = pygame.mouse.get_pos()
        dx = mousePos[0] - self.koordinaten[0]
        dy = mousePos[1] - self.koordinaten[1]
        return abs(dx) < self.einzugsbereich[0]/2 and abs(dy) < self.einzugsbereich[1]/2

    def sendEvent(self):
        pass

    def show(self, screen):
        pygame.draw.circle(screen, (250,0,0), self.koordinaten, self.einzugsbereich[0])


class Klicken(InputEvent):

    def __init__(self, koordinaten: (int, int), einzugsbereich=(100, 100)):
        """

        :param (int, int) koordinaten:
        """
        super().__init__(koordinaten, einzugsbereich)
        self.ringe = []
        self.surf = pygame.Surface(einzugsbereich)

    def __str__(self):
        return "klicken bei " + self.koordinaten

    def sendEvent(self):
        if self.mouseIn():
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return event
        pass

    def animation(self, screen: pygame.Surface, time, maxR, korrektur=(0,0)):
        """
        Füllen der Liste mit Ringen
        Fall1: Erster Ring bei leerer Liste
        Fall2: Weitere Ringe wenn Ring zuvor mit Radius größer 30
        """
        if self.mouseIn():
            self.surf = pygame.transform.scale(self.surf,(3*maxR, 3*maxR))


            if len(self.ringe) == 0 or self.ringe[len(self.ringe) - 1].r > 30:
                self.ringe.append(Ring(self.koordinaten, 0, time, maxR))
                #printDebug((len(self.ringe), self.ringe[len(self.ringe) - 2].r))

            for ring in self.ringe:
                ring.r = (1+time - ring.t0) / 30
                ring.animation(screen)
                if ring.r > maxR:
                   # printDebug("now")
                    self.ringe.remove(ring)
                    del ring
        else:
            self.surf.fill((0,0,0))
            for ring in self.ringe:
                del ring
            self.ringe.clear()

class Ziehen:

    def __init__(self, koordinaten: (int, int)):
        self.koordinaten = koordinaten
        self.ring = Ring(self.koordinaten, 50, 0)

    def __str__(self):
        return "Ziehen bei " + self.koordinaten

    def addTuble(a, b):
        if len.a != len.b:
            raise ValueError
        c = ()
        for i in range(len(a)):
            c.append(a(i) + b(i))

    def animation(self, screen, time, maxR):
        """
        """
        self.ring.koordinaten = self.addTuble(self.koordinaten, (40 * math.sin(time / 40), 40 * math.cos((time / 40))))

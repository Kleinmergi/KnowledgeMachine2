import math

from Events.UIAnimationen import Ring
from OwnDebug import printDebug

def neuer(type, koordinaten):
    if type == "Klicken":
         return Klicken(koordinaten)
    elif type == "Ziehen":
        return





class Klicken:

    def __init__(self, koordinaten):
        self.koordinaten = koordinaten
        self.ringe = []

    def animation(self, screen, background, time, maxR):
        """
        Füllen der Liste mit Ringen
        Fall1: Erster Ring bei leerer Liste
        Fall2: Weitere Ringe wenn Ring zuvor mit Radius größer 30
        """

        if len(self.ringe) == 0 or self.ringe[len(self.ringe) - 1].r > 30:
            self.ringe.append(Ring(self.koordinaten, 0, time))
            printDebug((len(self.ringe), self.ringe[len(self.ringe) - 2].r))

        for ring in self.ringe:
            ring.r = (time - ring.t0) / 50
            ring.animation(screen, background)
            if ring.r > maxR:
                printDebug("now")
                self.ringe.remove(ring)
                del ring

class Ziehen:

    def __init__(self, koordinaten):
        self.koordinaten = koordinaten
        self.ring = Ring(self.koordinaten, 50, t0)

    def addTuble(a,b):
        if len.a != len.b:
            raise ValueError
        c=()
        for i in range(len(a)):
            c.append(a(i)+b(i))


    def animation(self, screen, background, time, maxR):
        """
        """
        self.ring.koordinaten = self.addTuble(self.koordinaten,(40*math.sin(time/40),40*math.cos((time/40))))




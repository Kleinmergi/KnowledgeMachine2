from Events.UIAnimationen import Ring
from OwnDebug import printDebug

class InputEvents:
    def __init__(self, koordinaten):
        self.koordinaten = koordinaten
        # self.y = y

    def animation(self):
        pass




class Klicken(InputEvents):

    def __init__(self, koordinaten):
        super(Klicken, self).__init__(koordinaten)
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


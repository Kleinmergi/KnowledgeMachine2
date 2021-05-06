import pygame

from OwnDebug import printDebug


class MySprite:

    def __init__(self, image, korrdinaten, width, height, frame0):
        """
        Die Paramater werden von der enstsprechenden JSON über die Szene übergeben
        :param str image: Bildpfad
        :param (float, float) korrdinaten: Koordinaten des oberen linken Bildpunktes
        :param int width: Breite eines Frames
        :param int height: Höhe eines Frames
        :param int frame0: Std. Frame, Beginn der Animationen
        """

        self.setPos(korrdinaten)
        self.setSize(width, height)
        self.frame0 = frame0
        self.frame = frame0
        self.image = pygame.image.load(image)
        self.image.convert()
        self.frames = self.image.get_width() / self.width
        printDebug(self.frames)
        self.rect = pygame.Rect((self.frameToPos(self.frame0), 0),(self.width, self.height))

    def frameToPos(self, frame):
        return self.width * frame

    def setFrame(self, frame):
        if frame <= self.frames:
            self.frame = frame//1
            self.rect.x = self.frameToPos(self.frame)
        else:
            pass

    def setPos(self, koordinaten):
        self.koordinaten = koordinaten

    def setSize(self, width, height):
        self.width = width
        self.height = height

    def playAnimation(self, speed, animation, clock: pygame.time.Clock, time0):
        clock.get_time()

    def print(self, screen: pygame.Surface):
        """
        Gibt den aktuellen Frame des SpriteSheet auf den Screen aus
        :param screen Das pygame display, auf welchen sprite ausgegeben werden soll
        """
        screen.blit(self.image, self.koordinaten, self.rect)


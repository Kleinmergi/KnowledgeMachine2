import pygame
from Events.InputEvents import InputEvent


class MySpriteAnimations:

    def __init__(self, name, korrdinaten, width, height, frame0, event: InputEvent, loops, delay):
        """
        Die Paramater werden von der enstsprechenden JSON über die Szene übergeben
        :param str name: Name der Animation
        :param (float, float) korrdinaten: Koordinaten des oberen linken Bildpunktes
        :param int width: Breite eines Frames
        :param int height: Höhe eines Frames
        :param int frame0: Std. Frame, Beginn der Animationen
        :param int loops: anzahl der animationswiederholungen
        :param int delay: verzögerung der animation
        """
        # Atribute festlegen
        self.name = name
        self.setPos(korrdinaten)
        self.setSize(width, height)
        self.frame0 = frame0
        self.frame = frame0


        # Bild Laden und Skalieren
        image0 = pygame.image.load("Animations/" + self.name + ".png")
        faktor = (self.width / image0.get_size()[1])
        self.image = pygame.transform.scale(pygame.image.load("Animations/" + self.name + ".png"),
                                            (int((faktor * image0.get_size()[0])),
                                             int((faktor * image0.get_size()[1]) // 1)))
        self.image.convert()

        # Anzahl der Frames berechnen und Rahmen festlegen
        self.frames = self.image.get_width() / self.width
        self.rect = pygame.Rect((self.frameToPos(self.frame0), 0), (self.width, self.height))

        # Looper und Playing-Bool für Animationen
        self.looper = 0
        self.loops = loops
        self.delay = delay
        self.playing = False

        # Auslöseevent festlegen
        self.event = event

        #Sound laden
        self.sound = pygame.mixer.Sound("Sounds/" + self.name + ".wav")

    def frameToPos(self, frame):
        return self.width * frame

    def setFrame(self, frame):
        """
        Setze aktuellen Frame
        :param frame: neuer akteueller Frame
        """
        if frame <= self.frames:
            self.frame = frame // 1
            self.rect.x = self.frameToPos(self.frame)
        else:
            pass

    def setPos(self, koordinaten):
        self.koordinaten = koordinaten

    def setSize(self, width, height):
        self.width = width
        self.height = height

    def startAnimation(self):
        """
        Starte animation mit setzen des aktuellen Null-Zeitpunktes
        """
        if self.event.mouseIn():
            self.sound.stop()
            self.eigenZeit = pygame.time.get_ticks()
            self.playing = True
            self.sound.play()
            self.eigenZeit += self.delay*300
            #pygame.mixer.music.load("Sounds/" + self.name + ".wav")
            #pygame.mixer.music.play()
        else:
            self.playing = False
            self.sound.stop()
            #pygame.mixer.stop()

    def playAnimation(self, speed):
        """
        Wächeslt loops-mal Sprite-Frames mit übergebener zeit
        :param speed: Geschwindigkeitsfaktor
        :param loops: Anzahl an wiederholungen
        """

        if self.looper < self.loops and self.playing:
            t = pygame.time.get_ticks() - self.eigenZeit
           # print(self.eigenZeit-self.delay*300)
            k = ((max(0,t) * speed) // 1) % (self.frames)
            self.setFrame(k)
            if k == self.frames-1:
                self.eigenZeit = pygame.time.get_ticks()
                self.looper += 1

        else:
            self.looper = 0
            self.playing = False

    def draw(self, screen: pygame.Surface):
        """
        Gibt den aktuellen Frame des SpriteSheet und die Eventanimation auf den Screen aus
        :param screen Das pygame display, auf welchen sprite ausgegeben werden soll
        """
        self.playAnimation(0.01)
        screen.blit(self.image, self.koordinaten, self.rect)
        if not self.playing:
            self.event.animation(screen, pygame.time.get_ticks(), 100, (0, 50))

        # self.event.show(screen)

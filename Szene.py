import pygame.time
from Animations.MySpriteAnimations import MySpriteAnimations
from Events import InputEvents
from Events.InputEvents import neuesEvent
from OwnDebug import printDebug


class Szene:
    def __init__(self, infos, clock: pygame.time.Clock):
        self.infos = infos
        self.szenenname = infos["Name"]
        self.setInterakationen()
        self.clock = clock



    def setInterakationen(self):
        """Anlegen eines Interaktionen Dictionary der form
            key: [Event, sound, MySprite)
        """
        self.Interaktionen = {}
        for interaktion in self.infos["Iteraktionen"]:
            koordinaten = (interaktion['Koordinaten']['x'], interaktion['Koordinaten']['y'])
            abmessung = (interaktion['Koordinaten']['w'], interaktion['Koordinaten']['h'])
            spriteInfo = interaktion["Sprite"];
            #!!sounds noch einbinden
            self.Interaktionen[interaktion["Name"]] = MySpriteAnimations(spriteInfo["File"],
                                                                          koordinaten,
                                                                          spriteInfo["w"],
                                                                          spriteInfo["h"],
                                                                          spriteInfo["Frame0"],
                                                                          neuesEvent(interaktion["Typ"],
                                                                                     InputEvents.obenLinks(koordinaten, abmessung),
                                                                                     abmessung),
                                                                         spriteInfo["loop"],
                                                                         spriteInfo["delay"]
                                                                         )

        printDebug(self.Interaktionen)

    def drawInteraktionen(self, screen):
        for key in self.Interaktionen:
            self.Interaktionen[key].draw(screen)

    def playAnimation(self):
        #self.Interaktionen[interaktion].playAnimation(-0.01,0, self.clock, self.clock.get_time())
        for key in self.Interaktionen:
            self.Interaktionen[key].startAnimation()

    def printIteraktionen(self):
        out = ""
        for interaktion in self.infos["Iteraktionen"]:
            out += interaktion["Name"]
        return out

    def __str__(self):
        return self.szenenname

from Events import InputEvents
from Events.InputEvents import neuesEvent
from OwnDebug import printDebug


class Szene:
    def __init__(self, szenenname, infos):
        self.selfszenenname = szenenname;
        self.infos = infos
        self.parseInfo()


    def parseInfo(self):
        self.Interaktionen = {}
        for interaktion in self.infos["Iteraktionen"]:
            #printDebug(interaktion)
            koordinaten = (interaktion['Koordinaten']['x'], interaktion['Koordinaten']['y'])
            self.Interaktionen[interaktion["Name"]] = [neuesEvent(interaktion["Typ"], koordinaten), interaktion["Sounds"], interaktion["Sprites"]]
        printDebug(self.Interaktionen)



    def printIteraktionen(self):
        out = ""
        for interaktion in self.infos["Iteraktionen"]:
            out += interaktion["Name"]
        return out

    def __str__(self):
        return self.selfszenenname
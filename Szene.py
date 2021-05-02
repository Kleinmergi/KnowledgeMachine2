
from Events import InputEvents
from Events.InputEvents import neuesEvent
from OwnDebug import printDebug


class Szene:
    def __init__(self, szenenname, infos):
        self.selfszenenname = szenenname;
        self.infos = infos
        self.parseInfo()


    def parseInfo(self):
        self.Interaktionen = []
        for interaktion in self.infos["Iteraktionen"]:
            self.Interaktionen.append(neuesEvent("interaktion"))
        printDebug(self.Interaktionen)



    def printIteraktionen(self):
        out = ""
        for interaktion in self.infos["Iteraktionen"]:
            out += interaktion["name"]
        return out

    def __str__(self):
        return self.selfszenenname
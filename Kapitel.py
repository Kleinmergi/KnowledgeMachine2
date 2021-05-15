import json
from OwnDebug import *
from Szene import Szene




class Kapitel:
    def __init__(self, Kapitelname, clock):
        self.Kapitelname = Kapitelname;
        self.config = self.loadJson(Kapitelname)
        self.szenen = {}
        self.aktuelleSzene = 1
        self.clock = clock

        for szene in self.config["Scenen"]:
            self.szenen[szene["S_ID"]] = Szene(szene, self.clock)
        for key, value in self.szenen.items():
            printDebug(str(key) +","+str(value)+"\t"+ value.printIteraktionen())


    def __str__(self):
        out = self.Kapitelname+"-> "
        for key, value in self.szenen.items():
            out += str(key) + ": " + str(value) + "\t" + value.printIteraktionen()+";"
        return out

    def getAKtuelleSzene(self):
        return self.szenen[self.aktuelleSzene]

    def loadJson(self, szene):
        with open("JSON/"+self.Kapitelname+'.json') as json_file:
            return json.load(json_file)

    def setzeSzene(self, szenenID):
        self.aktuelleSzene = szenenID

    def NextSzene(self):
        if(self.aktuelleSzene+1 < len(self.szenen)):
            self.setzeSzene(self.aktuelleSzene+1)

    def PrevSzene(self):
        if(self.aktuelleSzene >0 ):
            self.setzeSzene(self.aktuelleSzene-1)

    def testplay(self):
        self.szenen[1].playAnimation("Bernstein")

    def draw(self, screen):
        for key in self.szenen:
            self.szenen[key].drawInteraktionen(screen)
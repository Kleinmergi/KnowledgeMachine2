import json
from OwnDebug import *
from Szene import Szene


class Kapitel:
    def __init__(self, Kapitelname):
        self.Kapitelname = Kapitelname;
        self.config = self.loadJson(Kapitelname)
        self.szenen = {}
        for szene in self.config["Scenen"]:
            self.szenen[szene["S_ID"]] = Szene(szene["Name"])
        printDebug(self.szenen)


    def loadJson(self, szene):
        with open(self.Kapitelname+'.json') as json_file:
            return json.load(json_file)


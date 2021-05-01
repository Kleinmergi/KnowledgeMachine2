import json

class Szene:
    def __init__(self, szenenname, infos):
        self.selfszenenname = szenenname;
        self.infos = infos


    def parseInfo(self):
        self.Interaktionen = []
        for interaktion in self.infos["Iteraktionen"]:



    def printIteraktionen(self):
        out = ""
        for interaktion in self.infos["Iteraktionen"]:
            out += interaktion["name"]
        return out

    def __str__(self):
        return self.selfszenenname
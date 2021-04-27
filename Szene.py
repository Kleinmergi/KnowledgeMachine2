import json

class Szene:
    def __init__(self, szenenname):
        self.selfszenenname = szenenname;
        self.config = self.loadJson(szenenname)

    def loadJson(self, szene):
        with open(szene+'.json') as json_file:
            return json.load(json_file)


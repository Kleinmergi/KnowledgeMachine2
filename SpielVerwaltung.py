from Kapitel import Kapitel
from OwnDebug import printDebug
from Szene import Szene
from UI.UI import MyUI


class SpielVerwaltung:
    instance = None

    def __new__ (cls, name):
        if cls.instance is None:
            cls.MyUi = MyUI()
            cls.instance = object.__new__(cls)
        return cls.instance

    def __call__(cls, *args, **kwargs):
        print(cls.aktuellesKapitel)

    """
    bis her Szene und Kapitel gemischt, bald ordnen!!!
    """
    def draw(cls, screen):
        cls.aktuellesKapitel.draw(screen)
        cls.MyUi.draw(screen, 50);

    def aktuelleSzene(cls):
        return cls.aktuellesKapitel.getAKtuelleSzene()

    def testPlay(cls):
        cls.aktuellesKapitel.testplay()

    def KapitelLaden(cls, name, clock):
        cls.aktuellesKapitel = Kapitel(name, clock)
        cls.jsonFarbe = cls.aktuellesKapitel.config["Farbe"]
        cls.bColor = (cls.jsonFarbe[0], cls.jsonFarbe[1], cls.jsonFarbe[2])
        cls.SzenenWechsel(1)
        cls.MyUi.KapitelLaden(name)

    def SzenenWechsel(cls, SzenenId):
        cls.aktuellesKapitel.setzeSzene(SzenenId)
        cls.MyUi.SzeneLaden(cls.aktuellesKapitel.getAKtuelleSzene().__str__())


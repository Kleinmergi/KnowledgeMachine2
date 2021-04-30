from Szene import Szene


class SpielVerwaltung:
    instance = None

    def __new__ (cls, name):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def __call__(cls, *args, **kwargs):
        print(cls.aktuellesKapitel)

    """
    bis her Szene und Kapitel gemischt, bald ordnen!!!
    """

    def setzeEvents(cls):
        cls.aktuellesKapitel.config

    def KapitelLaden(cls, name):
        cls.aktuellesKapitel = Szene(name)
        cls.jsonFarbe = cls.aktuellesKapitel.config["Farbe"]
        cls.bColor = (cls.jsonFarbe[0], cls.jsonFarbe[1], cls.jsonFarbe[2])


import pygame


class MyUI:
    def __init__(self):
        self.UISurface = pygame.Surface(pygame.display.get_surface().get_size())
        self.UISurface.set_colorkey((0, 0, 0))
        self.KapitelLogo = pygame.image.load("UI/Hauptmenu.png")
        self.Szene = ""
        pygame.font.init()
        self.Schriften = pygame.font.SysFont('Comic Sam', 30)
        self.SzenenTitel = ""

    def KapitelLaden(self, name):
        self.KapitelLogo = pygame.image.load("UI/" + name + ".png")

    def SzeneLaden(self, name):
        self.SzenenTitel = name

    def draw(self, screen: pygame.Surface, frame):
        # Rahmen
        Size = pygame.display.get_surface().get_size()
        pygame.draw.rect(self.UISurface, (150, 150, 150), pygame.Rect((0, 0), Size))
        pygame.draw.rect(self.UISurface, (0, 0, 0),
                         pygame.Rect((frame, frame), (Size[0] - 2 * frame, Size[1] - 2 * frame)))
        # Szenentitel
        Titelleiste = self.Schriften.render(self.SzenenTitel, False, (55, 55, 55))
        self.UISurface.blit(Titelleiste, (100, 100))

        # Kaptielbild
        self.UISurface.blit(pygame.transform.scale(self.KapitelLogo, (128, 64)), (0, 0))

        # Layer einbinden
        screen.blit(self.UISurface, (0, 0))

import pygame

class Ring:
    def __init__(self, koordinaten, r, t0, Rmax):
        self.r = int(r+1)
        self.koordinaten = (koordinaten[0]-Rmax, koordinaten[1]-Rmax)
        self.t0 = t0;
        self.Rmax = Rmax
        self.malf =  pygame.Surface((2*self.Rmax,2*self.Rmax))
        self.malf.set_colorkey((0, 0, 0))


    def colorAdd(self, c1, c2):
        return (min(255, (c1[0] + c2[0])), min(255, (c1[1] + c2[1])), min(255, (c1[2] + c2[2])))

    def animation(self, screen:pygame.Surface):
        self.malf.set_alpha(self.Rmax / (self.r + 1) * 15)
        pygame.draw.circle(self.malf, (255, 255, 255), (self.Rmax, self.Rmax), (self.r))
        pygame.draw.circle(self.malf, (0, 0, 0), (self.Rmax, self.Rmax), (self.r - 5 ))
        screen.blit(self.malf, self.koordinaten)
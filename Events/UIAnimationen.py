import pygame




class Ring:
    def __init__(self, koordinaten, r, t0):
        self.r = r
        self.koordinaten = koordinaten
        self.t0 = t0;

    def colorAdd(self, c1, c2):
        return (min(255, (c1[0] + c2[0])), min(255, (c1[1] + c2[1])), min(255, (c1[2] + c2[2])))

    def animation(self, screen, background):
        d=15
        for j in range(d):
            k = abs(max(0, j - self.r / 100))  # (d/2-abs(d-j))#/ math.sqrt(r + 1)
            # print(k)
            pygame.draw.circle(screen, self.colorAdd((k, k, k), background), self.koordinaten, (self.r - j))
            pygame.draw.circle(screen, background, self.koordinaten, (self.r - d + 1))

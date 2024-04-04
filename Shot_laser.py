import pygame


class ShotLaser:
    color = (255, 0, 0)
    width = 10
    height = 10

    def __init__(self, screen, xvalue, yvalue, speedx, speedy):
        self.screen = screen
        self.xvalue = xvalue
        self.yvalue = yvalue
        self.speedx = speedx*2
        self.speedy = speedy*2

    def update(self):
        self.xvalue += self.speedx
        self.yvalue += self.speedy

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.xvalue, self.yvalue, self.width, self.height))

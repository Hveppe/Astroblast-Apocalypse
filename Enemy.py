import pygame


class EnemyClass:
    width = 20
    height = 20
    colour = (255, 0, 0)

    def __init__(self, screen, xvalue, yvalue, speedx, speedy):
        self.x = xvalue
        self.y = yvalue
        self.speedx = speedx
        self.speedy = speedy
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))

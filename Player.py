import pygame


class PlayerClass:
    colour = (255, 255, 255)
    width = 20
    height = 20

    def __init__(self, screen, xvalue, yvalue):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))

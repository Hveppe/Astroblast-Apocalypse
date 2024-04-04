import pygame


class PlayerClass:
    colour = (255, 255, 255)
    width = 40
    height = 40
    xmove = 0
    ymove = 0
    movespeed = 1

    def __init__(self, screen, xvalue, yvalue):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue

    def update(self):
        self.x += self.xmove
        self.y += self.ymove

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))

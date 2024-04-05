import pygame


class PlayerClass:
    colour = (255, 255, 255)
    width = 40
    height = 40
    xmove = 0
    ymove = 0
    movespeed = 10

    def __init__(self, screen, xvalue, yvalue):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue

        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()

    def update(self):
        self.x += self.xmove
        self.y += self.ymove

        if self.x+self.width > self.screenwidth:
            self.x = self.screenwidth - self.width
        if self.y+self.height > self.screenheight:
            self.y = self.screenheight - self.height
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))

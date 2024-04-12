# Spillet er lavet af Hveppe

import pygame


class PlayerClass:
    width = 40
    height = 40
    xmove = 0
    ymove = 0
    movespeed = 10

    def __init__(self, screen, xvalue, yvalue, picture):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue

        self.picture = pygame.transform.scale(picture, (self.width, self.height))

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
        self.screen.blit(self.picture, (self.x, self.y))

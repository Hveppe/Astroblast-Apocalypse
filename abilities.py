# Spillet er lavet af Hveppe

import pygame


class ShotLaser:
    color = (0, 0, 255)
    width = 10
    height = 10
    speedx = 0
    speedy = 0

    def __init__(self, screen, xvalue, yvalue, last_move):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue

        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()

        self.hitwall = False

        self.last_move = last_move

        if self.last_move == 'up':
            self.speedy -= 15
        if self.last_move == 'down':
            self.speedy += 15
        if self.last_move == 'left':
            self.speedx -= 15
        if self.last_move == 'right':
            self.speedx += 15

    def update(self):
        self.x += self.speedx
        self.y += self.speedy

        if (self.x + self.width > self.screenwidth or self.y + self.height > self.screenheight or
                self.x < 0 or self.y < 0):
            self.hitwall = True

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))


class LayMine:
    color = (100, 100, 100)
    speedx = 0
    speedy = 0
    width = 10
    height = 10
    radius = 5

    def __init__(self, screen, xvalue, yvalue):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue

        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()

        self.hitwall = False

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


TODO: 'gør collision med shield bedre'


class Shield:
    color = (0, 0, 255, 127)
    radius = 70

    def __init__(self, screen, xvalue, yvalue):
        self.x = xvalue
        self.y = yvalue

        self.screen = screen

    def update(self, player):
        self.x = player.x + player.width/2
        self.y = player.y + player.height/2

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius, 2)

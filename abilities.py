# Spillet er lavet af Hveppe

import pygame
from Define import scalar


class ShotLaser:
    width = 10*scalar.scalar
    height = 10*scalar.scalar
    speedx = 0
    speedy = 0

    def __init__(self, screen, xvalue, yvalue, last_move, color):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue
        self.color = color

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
    speedx = 0
    speedy = 0
    width = 12*scalar.scalar
    height = 12*scalar.scalar
    radius = 6

    def __init__(self, screen, xvalue, yvalue, picture):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue

        picture = pygame.transform.scale(picture, (self.width, self.height))
        self.picture = picture

        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()

        self.hitwall = False

    def draw(self):
        self.screen.blit(self.picture, (self.x-self.width/2, self.y-self.height/2))

    def draw_debug(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), self.radius, 2)


class Shield:
    color = (0, 0, 255)
    radius = 70*scalar.scalar

    def __init__(self, screen, xvalue, yvalue):
        self.x = xvalue
        self.y = yvalue

        self.screen = screen

    def update(self, player):
        self.x = player.x + player.width/2
        self.y = player.y + player.height/2

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius, 2)

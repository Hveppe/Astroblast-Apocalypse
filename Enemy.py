import pygame
import math


class EnemyClass:
    width = 30
    height = 30

    def __init__(self, screen, xvalue, yvalue, speedx, speedy, colour):
        self.x = xvalue
        self.y = yvalue
        self.speedx = speedx
        self.speedy = speedy
        self.screen = screen
        self.colour = colour

        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()

    def update(self):
        self.x += self.speedx
        self.y += self.speedy

        if self.x + self.width > self.screenwidth or self.x < 0:
            self.speedx = -self.speedx

        if self.y + self.height > self.screenheight or self.y < 0:
            self.speedy = -self.speedy

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))


class HeavyEnemyClass:
    width = 40
    height = 40
    lives = 3
    dead = False
    colour = (139, 0, 0)

    def __init__(self, screen, xvalue, yvalue, speedx, speedy):
        self.x = xvalue
        self.y = yvalue
        self.speedx = speedx
        self.speedy = speedy
        self.screen = screen

        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()

    def update(self):
        self.x += self.speedx
        self.y += self.speedy

        if self.x + self.width > self.screenwidth or self.x < 0:
            self.speedx = -self.speedx

        if self.y + self.height > self.screenheight or self.y < 0:
            self.speedy = -self.speedy

        if self.lives <= 0:
            self.dead = True

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))


class HommingEnemyClass:
    width = 10
    height = 10

    def __init__(self, screen, xvalue, yvalue, speedx, speedy, radius, color):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue
        self.speedx = speedx
        self.speedy = speedy
        self.radius = radius
        self.color = color

    def update(self, player):
        distancex = player.x - self.x
        distancey = player.y - self.y

        distance = math.sqrt(distancex ** 2 + distancey ** 2)

        if distance > 0:
            distancex /= distance
            distancey /= distance

        self.x += distancex * self.speedx
        self.y += distancey * self.speedy

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

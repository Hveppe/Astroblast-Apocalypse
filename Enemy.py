# Spillet er lavet af Hveppe

import pygame
import math


class EnemyClass:
    width = 40
    height = 40

    def __init__(self, screen, xvalue, yvalue, speedx, speedy, colour, picture):
        self.x = xvalue
        self.y = yvalue
        self.speedx = speedx
        self.speedy = speedy
        self.screen = screen
        self.colour = colour

        picture = pygame.transform.scale(picture, (self.width, self.height))
        self.picture = picture

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
        picture_rect = self.picture.get_rect(topleft=(self.x, self.y))
        self.screen.blit(self.picture, picture_rect.topleft)

    def draw_debug(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.width, self.height), 2)


class HeavyEnemyClass:
    width = 60
    height = 60
    lives = 3
    dead = False
    colour = (139, 0, 0)

    def __init__(self, screen, xvalue, yvalue, speedx, speedy, picture):
        self.x = xvalue
        self.y = yvalue
        self.speedx = speedx
        self.speedy = speedy
        self.screen = screen

        picture = pygame.transform.scale(picture, (self.width, self.height))
        self.picture = picture

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
        picture_rect = self.picture.get_rect(topleft=(self.x, self.y))
        self.screen.blit(self.picture, picture_rect.topleft)

    def draw_debug(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.width, self.height), 2)


class HommingEnemyClass:
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

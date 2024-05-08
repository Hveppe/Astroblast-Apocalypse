# Spillet er lavet af Hveppe

import pygame
import math


class EnemyClass:
    width = 40
    height = 40
    dead = False
    timeofdeath = None

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
        if self.dead is False:
            self.x += self.speedx
            self.y += self.speedy
        else:
            pass

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
    timeofdeath = None
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
        if self.dead is False:
            self.x += self.speedx
            self.y += self.speedy

            if self.x + self.width > self.screenwidth or self.x < 0:
                self.speedx = -self.speedx

            if self.y + self.height > self.screenheight or self.y < 0:
                self.speedy = -self.speedy
        else:
            pass

    def draw(self):
        picture_rect = self.picture.get_rect(topleft=(self.x, self.y))
        self.screen.blit(self.picture, picture_rect.topleft)

    def draw_debug(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.width, self.height), 2)


class HommingEnemyClass:
    width = 50
    height = 50
    dead = False
    timeofdeath = None
    lastangleofmovement = None

    def __init__(self, screen, xvalue, yvalue, speedx, speedy, color, picture):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue
        self.xold = xvalue
        self.yold = yvalue
        self.speedx = speedx
        self.speedy = speedy
        self.color = color

        picture = pygame.transform.scale(picture, (self.width, self.height))
        self.picture = picture

    def update(self, player):
        if self.dead is False:
            self.xold = self.x
            self.yold = self.y
            distancex = player.x - self.x
            distancey = player.y - self.y

            distance = math.sqrt(distancex ** 2 + distancey ** 2)

            if distance > 0:
                distancex /= distance
                distancey /= distance

            self.x += distancex * self.speedx
            self.y += distancey * self.speedy
        else:
            pass

    def draw(self):
        if self.speedy != 0 and self.speedx != 0:
            rotated_image = pygame.transform.rotate(self.picture, self.lastangleofmovement)
            rotated_rect = rotated_image.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
            self.screen.blit(rotated_image, rotated_rect.topleft)
        else:
            angleofmovement = math.degrees(math.atan2(-(self.yold - self.y), self.xold - self.x)) + 90
            rotated_image = pygame.transform.rotate(self.picture, angleofmovement)
            rotated_rect = rotated_image.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
            self.screen.blit(rotated_image, rotated_rect.topleft)
            self.lastangleofmovement = angleofmovement

    def draw_debug(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.width, self.height), 2)

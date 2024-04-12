# Spillet er lavet af Hveppe

import pygame
import math


class PlayerClass:
    width = 62
    height = 64.4
    xmove = 0
    ymove = 0
    movespeed = 10
    last_angle = 0

    def __init__(self, screen, xvalue, yvalue, picture):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue
        self.xold = xvalue
        self.yold = yvalue

        picture = pygame.transform.scale(picture, (self.width, self.height))
        self.picture = picture

        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()

    def update(self):
        self.xold = self.x
        self.yold = self.y
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
        if self.xmove == 0 and self.ymove == 0:
            stillpicture = self.picture.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
            self.screen.blit(self.picture, stillpicture.center)
        else:
            angleofmovement = math.degrees(math.atan2(-(self.yold - self.y), self.xold - self.x)) + 90
            rotated_image = pygame.transform.rotate(self.picture, angleofmovement)
            rotated_rect = rotated_image.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
            self.screen.blit(rotated_image, rotated_rect.center)
# Spillet er lavet af Hveppe

import pygame
import math

from Define import scalar


class PlayerClass:
    xmove = 0
    ymove = 0
    movespeed = 10

    def __init__(self, screen, xvalue, yvalue, picture, damage_picture):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue
        self.xold = xvalue
        self.yold = yvalue
        self.last_angle = 0

        self.width = 60 * scalar.scalar
        self.height = 60 * scalar.scalar

        picture = pygame.transform.scale(picture, (int(self.width), int(self.height)))
        self.picture = picture
        damage_picture = pygame.transform.scale(damage_picture, (int(self.width), int(self.height)))
        self.damage_picture = damage_picture

    def update(self):
        self.xold = self.x
        self.yold = self.y
        self.x += self.xmove
        self.y += self.ymove

        if self.x+self.width > self.screen.get_width():
            self.x = self.screen.get_width() - self.width

        if self.y+self.height > self.screen.get_height():
            self.y = self.screen.get_height() - self.height

        if self.x < 0:
            self.x = 0

        if self.y < 0:
            self.y = 0

    def update_picture(self):
        picture = pygame.transform.scale(self.picture, (int(self.width), int(self.height)))
        self.picture = picture
        damage_picture = pygame.transform.scale(self.damage_picture, (int(self.width), int(self.height)))
        self.damage_picture = damage_picture

    def draw(self, damage):
        if self.xmove == 0 and self.ymove == 0:
            if damage is False:
                rotated_image = pygame.transform.rotate(self.picture, self.last_angle)
                rotated_rect = rotated_image.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
                self.screen.blit(rotated_image, rotated_rect.topleft)
            elif damage is True:
                rotated_image = pygame.transform.rotate(self.damage_picture, self.last_angle)
                rotated_rect = rotated_image.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
                self.screen.blit(rotated_image, rotated_rect.topleft)
        else:
            if damage is False:
                angleofmovement = math.degrees(math.atan2(-(self.yold - self.y), self.xold - self.x)) + 90
                rotated_image = pygame.transform.rotate(self.picture, angleofmovement)
                rotated_rect = rotated_image.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
                self.screen.blit(rotated_image, rotated_rect.topleft)
                self.last_angle = angleofmovement
            elif damage is True:
                angleofmovement = math.degrees(math.atan2(-(self.yold - self.y), self.xold - self.x)) + 90
                rotated_image = pygame.transform.rotate(self.damage_picture, angleofmovement)
                rotated_rect = rotated_image.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
                self.screen.blit(rotated_image, rotated_rect.topleft)
                self.last_angle = angleofmovement

    def draw_debug(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.width, self.height), 2)

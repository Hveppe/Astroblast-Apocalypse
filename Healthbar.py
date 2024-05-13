# Lavet af Hveppe og lidt kode fra anton

import pygame
from Define import White, Red, Green


class HealthBar:
    white = White
    red = Red
    green = Green

    def __init__(self, x, y, width, height, max_hp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        # udrenger hvor mange procent liv man har
        ratio = self.hp / self.max_hp

        # tegner healthbaren
        pygame.draw.rect(surface, self.red, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, self.green, (self.x, self.y, self.width * ratio, self.height))
        pygame.draw.rect(surface, self.white, (self.x, self.y, self.width, self.height), 2)

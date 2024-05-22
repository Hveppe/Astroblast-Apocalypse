# Lavet af Hveppe

import pygame
from Define import White, scalar


class HealthBar:  # skelet af kode var lavet af anton
    white = White

    def __init__(self, x, y, width, height, max_hp, color, emptycolor):
        self.x = x
        self.y = y
        self.width = width*scalar
        self.height = height*scalar
        self.hp = max_hp
        self.max_hp = max_hp
        self.color = color
        self.emptycolor = emptycolor

    def draw(self, surface):
        # udrenger hvor mange procent liv man har
        ratio = self.hp / self.max_hp

        # tegner healthbaren
        pygame.draw.rect(surface, self.emptycolor, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width * ratio, self.height))
        pygame.draw.rect(surface, self.white, (self.x, self.y, self.width, self.height), 2)

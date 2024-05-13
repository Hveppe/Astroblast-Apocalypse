import pygame
from Define import White


class HealthBar:
    color = White

    def __init__(self, x, y, width, height, max_hp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.width * ratio, self.height))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height), 2)

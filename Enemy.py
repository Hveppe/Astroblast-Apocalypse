import pygame


class EnemyClass:
    width = 20
    height = 20

    def __init__(self, xvalue, yvalue, speedx, speedy):
        self.x = xvalue
        self.y = yvalue
        self.speedx = speedx
        self.speedy = speedy

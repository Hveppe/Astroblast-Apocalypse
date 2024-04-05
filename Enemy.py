import pygame


class EnemyClass:
    width = 30
    height = 30
    colour = (255, 0, 0)

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

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))

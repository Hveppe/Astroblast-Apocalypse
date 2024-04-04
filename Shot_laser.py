import pygame


class ShotLaser:
    color = (255, 0, 0)
    width = 10
    height = 10

    def __init__(self, screen, xvalue, yvalue, speedx, speedy):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue
        self.speedx = speedx*2
        self.speedy = speedy*2

        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()

        self.hitwall = False

        if self.speedx == 0 and self.speedy == 0:
            self.speedy = -1

    def update(self):
        self.x += self.speedx
        self.y += self.speedy

        if (self.x + self.width > self.screenwidth or self.y + self.height > self.screenheight or
                self.x < 0 or self.y < 0):
            self.hitwall = True

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

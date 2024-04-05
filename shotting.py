import pygame


class ShotLaser:
    color = (0, 0, 255)
    width = 10
    height = 10
    speedx = 0
    speedy = 0

    def __init__(self, screen, xvalue, yvalue, last_move):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue

        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()

        self.hitwall = False

        self.last_move = last_move

        if self.last_move == 'w':
            self.speedy -= 15
        if self.last_move == 's':
            self.speedy += 15
        if self.last_move == 'a':
            self.speedx -= 15
        if self.last_move == 'd':
            self.speedx += 15

    def update(self):
        self.x += self.speedx
        self.y += self.speedy

        if (self.x + self.width > self.screenwidth or self.y + self.height > self.screenheight or
                self.x < 0 or self.y < 0):
            self.hitwall = True

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))


class LayMine:
    color = (100, 100, 100)
    speedx = 0
    speedy = 0
    width = 10
    height = 10

    def __init__(self, screen, xvalue, yvalue):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue

        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()

        self.hitwall = False

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 5)
import pygame


class AstroidClass:
    color = (187, 188, 188)

    def __init__(self, screen, xvalue, yvalue, speed, radius, direction):
        self.screen = screen
        self.x = xvalue
        self.y = yvalue
        self.radius = radius
        self.speed = speed
        self.direction = direction

        self.width = radius * 2
        self.height = radius * 2

    def move(self):
        if self.direction == 1:
            self.y += self.speed
        if self.direction == 2:
            self.x += self.speed
        if self.direction == 3:
            self.y -= self.speed
        if self.direction == 4:
            self.x -= self.speed

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

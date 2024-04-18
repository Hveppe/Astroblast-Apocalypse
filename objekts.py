# Spillet er lavet af Hveppe

import pygame


class Button:
    def __init__(self, screen, x, y, image):
        self.image = image
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
        self.action = True

    def draw(self):
        self.action = False

        # position af musen
        mus_position = pygame.mouse.get_pos()

        # check om musen er over knappen og om der trykkes på den
        if self.rect.collidepoint(mus_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                self.action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # tegn knappen
        self.screen.blit(self.image, self.rect.topleft)

        return self.action


class Picture:
    def __init__(self, screen, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect.center)


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

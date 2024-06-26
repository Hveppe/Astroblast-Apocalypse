# Spillet er lavet af Hveppe

import pygame


class MouseCursor:
    width = 25
    height = 30

    def __init__(self, screen, picture, picture_clik):
        self.screen = screen
        self.picture = pygame.transform.scale(picture, (self.width, self.height))
        self.picture_clik = pygame.transform.scale(picture_clik, (self.width, self.height))
        self.x, self.y = pygame.mouse.get_pos()

    def update(self):
        self.x, self.y = pygame.mouse.get_pos()

    def update_picture(self):
        self.picture = pygame.transform.scale(self.picture, (self.width, self.height))
        self.picture_clik = pygame.transform.scale(self.picture_clik, (self.width, self.height))

    def draw(self, click):
        if click is False:
            self.screen.blit(self.picture, (self.x-self.width/2, self.y-self.height/2))
        elif click is True:
            self.screen.blit(self.picture_clik, (self.x-self.width/2, self.y-self.height/2))

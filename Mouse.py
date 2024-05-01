import pygame


class MouseCursor:
    width = 20
    height = 20

    def __init__(self, screen, picture, picture_clik):
        self.screen = screen
        self.picture = pygame.transform.scale(picture, (self.width, self.height))
        self.picture_clik = pygame.transform.scale(picture_clik, (self.width, self.height))
        self.pos = None

    def update(self):
        self.pos = pygame.mouse.get_pos()

    def draw(self, click):
        if click is False:
            self.screen.blit(self.picture, self.pos)
        else:
            self.screen.blit(self.picture_clik, self.pos)

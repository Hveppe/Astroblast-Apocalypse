import pygame


class MouseCursor:
    width = 20
    height = 20

    def __init__(self, screen, picture):
        self.screen = screen
        self.picture = pygame.transform.scale(picture, (self.width, self.height))
        self.pos = None

    def update(self):
        self.pos = pygame.mouse.get_pos()

    def draw(self):
        self.screen.blit(self.picture, self.pos)

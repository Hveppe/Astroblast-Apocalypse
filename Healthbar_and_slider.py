# Lavet af Hveppe

import pygame
from Define import White, scalar


class HealthBar:  # skelet af kode var lavet af anton
    white = White

    def __init__(self, x, y, width, height, max_hp, color, emptycolor):
        self.x = x
        self.y = y
        self.width = width*scalar.scalar
        self.height = height*scalar.scalar
        self.hp = max_hp
        self.max_hp = max_hp
        self.color = color
        self.emptycolor = emptycolor

    def draw(self, surface):
        # udrenger hvor mange procent liv man har
        ratio = self.hp / self.max_hp

        # tegner healthbaren
        pygame.draw.rect(surface, self.emptycolor, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width * ratio, self.height))
        pygame.draw.rect(surface, self.white, (self.x, self.y, self.width, self.height), 2)


class Slider:  # slider til forskellige ting
    def __init__(self, width, height, screen, max_number, color_square, color_side, color_slider):
        self.width = width*scalar.scalar
        self.height = height*scalar.scalar
        self.screen = screen
        self.max_number = max_number

        self.color_square = color_square
        self.color_side = color_side
        self.color_slider = color_slider

        self.sliderrect_x = None
        self.return_data = max_number

        self.rect = None

    def draw(self, x, y):
        self.rect = pygame.draw.rect(self.screen, self.color_square, (x, y, self.width-10*scalar.scalar, self.height))

        if self.sliderrect_x is None:
            self.sliderrect_x = x+self.width-10*scalar.scalar

        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.sliderrect_x, u = mouse_pos

                self.return_data = self.return_data = (self.sliderrect_x - x) / (self.width - 10 * scalar.scalar) * self.max_number

        self.rect = pygame.draw.rect(self.screen, self.color_square, (x, y, self.width, self.height))

        pygame.draw.rect(self.screen, self.color_square, (x, y, self.width, self.height))
        pygame.draw.rect(self.screen, self.color_slider, (self.sliderrect_x, y, 10*scalar.scalar, self.height))
        pygame.draw.rect(self.screen, (255, 255, 255), (x-2, y-2, self.width+2,
                                                        self.height+2), 2)

        return self.return_data

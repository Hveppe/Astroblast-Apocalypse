# spil lavet af Hveppe

import pygame


def tekst_render(font, tekst, x, y, screen):
    tekst = font.render(tekst, True, (255, 255, 255))
    screen.blit(tekst, (x, y))

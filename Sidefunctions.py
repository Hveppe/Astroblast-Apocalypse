# spil lavet af Hveppe

import pygame


def tekst_render(font, tekst, destination, screen, color):
    tekst = font.render(tekst, True, color)
    screen.blit(tekst, destination)

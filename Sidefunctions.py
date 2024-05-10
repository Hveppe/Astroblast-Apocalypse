# spil lavet af Hveppe

import pygame


def tekst_render(font, tekst, destination, screen, color, center):
    tekst = font.render(tekst, True, color)
    x, y = destination

    if center is True:
        screen.blit(tekst, (x-tekst.get_width()/2, y))
    elif center is False:
        screen.blit(tekst, destination)

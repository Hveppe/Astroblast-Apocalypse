# spil lavet af Hveppe

import pygame


def tekst_render(font, tekst, destination, screen, color, center):
    tekst = font.render(tekst, True, color)

    if center is True:
        x, y = destination
        screen.blit(tekst, (x-tekst.get_width()/2, y))
    elif center is False:
        screen.blit(tekst, destination)


def explosion_effekt(type_enemy, current, explosion_time, explosion_effeckt, display):
    for enemytype in type_enemy:
        if enemytype.dead is True:
            if current - enemytype.timeofdeath >= explosion_time:
                type_enemy.remove(enemytype)
            else:
                display.blit(pygame.transform.scale(explosion_effeckt,
                                                    (enemytype.width + enemytype.width / 2,
                                                     enemytype.height + enemytype.width / 2)),
                             (enemytype.x - enemytype.width / 2 / 2, enemytype.y - enemytype.width / 2 / 2))
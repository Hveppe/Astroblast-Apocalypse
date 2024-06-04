# spil lavet af Hveppe

from collisioncheck_functioner import collisionchecker, collisionchecker_circle, collisionchecker_circle_square
import pygame
import time
import random


def tekst_render(font, tekst, destination, screen, color, center):
    tekst = font.render(tekst, True, color)

    if center is True:
        x, y = destination
        screen.blit(tekst, (x-tekst.get_width()/2, y))
    elif center is False:
        screen.blit(tekst, destination)
    elif center is None:
        x, y = destination
        screen.blit(tekst, (x-tekst.get_width(), y))


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


def tint_image(image, tint_color):
    tinted_image = image.copy()
    tint = pygame.Surface(image.get_size())
    tint.fill(tint_color)
    tinted_image.blit(tint, (0, 0), special_flags=pygame.BLEND_MULT)
    return tinted_image


def taken_damage():
    return True, time.time()


def reset(lasershot, mineshot, fjender, heavyfjender, mineswepperfjender, hommingfjender, astroids, player, variabler,
          screenwith, screenheight):
    # Clear lister
    lasershot.clear()
    mineshot.clear()
    fjender.clear()
    heavyfjender.clear()
    mineswepperfjender.clear()
    hommingfjender.clear()
    astroids.clear()

    # Reset af player
    player.xmove = 0
    player.ymove = 0
    player.x = screenwith/2-player.width/2
    player.y = screenheight/2-player.height/2

    # Reset af variabler
    variabler.reset()
    variabler.wave -= 1
    variabler.antalfjender -= 2


def spawn_enemy(enemylist, klasse, player, screenwith, screenheight, *args):
    fjende_spawn = True
    new_enemy = klasse(*args)
    while fjende_spawn:
        if collisionchecker(new_enemy, player):
            new_enemy.x = random.randint(0, int(round(screenwith-new_enemy.width, 0)))
            new_enemy.y = random.randint(0, int(round(screenheight-new_enemy.height, 0)))
        else:
            enemylist.append(new_enemy)
            fjende_spawn = False

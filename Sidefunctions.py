# spil lavet af Hveppe

import pygame
import time


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
    variabler.ArsenalMines = 5
    variabler.lives = 5
    variabler.wavelives = 4
    variabler.wave = 1
    player.x = screenwith / 2 - 20
    player.y = screenheight - 100
    variabler.shotting = False
    variabler.shield_up = False
    variabler.shield_charge = 100
    variabler.last_draintime = None

    # reset af fjender
    variabler.antalfjender = 0
    variabler.waveheavyspawn = 5
    variabler.wavemineswepperspawn = 6
    variabler.wavehommingspawn = 7
    variabler.antalfjenderheavy = 0
    variabler.antalfjenderhomming = 0
    variabler.antalfjendermineswpper = 0

# importer fra andre python filer
from Player import PlayerClass
from Shot_laser import ShotLaser
from Enemy import EnemyClass

# importer libaries
import random
import pygame

pygame.init()

# opsætting af skærm
screenwith, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((screenwith, screenheight))


def collisionchecker(firstobject, seconobject):
    if (firstobject.x + firstobject.width > seconobject.x and
            firstobject.x < seconobject.x + seconobject.width and
            firstobject.y + firstobject.height > seconobject.y and
            firstobject.y < seconobject.y + seconobject.height):
        return True
    return False

# laver lister til classer der skal havde flere af gangen på skærmen
Lasershot = []
Fjender = []

# laver player
player = PlayerClass(screen=display, xvalue=screenwith/2-20, yvalue=screenheight-100)

gamerunning = True
lastmove = 'w'
antalfjender = 10

clock = pygame.time.Clock()

for i in range(antalfjender):
    Fjender.append(EnemyClass(screen=display, xvalue=random.randint(0, screenwith-10),
                              yvalue=random.randint(0, screenheight-150), speedx=10, speedy=10))

while gamerunning:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            gamerunning = False

        # controls til PlayerClass
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                lastmove = 'w'
            if event.key == pygame.K_DOWN:
                lastmove = 's'
            if event.key == pygame.K_LEFT:
                lastmove = 'a'
            if event.key == pygame.K_RIGHT:
                lastmove = 'd'

            if event.key == pygame.K_w:
                player.ymove -= player.movespeed
                lastmove = 'w'
            if event.key == pygame.K_s:
                player.ymove += player.movespeed
                lastmove = 's'
            if event.key == pygame.K_d:
                player.xmove += player.movespeed
                lastmove = 'd'
            if event.key == pygame.K_a:
                player.xmove -= player.movespeed
                lastmove = 'a'
            if event.key == pygame.K_SPACE:
                Lasershot.append(ShotLaser(screen=display, xvalue=player.x + player.width / 2,
                                           yvalue=player.y + player.height / 2,
                                           speedx=player.xmove, speedy=player.ymove, last_move=lastmove))
        # Bruges til at modvirker controls
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.ymove += player.movespeed
            if event.key == pygame.K_s:
                player.ymove -= player.movespeed
            if event.key == pygame.K_d:
                player.xmove -= player.movespeed
            if event.key == pygame.K_a:
                player.xmove += player.movespeed

    # Farver baggrund
    display.fill((0, 0, 0))

    # Tegner player
    player.draw()
    player.update()

    for lasershot in Lasershot:
        lasershot.draw()
        lasershot.update()

        # fjerner laserne når de rammer kanterne af skærmen
        if lasershot.hitwall is True:
            Lasershot.remove(lasershot)

    for EnemyClass in Fjender:
        EnemyClass.draw()

        for lasershot in Lasershot:
            if collisionchecker(EnemyClass, lasershot):
                Lasershot.remove(lasershot)
                Fjender.remove(EnemyClass)

    # Updater display
    pygame.display.flip()

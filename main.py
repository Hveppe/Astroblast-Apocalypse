# importer fra andre python filer
from Player import PlayerClass
from shotting import ShotLaser, LayMine
from Enemy import EnemyClass

# importer libaries
import random
import pygame

pygame.init()
pygame.font.init()

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
Mineshot = []
Fjender = []

# laver player
player = PlayerClass(screen=display, xvalue=screenwith/2-20, yvalue=screenheight-100)

gamerunning = True
lastmove = 'w'
antalfjender = 2
wave = 1
lives = 5
minepoint = 0

# Antal miner til rådighed
ArsenalMines = 5

clock = pygame.time.Clock()

# Fonts til text
Font = pygame.font.Font(None, 36)
Fontbig = pygame.font.Font(None, 100)

for i in range(antalfjender):
    enemy = EnemyClass(screen=display, xvalue=random.randint(0, screenwith - 10),
                       yvalue=random.randint(0, screenheight - 150), speedx=random.randint(1, 10),
                       speedy=random.randint(1, 10))
    Fjender.append(enemy)

while gamerunning:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            gamerunning = False

        # controls til PlayerClass
        if event.type == pygame.KEYDOWN:

            # Kode til at kontroler våben
            if event.key == pygame.K_UP:
                lastmove = 'w'
                Lasershot.append(ShotLaser(screen=display, xvalue=player.x + player.width / 2,
                                           yvalue=player.y + player.height / 2, last_move=lastmove))
            if event.key == pygame.K_DOWN:
                lastmove = 's'
                Lasershot.append(ShotLaser(screen=display, xvalue=player.x + player.width / 2,
                                           yvalue=player.y + player.height / 2, last_move=lastmove))
            if event.key == pygame.K_LEFT:
                lastmove = 'a'
                Lasershot.append(ShotLaser(screen=display, xvalue=player.x + player.width / 2,
                                           yvalue=player.y + player.height / 2, last_move=lastmove))
            if event.key == pygame.K_RIGHT:
                lastmove = 'd'
                Lasershot.append(ShotLaser(screen=display, xvalue=player.x + player.width / 2,
                                           yvalue=player.y + player.height / 2, last_move=lastmove))
            if event.key == pygame.K_SPACE:
                if ArsenalMines > 0:
                    ArsenalMines -= 1
                    Mineshot.append(LayMine(screen=display, xvalue=player.x + player.width / 2,
                                            yvalue=player.y + player.height / 2, ))

            # Bevægelse af player
            if event.key == pygame.K_w:
                player.ymove -= player.movespeed
            if event.key == pygame.K_s:
                player.ymove += player.movespeed
            if event.key == pygame.K_d:
                player.xmove += player.movespeed
            if event.key == pygame.K_a:
                player.xmove -= player.movespeed

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

    for Mine in Mineshot:
        Mine.draw()

        if Mine.hitwall is True:
            Mineshot.remove(Mine)

    for enemy in Fjender:
        enemy.draw()
        enemy.update()

        if collisionchecker(player, enemy):
            Fjender.remove(enemy)
            lives -= 1

        for lasershot in Lasershot:
            if collisionchecker(enemy, lasershot):
                Lasershot.remove(lasershot)
                minepoint += 1

                try:
                    Fjender.remove(enemy)
                except ValueError:
                    pass

        for Mine in Mineshot:
            if collisionchecker(enemy, Mine):
                Mineshot.remove(Mine)

                try:
                    Fjender.remove(enemy)
                except ValueError:
                    pass

    if len(Fjender) == 0:
        wave += 1
        antalfjender += 2
        for i in range(antalfjender):
            new_enemy = EnemyClass(screen=display, xvalue=random.randint(0, screenwith - 10),
                                   yvalue=random.randint(0, screenheight - 10), speedx=random.randint(1, 10),
                                   speedy=random.randint(1, 10))
            Fjender.append(new_enemy)

    if minepoint > 10:
        ArsenalMines += 1
        minepoint = 0

    livestext = Font.render(f'Lives: {lives}', True, (255, 255, 255))
    display.blit(livestext, (screenwith-160, 10))

    pointstext = Font.render(f'Wave: {wave}', True, (255, 255, 255))
    display.blit(pointstext, (10, 10))

    minetext = Font.render(f'Mine: {ArsenalMines}', True, (255, 255, 255))
    display.blit(minetext, (10, 50))

    # Updater display
    pygame.display.flip()

    if lives <= 0:
        gameover = True

        while gameover:
            clock.tick(60)

            # Farver baggrund
            display.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamerunning = False
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gamerunning = False
                        gameover = False
                    elif event.key == pygame.K_r:
                        gameover = False
                        Lasershot.clear()
                        Mineshot.clear()
                        Fjender.clear()
                        player.xmove = 0
                        player.ymove = 0
                        lives = 5
                        antalfjender = 0
                        wave = 1
                        player.x = screenwith / 2 - 20
                        player.y = screenheight - 100

            gameovertext = Fontbig.render(f'GAME OVER', True, (255, 255, 255))
            display.blit(gameovertext, (screenwith/2 - 200, screenheight / 2 - 200))

            gameovertext = Font.render(f'WAVE: {wave}', True, (255, 255, 255))
            display.blit(gameovertext, (screenwith/2 - 50, screenheight / 2 - 100))

            gameovertext = Font.render('Tryk R for at starte igen', True, (255, 255, 255))
            display.blit(gameovertext, (screenwith/2 - 100, screenheight / 2))

            pygame.display.flip()

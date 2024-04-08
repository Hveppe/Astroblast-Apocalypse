# importer fra andre python filer
import time

from Player import PlayerClass
from shotting import ShotLaser, LayMine
from Enemy import EnemyClass, HeavyEnemyClass
from objekts import AstroidClass

# importer libaries
import random
import pygame
import shelve
import math

# starter pygame og pygame font
pygame.init()
pygame.font.init()

# opsætting af skærm og angiver et navn til programet
screenwith, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((screenwith, screenheight))
pygame.display.set_caption("GAME")

gameimagepng = pygame.image.load('Image/gameimage.png').convert()
pygame.display.set_icon(gameimagepng)

# lyde til spillet
lasersound = pygame.mixer.Sound('sound/laser-gun-81720.wav')
mineplacesound = pygame.mixer.Sound('sound/place-100513.wav')
enemydeadsound = pygame.mixer.Sound('sound/big explosion.wav')
gameoversound = pygame.mixer.Sound('sound/game-over-160612.wav')


def collisionchecker(firstobject, seconobject):
    if (firstobject.x + firstobject.width > seconobject.x and
            firstobject.x < seconobject.x + seconobject.width and
            firstobject.y + firstobject.height > seconobject.y and
            firstobject.y < seconobject.y + seconobject.height):
        return True
    return False


def collisionchecker_circle_square(circle, square):
    # Finder afstanden mellem det tæteste punkt mellem square og circle
    closest_x = max(square.x, min(circle.x, square.x + square.width))
    closest_y = max(square.y, min(circle.y, square.y + square.height))

    distance = math.sqrt((circle.x - closest_x) ** 2 + (circle.y - closest_y) ** 2)

    # Checker om distancen er mindre eller det samme som radius
    if distance <= circle.radius:
        return True
    return False


thing = False

# Laver mousecursor usynlig
pygame.mouse.set_visible(False)

# laver lister til classer der skal havde flere af gangen på skærmen
Lasershot = []
Mineshot = []
Fjender = []
MineswepperFjender = []
HeavyFjender = []
Astroids = []

# laver player
player = PlayerClass(screen=display, xvalue=screenwith/2-20, yvalue=screenheight-100)

# variabler
gamerunning = True
lastmove = 'w'
antalfjender = 2
antalfjenderheavy = 0
antalfjendermineswpper = 0
wave = 1
waveheavyspawn = 5
wavemineswepperspawn = 5
lives = 5
wavelives = 4
minepoint = 0
fjende_spawn = False

# delay til laser
delaylaser = 0.2
last_time_shot = 0

# laver shelve til at gemme highscore
d = shelve.open('highscore')

try:
    highscore = d['highscore']
except ValueError or TypeError:
    highscore = 0

# Antal miner til rådighed
ArsenalMines = 5

# Opsætter clock
clock = pygame.time.Clock()

# Fonts til text
Font = pygame.font.Font(None, 36)
Fontbig = pygame.font.Font(None, 100)

for i in range(antalfjender):
    fjende_spawn = True
    while fjende_spawn:
        enemy = EnemyClass(screen=display, xvalue=random.randint(0, screenwith - 10),
                           yvalue=random.randint(0, screenheight - 150), speedx=random.randint(1, 10),
                           speedy=random.randint(1, 10), colour=(255, 0, 0))
        if collisionchecker(enemy, player):
            enemy.x = random.randint(0, screenwith - 10)
            enemy.y = random.randint(0, screenheight - 150)
        else:
            Fjender.append(enemy)
            fjende_spawn = False


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
            current = time.time()
            if event.key == pygame.K_UP:
                if current - last_time_shot >= delaylaser:
                    lastmove = 'w'
                    Lasershot.append(ShotLaser(screen=display, xvalue=player.x + player.width / 2,
                                               yvalue=player.y + player.height / 2, last_move=lastmove))
                    lasersound.play()
                    last_time_shot = current
            if event.key == pygame.K_DOWN:
                if current - last_time_shot >= delaylaser:
                    lastmove = 's'
                    Lasershot.append(ShotLaser(screen=display, xvalue=player.x + player.width / 2,
                                               yvalue=player.y + player.height / 2, last_move=lastmove))
                    lasersound.play()
                    last_time_shot = current
            if event.key == pygame.K_LEFT:
                if current - last_time_shot >= delaylaser:
                    lastmove = 'a'
                    Lasershot.append(ShotLaser(screen=display, xvalue=player.x + player.width / 2,
                                               yvalue=player.y + player.height / 2, last_move=lastmove))
                    lasersound.play()
                    last_time_shot = current
            if event.key == pygame.K_RIGHT:
                if current - last_time_shot >= delaylaser:
                    lastmove = 'd'
                    Lasershot.append(ShotLaser(screen=display, xvalue=player.x + player.width / 2,
                                               yvalue=player.y + player.height / 2, last_move=lastmove))
                    lasersound.play()
                    last_time_shot = current
            if event.key == pygame.K_SPACE:
                if ArsenalMines > 0:
                    ArsenalMines -= 1
                    Mineshot.append(LayMine(screen=display, xvalue=player.x + player.width / 2,
                                            yvalue=player.y + player.height / 2, ))
                    mineplacesound.play()

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

    # pause spil
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause = True
                while pause is True:

                    for eventpause in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pause = False
                            gamerunning = False
                        if eventpause.type == pygame.KEYDOWN:
                            if eventpause.key == pygame.K_ESCAPE:
                                pause = False
                                gamerunning = False
                            if eventpause.key == pygame.K_p:
                                pause = False

                    pausetext = Fontbig.render('PAUSED', True, (255, 255, 255))
                    display.blit(pausetext, (screenwith/2-120, screenheight/2-20))

                    pygame.display.flip()

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
            enemydeadsound.play()
            lives -= 1

        for lasershot in Lasershot:
            if collisionchecker(enemy, lasershot):
                Lasershot.remove(lasershot)
                minepoint += 1
                enemydeadsound.play()

                try:
                    Fjender.remove(enemy)
                except ValueError:
                    pass

        for Mine in Mineshot:
            if collisionchecker_circle_square(Mine, enemy):
                Mineshot.remove(Mine)
                enemydeadsound.play()

                try:
                    Fjender.remove(enemy)
                except ValueError:
                    pass

    for enemy in HeavyFjender:
        enemy.draw()
        enemy.update()

        if collisionchecker(player, enemy):
            HeavyFjender.remove(enemy)
            enemydeadsound.play()
            lives -= 3

        for lasershot in Lasershot:
            if collisionchecker(enemy, lasershot):
                Lasershot.remove(lasershot)
                enemydeadsound.play()

                if enemy.dead:
                    minepoint += 3
                    try:
                        HeavyFjender.remove(enemy)
                    except ValueError:
                        pass
                else:
                    enemy.lives -= 1

        for Mine in Mineshot:
            if collisionchecker_circle_square(Mine, enemy):
                Mineshot.remove(Mine)
                enemydeadsound.play()

                if enemy.dead:
                    try:
                        HeavyFjender.remove(enemy)
                    except ValueError:
                        pass
                else:
                    enemy.lives -= 1

    for enemy in MineswepperFjender:
        enemy.draw()
        enemy.update()

        if collisionchecker(player, enemy):
            MineswepperFjender.remove(enemy)
            enemydeadsound.play()

        for lasershot in Lasershot:
            if collisionchecker(enemy, lasershot):
                Lasershot.remove(lasershot)
                enemydeadsound.play()

                try:
                    MineswepperFjender.remove(enemy)
                except ValueError:
                    pass

        for Mine in Mineshot:
            if collisionchecker_circle_square(Mine, enemy):
                Mineshot.remove(Mine)

    for astriod in Astroids:
        astriod.draw()
        astriod.move()

        if collisionchecker(player, astriod):
            lives = 0

        for enemy in Fjender:
            if collisionchecker_circle_square(astriod, enemy):
                Fjender.remove(enemy)
                enemydeadsound.play()

        for enemy in HeavyFjender:
            if collisionchecker_circle_square(astriod, enemy):
                HeavyFjender.remove(enemy)
                enemydeadsound.play()

        for enemy in MineswepperFjender:
            if collisionchecker_circle_square(astriod, enemy):
                MineswepperFjender.remove(enemy)
                enemydeadsound.play()

        if astriod.x > 5000 or astriod.x < -5000 or astriod.y > 5000 or astriod.y < -5000:
            Astroids.remove(astriod)

    if len(Fjender) == 0 and len(HeavyFjender) == 0 and len(MineswepperFjender) == 0:
        wave += 1

        if wave >= wavelives:
            lives += 1
            wavelives += 4

        if wave >= waveheavyspawn:
            antalfjenderheavy += 1
            waveheavyspawn += 5
        else:
            antalfjender += 2

        if wave >= wavemineswepperspawn:
            antalfjendermineswpper += 1
            wavemineswepperspawn += 5

        for i in range(antalfjender):
            fjende_spawn = True
            while fjende_spawn:
                new_enemy = EnemyClass(screen=display, xvalue=random.randint(0, screenwith - 30),
                                       yvalue=random.randint(0, screenheight - 30), speedx=random.randint(1, 5),
                                       speedy=random.randint(1, 10), colour=(255, 0, 0))
                if collisionchecker(new_enemy, player):
                    new_enemy.x = random.randint(0, screenwith - 10)
                    new_enemy.y = random.randint(0, screenheight - 150)
                else:
                    Fjender.append(new_enemy)
                    fjende_spawn = False

        for n in range(antalfjenderheavy):
            heavyfjendespawn = True
            while heavyfjendespawn:
                new_heavy = HeavyEnemyClass(screen=display, xvalue=random.randint(0, screenwith-40),
                                            yvalue=random.randint(0, screenheight-40), speedx=random.randint(1, 5),
                                            speedy=random.randint(1, 5))
                if collisionchecker(new_heavy, player):
                    new_heavy.x = random.randint(0, screenwith-10)
                    new_heavy.y = random.randint(0, screenheight-10)
                else:
                    HeavyFjender.append(new_heavy)
                    heavyfjendespawn = False

        for William in range(antalfjendermineswpper):
            mineswpperspawn = True
            while mineswpperspawn:
                new_enemy = EnemyClass(screen=display, xvalue=random.randint(0, screenwith - 30),
                                       yvalue=random.randint(0, screenheight - 30), speedx=random.randint(1, 5),
                                       speedy=random.randint(1, 10), colour=(0, 255, 0))
                if collisionchecker(new_enemy, player):
                    new_enemy.x = random.randint(0, screenwith - 10)
                    new_enemy.y = random.randint(0, screenheight - 150)
                else:
                    MineswepperFjender.append(new_enemy)
                    mineswpperspawn = False

    if minepoint > 50:
        ArsenalMines += 1
        minepoint = 0

    livestext = Font.render(f'Lives: {lives}', True, (255, 255, 255))
    display.blit(livestext, (10, 50))

    pointstext = Font.render(f'Wave: {wave}', True, (255, 255, 255))
    display.blit(pointstext, (10, 10))

    minetext = Font.render(f'Mine: {ArsenalMines}', True, (255, 255, 255))
    display.blit(minetext, (screenwith-160, 10))

    makeastroid = random.randint(1, 100000)

    if makeastroid < 10:
        direction = random.randint(1, 4)
        if direction == 1:
            xastriond = random.randrange(1, screenwith)
            yastriond = -random.randrange(100, 200)
        elif direction == 2:
            xastriond = -random.randrange(100, 200)
            yastriond = random.randrange(1, screenheight)
        elif direction == 3:
            xastriond = random.randrange(1, screenwith)
            yastriond = random.randrange(screenheight+100, screenheight+200)
        elif direction == 4:
            xastriond = random.randrange(screenwith+100, screenwith+200)
            yastriond = random.randrange(1, screenheight)
        else:
            xastriond = 0
            yastriond = 0

        Astroids.append(AstroidClass(screen=display, xvalue=xastriond, yvalue=yastriond, speed=5,
                                     radius=50, direction=direction))

    # Updater display
    pygame.display.flip()

    if lives <= 0:
        gameover = True
        gameoversound.play()

        if highscore < wave-1:
            highscore = wave-1
            d['highscore'] = wave-1

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
                        Astroids.clear()
                        player.xmove = 0
                        player.ymove = 0
                        lives = 5
                        antalfjender = 0
                        wave = 1
                        waveheavyspawn = 5
                        antalfjenderheavy = 0
                        player.x = screenwith / 2 - 20
                        player.y = screenheight - 100
                        ArsenalMines = 5

            gameovertext = Fontbig.render(f'GAME OVER', True, (255, 255, 255))
            display.blit(gameovertext, (screenwith/2 - 200, screenheight / 2 - 200))

            gameovertext = Font.render(f'WAVE: {wave-1}', True, (255, 255, 255))
            display.blit(gameovertext, (screenwith/2 - 50, screenheight / 2 - 100))

            gameovertext = Font.render('Tryk R for at starte igen', True, (255, 255, 255))
            display.blit(gameovertext, (screenwith/2 - 110, screenheight / 2))

            gameovertext = Font.render(f'HIGHSCORE: wave {highscore}', True, (255, 255, 255))
            display.blit(gameovertext, (screenwith/2 - 110, 20))

            pygame.display.flip()

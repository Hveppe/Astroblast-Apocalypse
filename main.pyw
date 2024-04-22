# Spillet er lavet af Hveppe

# importer fra andre python filer
from Player import PlayerClass
from abilities import ShotLaser, LayMine, Shield
from Enemy import EnemyClass, HeavyEnemyClass, HommingEnemyClass
from objekts import AstroidClass, Picture, Button
from collisioncheck_functioner import collisionchecker, collisionchecker_circle, collisionchecker_circle_square

# importer libaries
import random
import pygame
import time

# starter pygame og pygame font
pygame.init()
pygame.font.init()

# opsætting af skærm og angiver et navn til programet
screenwith, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((screenwith, screenheight))
pygame.display.set_caption("Astroblast Apocalypse")

gameimagepng = pygame.image.load('Image/Icon/gameimageversion2.png').convert()
pygame.display.set_icon(gameimagepng)

# baggrund
baggrund = pygame.image.load('Image/baggrund.jpg')
baggrund = pygame.transform.scale(baggrund, (screenwith, screenheight))
baggrund = Picture(screen=display, x=0, y=0, image=baggrund)

# baggrunds music
pygame.mixer.music.load('sound/backgroundmusic-200697.wav')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


# lyde til spillet
lasersound = pygame.mixer.Sound('sound/laser-gun-81720.wav')
mineplacesound = pygame.mixer.Sound('sound/place-100513.wav')
enemydeadsound = pygame.mixer.Sound('sound/big explosion.wav')
gameoversound = pygame.mixer.Sound('sound/game-over-160612.wav')

# laver lister til classer der skal havde flere af gangen på skærmen
# Våben
Lasershot = []
Mineshot = []
# Fjender
Fjender = []
MineswepperFjender = []
HeavyFjender = []
HommingFjender = []
# objekter
Astroids = []

# laver player
player = PlayerClass(screen=display, xvalue=screenwith/2, yvalue=screenheight/2,
                     picture=pygame.image.load('Image/Rumskibplayer.png'))

# variabler
lastmove = 'w'
antalfjender = 2
antalfjenderheavy = 0
antalfjendermineswpper = 0
antalfjenderhomming = 0
debug = False

wave = 1
waveheavyspawn = 5
wavemineswepperspawn = 6
wavehommingspawn = 7

lives = 5
wavelives = 4
minepoint = 0
fjende_spawn = False

waveheavyspawnadd = 5
wavemineswepperspawnadd = 4
wavehommingspawnadd = 4

changeinrate = 10

# delay til laser
delaylaser = 0.3
last_time_shot = 0
shotting = False

# shield varaibler
shield_up = False
shield_charge = 100
drain_speed = 0.5
last_draintime = None

# giving time of start
startgametime = time.time()
timer = time.time()-startgametime

# henter gemte highscore
try:
    with open('textfiler/highscore.txt', 'r') as file:
        highscore = int(file.read())
except ValueError or TypeError:
    highscore = 0

# Antal våben til rådighed
ArsenalMines = 5

# Opsætter clock
clock = pygame.time.Clock()

# Fonts til text
Font = pygame.font.SysFont('Comic Sans MS', 36, bold=False, italic=False)
Fontbig = pygame.font.SysFont('Comic Sans MS', 100, bold=True, italic=False)
Fontmainmenu_lowertekst = pygame.font.SysFont('Comic Sans MS', 40, bold=False, italic=False)

for i in range(antalfjender):
    fjende_spawn = True
    while fjende_spawn:
        enemy = EnemyClass(screen=display, xvalue=random.randint(0, screenwith - 40),
                           yvalue=random.randint(0, screenheight - 40), speedx=random.randint(1, 10),
                           speedy=random.randint(1, 10), colour=(255, 0, 0),
                           picture=pygame.image.load('Image/Fjender/Normalfjendeimage.png'))
        if collisionchecker(enemy, player):
            enemy.xvalue = random.randint(0, screenwith - 10)
            enemy.yvalue = random.randint(0, screenheight - 150)
        else:
            Fjender.append(enemy)
            fjende_spawn = False

# Laver shield
shield = Shield(display, player.x, player.y)

# ----------------------------------------laver knapper----------------------------------------------------------------
startspil_knap = Button(screen=display, tekst="START", size=(400, 100),
                        image=pygame.image.load('Image/Buttons/Simpel_button.png'))

infospil_knap = Button(screen=display, tekst="INFORMATION", size=(400, 100),
                       image=pygame.image.load('Image/Buttons/Simpel_button.png'))

return_knap = Button(screen=display, tekst="RETURN TO MENU", size=(450, 100),
                     image=pygame.image.load('Image/Buttons/Simpel_button.png'))

# variabler for loop
gamerunning = True
mainmenu = True
infoscreen = False

while gamerunning:
    # starter main menu loop
    # -------------------------------------Main Menu-------------------------------------------------------------------
    while mainmenu:
        # Laver mousecursor synlig
        pygame.mouse.set_visible(True)

        # sætter framerate til 60
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamerunning = False
                mainmenu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gamerunning = False
                    mainmenu = False
                if event.key == pygame.K_SPACE:
                    mainmenu = False

                    # reset/start timer
                    startgametime = time.time()
                if event.key == pygame.K_i:
                    infoscreen = True

            # starter loop for info skærm
            # -------------------------------------Info Screen--------------------------------------------------
            while infoscreen is True:
                # sætter framerate til 60
                clock.tick(60)

                for eventinfo in pygame.event.get():
                    if eventinfo.type == pygame.QUIT:
                        pause = False
                        gamerunning = False
                        infoscreen = False
                        mainmenu = False
                    if eventinfo.type == pygame.KEYDOWN:
                        if eventinfo.key == pygame.K_ESCAPE:
                            pause = False
                            gamerunning = False
                            infoscreen = False
                            mainmenu = False
                        if eventinfo.key == pygame.K_i:
                            infoscreen = False

                display.fill((0, 0, 0))
                baggrund.draw()

                # ---------------------------------objects info------------------------------------------------
                # Overskrift til objekter
                tekst = Font.render('Types of objects', True, (255, 255, 255))
                display.blit(tekst, (100, 20))

                # Player
                picture = pygame.transform.scale(pygame.image.load('Image/Rumskibplayer.png'),
                                                 (70, 70))
                picture_rect = picture.get_rect(topleft=(100, 100))
                display.blit(picture, picture_rect.topleft)

                tekst = Font.render('Player Spaceship', True, (255, 255, 255))
                display.blit(tekst, (120 + picture_rect.width, 100 + picture_rect.height/2 -
                                     tekst.get_height()/2))

                # Normal fjende
                picture = pygame.transform.scale(pygame.image.load('Image/Fjender/Normalfjendeimage.png'),
                                                 (70, 70))
                picture_rect = picture.get_rect(topleft=(100, 200))
                display.blit(picture, picture_rect.topleft)

                tekst = Font.render('Normal Enemy', True, (255, 255, 255))
                display.blit(tekst, (120 + picture_rect.width, 200 + picture_rect.height/2 -
                                     tekst.get_height()/2))

                # Mineswepper fjende
                picture = pygame.transform.scale(pygame.image.load('Image/Fjender/Mineswepperfjendeimage.png'),
                                                 (70, 70))
                picture_rect = picture.get_rect(topleft=(100, 300))
                display.blit(picture, picture_rect.topleft)

                tekst = Font.render('Mineswpper Enemy', True, (255, 255, 255))
                display.blit(tekst, (120 + picture_rect.width, 300 + picture_rect.height/2 -
                                     tekst.get_height()/2))

                # Homming fjender
                picture = pygame.transform.scale(pygame.image.load('Image/Fjender/HommingFjendeImage.png'),
                                                 (70, 70))
                picture_rect = picture.get_rect(topleft=(100, 400))
                display.blit(picture, picture_rect.topleft)

                tekst = Font.render('Homing Enemy', True, (255, 255, 255))
                display.blit(tekst, (120 + picture_rect.width, 400 + picture_rect.height/2 -
                                     tekst.get_height()/2))

                # Heavy fjender
                picture = pygame.transform.scale(pygame.image.load('Image/Fjender/Heavyfjendeimage.png'),
                                                 (70, 70))
                picture_rect = picture.get_rect(topleft=(100, 500))
                display.blit(picture, picture_rect.topleft)

                tekst = Font.render('Heavy Enemy', True, (255, 255, 255))
                display.blit(tekst, (120 + picture_rect.width, 500 + picture_rect.height/2 -
                                     tekst.get_height()/2))

                # ----------------------------Info om Controls--------------------------------------------------
                # Overskrift
                controltekst = Font.render('Controls', True, (255, 255, 255))
                display.blit(controltekst, (screenwith - screenwith/4 - controltekst.get_width()/2, 20))

                # Displayer controls
                tekst = Font.render('Movement: W, A, S, D', True, (255, 255, 255))
                display.blit(tekst, (screenwith - screenwith/4 - tekst.get_width()/2, 100))

                tekst = Font.render('Shot Laser: ARROWS', True, (255, 255, 255))
                display.blit(tekst, (screenwith - screenwith/4 - tekst.get_width()/2, 200))

                tekst = Font.render('Place Mine: M', True, (255, 255, 255))
                display.blit(tekst, (screenwith - screenwith/4 - tekst.get_width()/2, 300))

                tekst = Font.render('Shield: SPACE', True, (255, 255, 255))
                display.blit(tekst, (screenwith - screenwith / 4 - tekst.get_width() / 2, 400))

                tekst = Font.render('Show Hitboxes: H', True, (255, 255, 255))
                display.blit(tekst, (screenwith - screenwith/4 - tekst.get_width()/2, 500))

                tekst = Font.render('Pause Game: P', True, (255, 255, 255))
                display.blit(tekst, (screenwith - screenwith / 4 - tekst.get_width() / 2, 600))

                tekst = Font.render('Close Game: ESCAPE', True, (255, 255, 255))
                display.blit(tekst, (screenwith - screenwith / 4 - tekst.get_width() / 2, 700))

                # return button
                if return_knap.draw(screenwith/2-225, screenheight-100) is True:
                    infoscreen = False

                pygame.display.flip()

        display.fill((0, 0, 0))
        baggrund.draw()

        # displayer title
        mainmenutext = Fontbig.render('Astroblast', True, (255, 255, 255))
        display.blit(mainmenutext, (screenwith/2-mainmenutext.get_width()/2, 100))
        mainmenutext = Fontbig.render('Apocalypse', True, (255, 255, 255))
        display.blit(mainmenutext, (screenwith/2 - mainmenutext.get_width()/2, 190))

        # displayer highscore
        mainmenutext = Font.render(f'Highscore: wave {highscore}', True, (255, 255, 255))
        display.blit(mainmenutext, (screenwith/2-mainmenutext.get_width()/2, 20))

        if startspil_knap.draw(screenwith/2-200, screenheight/2-50) is True:
            mainmenu = False

            # reset/start timer
            startgametime = time.time()

        if infospil_knap.draw(screenwith/2-200, screenheight/2+60) is True:
            infoscreen = True

        pygame.display.flip()

    # -------------------------------------Main Game-------------------------------------------------------------------
    # Laver mousecursor usynlig
    pygame.mouse.set_visible(False)

    # sætter framerate til 60
    clock.tick(60)

    current = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            gamerunning = False

            if highscore < wave - 1:
                highscore = wave - 1
                with open('textfiler/highscore.txt', 'w') as file:
                    file.write(str(highscore))

        # controls til PlayerClass
        if event.type == pygame.KEYDOWN:
            # Kode til at kontroler våben
            if event.type == pygame.KEYDOWN:
                # Kode til at kontroler våben
                if event.key == pygame.K_UP:
                    lastmove = 'up'
                    shotting = True
                if event.key == pygame.K_DOWN:
                    lastmove = 'down'
                    shotting = True
                if event.key == pygame.K_LEFT:
                    lastmove = 'left'
                    shotting = True
                if event.key == pygame.K_RIGHT:
                    lastmove = 'right'
                    shotting = True

            # controls til mine
            if event.key == pygame.K_m:
                if ArsenalMines > 0 and shield_up is False:
                    ArsenalMines -= 1
                    Mineshot.append(LayMine(screen=display, xvalue=player.x + player.width/2,
                                            yvalue=player.y + player.height/2))
                    mineplacesound.play()

            if event.key == pygame.K_SPACE:
                shield_up = True

            # Bevægelse af player
            if event.key == pygame.K_w:
                player.ymove -= player.movespeed
            if event.key == pygame.K_s:
                player.ymove += player.movespeed
            if event.key == pygame.K_d:
                player.xmove += player.movespeed
            if event.key == pygame.K_a:
                player.xmove -= player.movespeed
            if event.key == pygame.K_h:
                debug = True

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
            if event.key == pygame.K_h:
                debug = False

            # modvirker våben
            if (event.key == pygame.K_UP or event.key == pygame.K_DOWN or
                    event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                    shotting = True
                else:
                    shotting = False

            if event.key == pygame.K_SPACE:
                shield_up = False

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
                                player.xmove = 0
                                player.ymove = 0

                    pausetext = Fontbig.render('PAUSED', True, (255, 255, 255))
                    display.blit(pausetext, (screenwith/2-pausetext.get_width()/2, screenheight/2
                                             - pausetext.get_height()/2))

                    pygame.display.flip()

    if shotting is True and shield_up is False:
        if current - last_time_shot >= delaylaser:
            Lasershot.append(ShotLaser(screen=display, xvalue=player.x + player.width/2,
                                       yvalue=player.y + player.height/2, last_move=lastmove))
            lasersound.play()
            last_time_shot = current

    # Farver baggrund
    display.fill((0, 0, 0))
    baggrund.draw()

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
            if shield_up:
                pass
            else:
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
            if shield_up:
                pass
            else:
                HeavyFjender.remove(enemy)
                enemydeadsound.play()
                lives -= enemy.lives

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
            if shield_up:
                pass
            else:
                MineswepperFjender.remove(enemy)
                enemydeadsound.play()
                lives -= 1

        for lasershot in Lasershot:
            if collisionchecker(enemy, lasershot):
                Lasershot.remove(lasershot)
                enemydeadsound.play()

                try:
                    MineswepperFjender.remove(enemy)
                    minepoint += 1
                except ValueError:
                    pass

        for Mine in Mineshot:
            if collisionchecker_circle_square(Mine, enemy):
                Mineshot.remove(Mine)

    for enemy in HommingFjender:
        enemy.update(player=player)
        enemy.draw()

        if collisionchecker(enemy, player):
            if shield_up:
                pass
            else:
                HommingFjender.remove(enemy)
                lives -= 1
                enemydeadsound.play()

        for lasershot in Lasershot:
            if collisionchecker(enemy, lasershot):
                Lasershot.remove(lasershot)
                enemydeadsound.play()

                try:
                    HommingFjender.remove(enemy)
                    minepoint += 1
                except ValueError:
                    pass

        for Mine in Mineshot:
            if collisionchecker_circle_square(Mine, enemy):
                Mineshot.remove(Mine)
                enemydeadsound.play()

                try:
                    HommingFjender.remove(enemy)
                except ValueError:
                    pass

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

        for enemy in HommingFjender:
            if collisionchecker_circle_square(astriod, enemy):
                HommingFjender.remove(enemy)
                enemydeadsound.play()

        for lasershot in Lasershot:
            if collisionchecker_circle_square(astriod, lasershot):
                Lasershot.remove(lasershot)

        for Mine in Mineshot:
            if collisionchecker_circle(Mine, astriod):
                Mineshot.remove(Mine)
                enemydeadsound.play()

        if astriod.x > 5000 or astriod.x < -5000 or astriod.y > 5000 or astriod.y < -5000:
            Astroids.remove(astriod)

    if len(Fjender) == 0 and len(HeavyFjender) == 0 and len(MineswepperFjender) == 0 and len(HommingFjender) == 0:
        wave += 1

        if wave >= wavelives:
            lives += 1
            wavelives += 4

        if wave >= waveheavyspawn:
            antalfjenderheavy += 1
            waveheavyspawn += waveheavyspawnadd
            antalfjender -= 1
        else:
            antalfjender += 2

        if wave >= wavemineswepperspawn:
            antalfjendermineswpper += 1
            wavemineswepperspawn += wavemineswepperspawnadd

        if wave >= wavehommingspawn:
            antalfjenderhomming += 2
            antalfjender -= 2
            wavehommingspawn += wavehommingspawnadd

        if wave == changeinrate and waveheavyspawn > 1:
            waveheavyspawnadd -= 1
            changeinrate += 10

        for i in range(antalfjender):
            fjende_spawn = True
            while fjende_spawn:
                new_enemy = EnemyClass(screen=display, xvalue=random.randint(0, screenwith - 40),
                                       yvalue=random.randint(0, screenheight - 40), speedx=random.randint(1, 5),
                                       speedy=random.randint(1, 10), colour=(255, 0, 0),
                                       picture=pygame.image.load('Image/Fjender/Normalfjendeimage.png'))
                if collisionchecker(new_enemy, player):
                    new_enemy.x = random.randint(0, screenwith - 10)
                    new_enemy.y = random.randint(0, screenheight - 150)
                else:
                    Fjender.append(new_enemy)
                    fjende_spawn = False

        for n in range(antalfjenderheavy):
            heavyfjendespawn = True
            while heavyfjendespawn:
                new_heavy = HeavyEnemyClass(screen=display, xvalue=random.randint(0, screenwith-60),
                                            yvalue=random.randint(0, screenheight-60), speedx=random.randint(1, 5),
                                            speedy=random.randint(1, 5),
                                            picture=pygame.image.load('Image/Fjender/Heavyfjendeimage.png'))
                if collisionchecker(new_heavy, player):
                    new_heavy.x = random.randint(0, screenwith-10)
                    new_heavy.y = random.randint(0, screenheight-10)
                else:
                    HeavyFjender.append(new_heavy)
                    heavyfjendespawn = False

        for m in range(antalfjendermineswpper):
            mineswpperspawn = True
            while mineswpperspawn:
                new_enemy = EnemyClass(screen=display, xvalue=random.randint(0, screenwith - 40),
                                       yvalue=random.randint(0, screenheight - 40), speedx=random.randint(1, 10),
                                       speedy=random.randint(1, 10), colour=(0, 255, 0),
                                       picture=pygame.image.load('Image/Fjender/Mineswepperfjendeimage.png'))
                if collisionchecker(new_enemy, player):
                    new_enemy.x = random.randint(0, screenwith - 10)
                    new_enemy.y = random.randint(0, screenheight - 30)
                else:
                    MineswepperFjender.append(new_enemy)
                    mineswpperspawn = False

        for h in range(antalfjenderhomming):
            hommingspawn = True
            while hommingspawn:
                new_enemy = HommingEnemyClass(screen=display, xvalue=random.randint(0, screenwith-50),
                                              yvalue=random.randint(0, screenheight-50), speedx=5,
                                              speedy=5, color=(255, 0, 0),
                                              picture=pygame.image.load('Image/Fjender/HommingFjendeImage.png'))
                if collisionchecker(new_enemy, player):
                    new_enemy.x = random.randint(0, screenwith-10)
                    new_enemy.y = random.randint(0, screenheight-10)
                else:
                    HommingFjender.append(new_enemy)
                    hommingspawn = False

    if shield_up is True and shield_charge > 0:
        shield.update(player)
        shield.draw()

        drain_time = time.time()

        if last_draintime is None:
            last_draintime = time.time()

        if drain_time - last_draintime >= drain_speed:
            shield_charge -= 1
            last_draintime = time.time()

        for enemy in Fjender:
            if collisionchecker_circle_square(shield, enemy):
                enemydeadsound.play()

                try:
                    Fjender.remove(enemy)
                except ValueError:
                    pass

        for enemy in HeavyFjender:
            if collisionchecker_circle_square(shield, enemy):
                enemydeadsound.play()
                shield_charge -= 2

                try:
                    HeavyFjender.remove(enemy)
                except ValueError:
                    pass

        for enemy in MineswepperFjender:
            if collisionchecker_circle_square(shield, enemy):
                enemydeadsound.play()

                try:
                    MineswepperFjender.remove(enemy)
                except ValueError:
                    pass

        for enemy in HommingFjender:
            if collisionchecker_circle_square(shield, enemy):
                enemydeadsound.play()

                try:
                    HommingFjender.remove(enemy)
                except ValueError:
                    pass

    if minepoint > 50:
        ArsenalMines += 1
        minepoint = 0

    # Tegner player
    player.draw()
    player.update()

    if debug is True:
        player.draw_debug()

        for enemy in Fjender:
            enemy.draw_debug()

        for enemy in MineswepperFjender:
            enemy.draw_debug()

        for enemy in HeavyFjender:
            enemy.draw_debug()

        for enemy in HommingFjender:
            enemy.draw_debug()

    livestext = Font.render(f'Lives: {lives}', True, (255, 255, 255))
    display.blit(livestext, (10, 90))

    pointstext = Font.render(f'Wave: {wave}', True, (255, 255, 255))
    display.blit(pointstext, (10, 50))

    shield_text = Font.render(f'Shield: {shield_charge}%', True, (255, 255, 255))
    display.blit(shield_text, (screenwith - 260, 10))

    minetext = Font.render(f'Mine: {ArsenalMines}', True, (255, 255, 255))
    display.blit(minetext, (screenwith - 260, 50))

    if lives > 0:
        timer = time.time()-startgametime

    timerext = Font.render(f'Timer: {round(timer, 2)}', True, (255, 255, 255))
    display.blit(timerext, (10, 10))

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

    # -------------------------------------Game Over-------------------------------------------------------------------
    if lives <= 0:
        gameover = True
        gameoversound.play()

        if highscore < wave:
            highscore = wave
            with open('textfiler/highscore.txt', 'w') as file:
                file.write(str(highscore))

        while gameover:
            # Laver mousecursor synlig
            pygame.mouse.set_visible(True)

            # sætter framerate til 60
            clock.tick(60)

            # Farver baggrund
            display.fill((0, 0, 0))
            baggrund.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamerunning = False
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gamerunning = False
                        gameover = False
                    if event.key == pygame.K_r:
                        gameover = False
                        mainmenu = True

                        # Clear lister
                        Lasershot.clear()
                        Mineshot.clear()
                        Fjender.clear()
                        HeavyFjender.clear()
                        MineswepperFjender.clear()
                        HommingFjender.clear()
                        Astroids.clear()

                        # Reset af player
                        player.xmove = 0
                        player.ymove = 0
                        ArsenalMines = 5
                        lives = 5
                        wavelives = 4
                        wave = 1
                        player.x = screenwith / 2 - 20
                        player.y = screenheight - 100
                        shotting = False
                        shield_up = False
                        shield_charge = 100
                        last_draintime = None

                        # reset af fjender
                        antalfjender = 0
                        waveheavyspawn = 5
                        wavemineswepperspawn = 6
                        wavehommingspawn = 7
                        antalfjenderheavy = 0
                        antalfjenderhomming = 0
                        antalfjendermineswpper = 0

            gameovertext = Fontbig.render(f'GAME OVER', True, (255, 255, 255))
            display.blit(gameovertext, (screenwith/2 - gameovertext.get_width()/2, screenheight / 2 - 200))

            gameovertext = Font.render(f'WAVE: {wave}', True, (255, 255, 255))
            display.blit(gameovertext, (screenwith/2 - gameovertext.get_width()/2, screenheight / 2 - 80))

            gameovertext = Font.render(f'TIME: {round(timer, 2)}', True, (255, 255, 255))
            display.blit(gameovertext, (screenwith/2 - gameovertext.get_width()/2, screenheight / 2 - 30))

            gameovertext = Font.render(f'Highscore: wave {highscore}', True, (255, 255, 255))
            display.blit(gameovertext, (screenwith/2 - gameovertext.get_width()/2, 20))

            # return button
            if return_knap.draw(screenwith / 2 - 225, screenheight - 100) is True:
                gameover = False
                mainmenu = True

                # Clear lister
                Lasershot.clear()
                Mineshot.clear()
                Fjender.clear()
                HeavyFjender.clear()
                MineswepperFjender.clear()
                HommingFjender.clear()
                Astroids.clear()

                # Reset af player
                player.xmove = 0
                player.ymove = 0
                ArsenalMines = 5
                lives = 5
                wavelives = 4
                wave = 1
                player.x = screenwith / 2 - 20
                player.y = screenheight - 100
                shotting = False
                shield_up = False
                shield_charge = 100
                last_draintime = None

                # reset af fjender
                antalfjender = 0
                waveheavyspawn = 5
                wavemineswepperspawn = 6
                wavehommingspawn = 7
                antalfjenderheavy = 0
                antalfjenderhomming = 0
                antalfjendermineswpper = 0

            pygame.display.flip()

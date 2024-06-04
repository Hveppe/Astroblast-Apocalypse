# Spillet er lavet af Hveppe

# importer fra andre python filer i mappen
from Player import PlayerClass
from abilities import ShotLaser, LayMine, Shield
from Enemy import EnemyClass, HeavyEnemyClass, HommingEnemyClass
from objekts import AstroidClass, Picture, Button
from collisioncheck_functioner import collisionchecker, collisionchecker_circle, collisionchecker_circle_square
from Mouse import MouseCursor
from Sidefunctions import *
from Define import *
from Healthbar_and_slider import HealthBar, Slider
from SkinMenu_class_function import SkinSlecter, LaserColorChange

# importer libaries
import random
import pygame
import time
import sys

# starter pygame og pygame font
pygame.init()
pygame.font.init()

# opsætting af skærm og angiver et navn til programet
screenwith, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((screenwith, screenheight))
pygame.display.set_caption("Astroblast Apocalypse")

# Starter en loading screen
display.fill(Black)

gameimagepng = pygame.image.load('Image/Icon/gameimageversion2.png').convert()
pygame.display.set_icon(gameimagepng)

# baggrund
baggrund = pygame.image.load('Image/baggrund.jpg').convert()
baggrund = pygame.transform.scale(baggrund, (screenwith, screenheight))
baggrund = Picture(screen=display, x=0, y=0, image=baggrund)

# billede til effekter
explosion_effeckt = pygame.image.load("Image/effects/explosion-with-pixel-art.png")

# baggrunds music
pygame.mixer.music.load('sound/backgroundmusic-200697.wav')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

# lyde til spillet
lasersound = pygame.mixer.Sound('sound/laser-gun-81720.wav')
mineplacesound = pygame.mixer.Sound('sound/place-100513.wav')
enemydeadsound = pygame.mixer.Sound('sound/big explosion.wav')
gameoversound = pygame.mixer.Sound('sound/game-over-160612.wav')
teleportsound = pygame.mixer.Sound('sound/game-teleport-90735.wav')

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

# variabler class
variabler = Variabler()

# laver player
player = PlayerClass(screen=display, xvalue=screenwith/2, yvalue=screenheight/2,
                     picture=pygame.image.load('Image/Playerships/Rumskibplayer.png').convert_alpha(),
                     damage_picture=tint_image(pygame.image.load('Image/Playerships/Rumskibplayer.png').convert_alpha(),
                                               (255, 0, 0)))

# henter gemte highscore
try:
    with open('textfiler/highscore.txt', 'r') as file:
        highscore = int(file.read())
except ValueError or TypeError:
    highscore = 0

# Opsætter clock
clock = pygame.time.Clock()
last_teleport = time.time()-30

# Fonts til text
Font = pygame.font.SysFont('Comic Sans MS', int(round(36, 0)), bold=False, italic=False)
Fontsmall = pygame.font.SysFont("Ariel", int(round(35, 0)), bold=False, italic=False)
Fontbig = pygame.font.SysFont('Comic Sans MS', int(round(100, 0)), bold=True, italic=False)
Fontmainmenu_lowertekst = pygame.font.SysFont('Comic Sans MS', int(round(40, 0)), bold=False, italic=False)

# ------------------------------------------------Mouse, Shield, Fjender------------------------------------------------
# laver mouse cursor
click = False
mousecursor = MouseCursor(screen=display,
                          picture=pygame.image.load("Image/mousecursor/orange-gradient_cusor.png").convert_alpha(),
                          picture_clik=pygame.image.load("Image/mousecursor/orange-gradient_cusor - click.png")
                          .convert_alpha())

# laver Fjender
for i in range(variabler.antalfjender):
    spawn_enemy(Fjender, EnemyClass, player, screenwith, screenheight, display, random.randint(0, screenwith - 40),
                random.randint(0, screenheight - 60), random.randint(1, 5), random.randint(1, 10),
                pygame.image.load('Image/Fjender/Normalfjendeimage.png').convert_alpha())

# laver shield
shield = Shield(display, player.x, player.y)

# ----------------------------------------laver knapper----------------------------------------------------------------
startspil_knap = Button(screen=display, tekst="START GAME", size=(450, 100),
                        image=pygame.image.load('Image/Buttons/Simpel_button.png').convert_alpha())

infospil_knap = Button(screen=display, tekst="INFORMATION", size=(450, 100),
                       image=pygame.image.load('Image/Buttons/Simpel_button.png').convert_alpha())

return_knap = Button(screen=display, tekst="RETURN TO MENU", size=(450, 100),
                     image=pygame.image.load('Image/Buttons/Simpel_button.png').convert_alpha())

skin_knap = Button(screen=display, tekst="SKINS", size=(450, 100),
                   image=pygame.image.load("Image/Buttons/Simpel_button.png").convert_alpha())

returntogame_button = Button(screen=display, tekst="RETURN TO GAME", size=(450, 100),
                             image=pygame.image.load("Image/Buttons/Simpel_button.png").convert_alpha())

quitgame_button = Button(screen=display, tekst="QUIT GAME", size=(450, 100),
                         image=pygame.image.load("Image/Buttons/Simpel_button.png").convert_alpha())

options_button = Button(screen=display, tekst="OPTIONS", size=(220, 100),
                        image=pygame.image.load("Image/Buttons/Simpel_button.png").convert_alpha())

# ---------------------------------------------SKINS/LASERCOLOR---------------------------------------------------------
# player skin ting
playerskinselecter = SkinSlecter(display, screenwith/2-340, screenheight/2-300, (300, 180), "player",
                                 pygame.image.load("Image/Playerships/Rumskibplayer.png").convert_alpha(),
                                 pygame.image.load("Image/Playerships/Rumskibplayer2.png").convert_alpha(),
                                 pygame.image.load("Image/Playerships/Rumskibplayer3.png").convert_alpha(),
                                 pygame.image.load("Image/Playerships/Rumskibplayer4.png").convert_alpha(),
                                 pygame.image.load("Image/Playerships/Rumskibplayer5.png").convert_alpha(),
                                 pygame.image.load("Image/Playerships/Rumskibplayer6.png").convert_alpha(),
                                 pygame.image.load("Image/Playerships/Rumskibplayer7.png").convert_alpha(),
                                 pygame.image.load("Image/Playerships/Rumskibplayer8.png").convert_alpha(),
                                 pygame.image.load("Image/Playerships/Rumskibplayer9.png").convert_alpha())

# cursor skin ting | Hver anden *args er click billeder
cursorskinselecter = SkinSlecter(display, screenwith/2+40, screenheight/2-300, (300, 180), "cursor",
                                 pygame.image.load("Image/mousecursor/orange-gradient_cusor.png").convert_alpha(),
                                 pygame.image.load("Image/mousecursor/orange-gradient_cusor - click.png")
                                 .convert_alpha(),
                                 pygame.image.load("Image/mousecursor/spacrecraft-custom-cursor.png").convert_alpha(),
                                 pygame.image.load("Image/mousecursor/spacrecraft-custom-cursor -click.png")
                                 .convert_alpha(),
                                 pygame.image.load("Image/mousecursor/Nasa_space_cursor.png").convert_alpha(),
                                 pygame.image.load("Image/mousecursor/Nasa_space_cursor - click.png").convert_alpha())

laserchangecolor = LaserColorChange(display, (screenwith/2-125, screenheight-400), (100, 100))

# Ændre skin og lasercolour til gemte valg fra skin tekstfilen
with open('textfiler/skin', 'r') as file:
    playerskinselecter.chosenskin = int(file.readline().strip())
    cursorskinselecter.chosenskin = int(file.readline().strip())
    laser_color = file.readline().strip()
    laser_color = tuple(map(int, laser_color.split(',')))
    player.picture, player.damage_picture = playerskinselecter.change_skin()
    mousecursor.picture, mousecursor.picture_clik = cursorskinselecter.change_skin()
    player.update_picture()
    mousecursor.update_picture()

# ------------------------------------------Bars and sliders-----------------------------------------------------------
# De forskellige bar
health_bar = HealthBar(10, 10, 300, 40, 5, Green, Red)
shied_bar = HealthBar(screenwith-300*scalar, 10, 300, 40, 100, DarkBlue, Grey)
teleport_bar = HealthBar(screenwith-300*scalar, 10+shied_bar.height, 300, 40, 30, Yellow, Grey)

# slider
lyd_slider = Slider(400, 50, display, 1, Grey, White, Red)
music_slider = Slider(400, 50, display, 1, Grey, White, Red)

# ------------------------------------------variabler for loop---------------------------------------------------------
gamerunning = True
mainmenu = True
infoscreen = False
skinmeny = False
maingame = False
pause = False
option = False

# Laver mousecursor synlig
pygame.mouse.set_visible(False)

while gamerunning:
    # starter main menu loop
    # -------------------------------------Main Menu-------------------------------------------------------------------
    while mainmenu:
        # sætter framerate til 60
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # starter loop for info skærm
        # -------------------------------------Info Screen--------------------------------------------------
        while infoscreen:

            for eventinfo in pygame.event.get():
                if eventinfo.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            display.fill((0, 0, 0))
            baggrund.draw()

            # ---------------------------------objects info------------------------------------------------
            # Overskrift til objekter
            tekst = Font.render('Types of objects', True, Orange)
            display.blit(tekst, (100, 20))

            # Player
            picture = pygame.transform.scale(player.picture, (70, 70))
            picture_rect = picture.get_rect(topleft=(100, 100))
            display.blit(picture, picture_rect.topleft)

            tekst = Font.render('Player Spaceship', True, White)
            display.blit(tekst, (120 + picture_rect.width, 100 + picture_rect.height / 2 -
                                 tekst.get_height() / 2))

            # Normal fjende
            picture = pygame.transform.scale(pygame.image.load('Image/Fjender/Normalfjendeimage.png').
                                             convert_alpha(), (70, 70))
            picture_rect = picture.get_rect(topleft=(100, 200))
            display.blit(picture, picture_rect.topleft)

            tekst = Font.render('Normal Enemy', True, White)
            display.blit(tekst, (120 + picture_rect.width, 200 + picture_rect.height/2 -
                                 tekst.get_height()/2))

            # Mineswepper fjende
            picture = pygame.transform.scale(pygame.image.load('Image/Fjender/Mineswepperfjendeimage.png')
                                             .convert_alpha(), (70, 70))
            picture_rect = picture.get_rect(topleft=(100, 300))
            display.blit(picture, picture_rect.topleft)

            tekst = Font.render('Mineswpper Enemy', True, White)
            display.blit(tekst, (120 + picture_rect.width, 300 + picture_rect.height/2 -
                                 tekst.get_height()/2))

            # Homming fjender
            picture = pygame.transform.scale(pygame.image.load('Image/Fjender/HommingFjendeImage.png')
                                             .convert_alpha(), (70, 70))
            picture_rect = picture.get_rect(topleft=(100, 400))
            display.blit(picture, picture_rect.topleft)

            tekst = Font.render('Homing Enemy', True, White)
            display.blit(tekst, (120 + picture_rect.width, 400 + picture_rect.height/2 -
                                 tekst.get_height()/2))

            # Heavy fjender
            picture = pygame.transform.scale(pygame.image.load('Image/Fjender/Heavyfjendeimage.png')
                                             .convert_alpha(), (70, 70))
            picture_rect = picture.get_rect(topleft=(100, 500))
            display.blit(picture, picture_rect.topleft)

            tekst = Font.render('Heavy Enemy', True, White)
            display.blit(tekst, (120 + picture_rect.width, 500 + picture_rect.height/2 -
                                 tekst.get_height()/2))

            # ----------------------------Info om Controls--------------------------------------------------
            # Overskrift
            controltekst = Font.render('Controls', True, Orange)
            display.blit(controltekst, (screenwith - screenwith/4 - controltekst.get_width()/2, 20))

            # Displayer controls
            tekst_render(Font, "Movement: W, A, S, D", (screenwith - screenwith / 4, 100), display, White, True)
            tekst_render(Font, "Shot Laser: ARROWS", (screenwith - screenwith / 4, 200), display, White, True)
            tekst_render(Font, "Place Mine: M", (screenwith - screenwith / 4, 300), display, White, True)
            tekst_render(Font, "Raise Shield: SPACE", (screenwith - screenwith / 4, 400), display, White, True)
            tekst_render(Font, "Teleport: TAB", (screenwith - screenwith / 4, 500), display, White, True)
            tekst_render(Font, "Pause Game: ESCAPE", (screenwith - screenwith / 4, 600), display, White, True)
            tekst_render(Font, "Show Debug Menu: H", (screenwith - screenwith / 4, 700), display, White, True)

            # return button
            if return_knap.draw(screenwith / 2-return_knap.width/2, screenheight-return_knap.height-10) is True:
                infoscreen = False

            mouse = pygame.mouse.get_pos()
            if return_knap.image_rect.collidepoint(mouse):
                click = True
            else:
                click = False

            mousecursor.update()
            mousecursor.draw(click=click)

            pygame.display.flip()

        # ------------------------------------------Skin Menu-----------------------------------------------------------
        while skinmeny:

            for eventskin in pygame.event.get():
                if eventskin.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if eventskin.type == pygame.MOUSEBUTTONDOWN:
                    laser_color = laserchangecolor.get_color_of_postion(pygame.mouse.get_pos(),
                                                                        laser_color)

            display.fill((0, 0, 0))
            baggrund.draw()

            playerskinselecter.draw("Player Skin")
            try:
                player.picture, player.damage_picture = playerskinselecter.buttondraw()
            except TypeError:
                pass
            player.update_picture()

            cursorskinselecter.draw("Cursor Skin")
            try:
                mousecursor.picture, mousecursor.picture_clik = cursorskinselecter.buttondraw()
            except TypeError:
                pass
            mousecursor.update_picture()

            if return_knap.draw(screenwith/2-returntogame_button.width/2,
                                screenheight-returntogame_button.height-10) is True:
                skinmeny = False
                
                with open('textfiler/skin', 'w') as file:
                    file.write(str(playerskinselecter.chosenskin) + '\n')
                    file.write(str(cursorskinselecter.chosenskin) + '\n')
                    file.write(str(laser_color).replace('(', '').replace(')', ''))

            mouse = pygame.mouse.get_pos()

            laserchangecolor.draw_color_grid()

            mousecursor.update()
            mousecursor.draw(click=click)

            if ((return_knap.image_rect.collidepoint(mouse) or
                    playerskinselecter.RightButton.image_rect.collidepoint(mouse) or
                    playerskinselecter.LeftButton.image_rect.collidepoint(mouse) or
                    cursorskinselecter.RightButton.image_rect.collidepoint(mouse) or
                    cursorskinselecter.LeftButton.image_rect.collidepoint(mouse)) or
                    laserchangecolor.collidemouse(mouse)):
                click = True
            else:
                click = False

            pygame.display.flip()

        # ----------------------------------------Option menu-----------------------------------------------------------
        while option:
            for event in pygame.event.get():
                pass

            display.fill((0, 0, 0))
            baggrund.draw()

            # Tegner sliderne
            tekst_render(Font, "Sound Effects", (screenwith/2, 100-lyd_slider.height), display, Orange, True)
            lyd_volume = lyd_slider.draw(screenwith/2-lyd_slider.width/2, 100)

            tekst_render(Font, "Music", (screenwith/2, 200-music_slider.height), display, Orange, True)
            pygame.mixer.music.set_volume(music_slider.draw(screenwith/2-music_slider.width/2, 200))

            # ændre lyd niveauet af de forskellige effekter
            lasersound.set_volume(lyd_volume)
            mineplacesound.set_volume(lyd_volume)
            teleportsound.set_volume(lyd_volume)
            enemydeadsound.set_volume(lyd_volume)

            if return_knap.draw(screenwith/2-returntogame_button.width/2, screenheight-returntogame_button.height-10):
                option = False

            mousecursor.update()
            mousecursor.draw(click=click)

            mouse = pygame.mouse.get_pos()
            if (return_knap.image_rect.collidepoint(mouse) or lyd_slider.rect.collidepoint(mouse) or
                    music_slider.rect.collidepoint(mouse)):
                click = True
            else:
                click = False

            pygame.display.flip()

        # ----------------------------------------Tilbage i main menu---------------------------------------------------

        display.fill((0, 0, 0))
        baggrund.draw()

        # displayer title
        tekst_render(Fontbig, "AstroBlast", (screenwith / 2, 100*scalar), display, White, True)
        tekst_render(Fontbig, "Apocalypse", (screenwith / 2, 190*scalar), display, White, True)

        # displayer highscore
        tekst_render(Font, f"Highscore: wave {highscore}", (screenwith / 2, 20), display, White, True)

        # displayer sjove ting i hjørnet
        tekst_render(Fontsmall, 'Created by Hveppe', (10, screenheight-50), display, White,
                     False)

        if startspil_knap.draw(screenwith/2-startspil_knap.width/2, screenheight/2-100) is True:
            mainmenu = False
            maingame = True
            new_wave_begin = time.time()

            # reset/start timer
            startgametime = time.time()

            # reset resten af tingene
            reset(Lasershot, Mineshot, Fjender, HeavyFjender, MineswepperFjender, HommingFjender, Astroids,
                  player, variabler, screenwith, screenheight)
            health_bar.max_hp = 5

        if infospil_knap.draw(screenwith/2-infospil_knap.width/2, screenheight/2-100+startspil_knap.height) is True:
            infoscreen = True

        if skin_knap.draw(screenwith/2-skin_knap.width/2, screenheight/2-100+infospil_knap.height*2) is True:
            skinmeny = True

        if quitgame_button.draw(screenwith/2-quitgame_button.width/2, screenheight/2-100+skin_knap.height*3) is True:
            pygame.quit()
            sys.exit()

        if options_button.draw(10, 10) is True:
            option = True

        mouse = pygame.mouse.get_pos()

        if (startspil_knap.image_rect.collidepoint(mouse) or infospil_knap.image_rect.collidepoint(mouse)
                or skin_knap.image_rect.collidepoint(mouse) or quitgame_button.image_rect.collidepoint(mouse))\
                or options_button.image_rect.collidepoint(mouse):
            click = True
        else:
            click = False

        mousecursor.update()
        mousecursor.draw(click=click)

        pygame.display.flip()

    # -------------------------------------Main Game-------------------------------------------------------------------
    while maingame:
        # Laver mousecursor usynlig
        pygame.mouse.set_visible(False)

        # sætter framerate til 60
        clock.tick(60)

        current = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # controls til PlayerClass
            if event.type == pygame.KEYDOWN:
                # Kode til at kontroler våben
                if event.type == pygame.KEYDOWN:

                    # Controls til laser
                    if event.key == pygame.K_UP:
                        variabler.lastmove = 'up'
                        variabler.shotting = True
                    if event.key == pygame.K_DOWN:
                        variabler.lastmove = 'down'
                        variabler.shotting = True
                    if event.key == pygame.K_LEFT:
                        variabler.lastmove = 'left'
                        variabler.shotting = True
                    if event.key == pygame.K_RIGHT:
                        variabler.lastmove = 'right'
                        variabler.shotting = True

                # controls til mine
                if event.key == pygame.K_m:
                    if variabler.ArsenalMines > 0 and variabler.shield_up is False:
                        variabler.ArsenalMines -= 1
                        Mineshot.append(LayMine(screen=display, xvalue=player.x + player.width / 2,
                                                yvalue=player.y + player.height / 2,
                                                picture=pygame.image.load("Image/Mines/mine.png").convert_alpha()))
                        mineplacesound.play()

                # control til shield
                if event.key == pygame.K_SPACE:
                    variabler.shield_up = True

                # Bevægelse af player
                if event.key == pygame.K_w:
                    player.ymove -= player.movespeed
                if event.key == pygame.K_s:
                    player.ymove += player.movespeed
                if event.key == pygame.K_d:
                    player.xmove += player.movespeed
                if event.key == pygame.K_a:
                    player.xmove -= player.movespeed
                if event.key == pygame.K_TAB:  # Teleporter player
                    if current - last_teleport >= 30:
                        player.x = random.randint(0, int(round(screenwith-player.width, 0)))
                        player.y = random.randint(0, int(round(screenwith-player.height, 0)))
                        last_teleport = time.time()
                        teleportsound.play()
                if event.key == pygame.K_h:
                    debug = True

            # Bruges til at modvirker controls
            if event.type == pygame.KEYUP:

                # modvirker bevægelse
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
                        variabler.shotting = True
                    else:
                        variabler.shotting = False

                if event.key == pygame.K_SPACE:
                    variabler.shield_up = False

            # pause spil
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = True

        if variabler.shotting is True and variabler.shield_up is False:
            if current - variabler.last_time_shot >= variabler.delaylaser:
                Lasershot.append(ShotLaser(screen=display, xvalue=player.x + player.width / 2 - 5,
                                           yvalue=player.y + player.height / 2 - 5, last_move=variabler.lastmove,
                                           color=laser_color))
                lasersound.play()
                variabler.last_time_shot = current

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

        for enemy in Fjender:
            if current - variabler.new_wave_begin >= variabler.new_wave_delay:
                enemy.update()

            enemy.draw()
            if collisionchecker(player, enemy) and enemy.dead is False:
                if variabler.shield_up:
                    pass
                else:
                    enemydeadsound.play()
                    variabler.lives -= 1
                    variabler.taking_damage_player, variabler.time_of_damage = taken_damage()
                    enemy.dead = True
                    enemy.timeofdeath = time.time()

            for lasershot in Lasershot:
                if collisionchecker(enemy, lasershot):
                    Lasershot.remove(lasershot)
                    variabler.minepoint += 1
                    enemydeadsound.play()
                    enemy.dead, enemy.timeofdeath = taken_damage()

            for Mine in Mineshot:
                if collisionchecker_circle_square(Mine, enemy):
                    Mineshot.remove(Mine)
                    enemydeadsound.play()
                    enemy.dead, enemy.timeofdeath = taken_damage()

        for enemy in HeavyFjender:
            if current - variabler.new_wave_begin >= variabler.new_wave_delay:
                enemy.update()

            enemy.draw()
            if collisionchecker(player, enemy) and enemy.dead is False:
                if variabler.shield_up:
                    pass
                else:
                    enemydeadsound.play()
                    variabler.lives -= enemy.lives
                    variabler.taking_damage_player, variabler.time_of_damage = taken_damage()
                    enemy.dead, enemy.timeofdeath = taken_damage()

            for lasershot in Lasershot:
                if collisionchecker(enemy, lasershot):
                    Lasershot.remove(lasershot)
                    enemydeadsound.play()

                    if enemy.lives <= 0:
                        variabler.minepoint += 3
                        enemy.dead, enemy.timeofdeath = taken_damage()
                    else:
                        enemy.lives -= 1

            for Mine in Mineshot:
                if collisionchecker_circle_square(Mine, enemy):
                    Mineshot.remove(Mine)
                    enemydeadsound.play()

                    if enemy.lives <= 0:
                        enemy.dead, enemy.timeofdeath = taken_damage()
                    else:
                        enemy.lives -= 1

        for enemy in MineswepperFjender:
            if current - variabler.new_wave_begin >= variabler.new_wave_delay:
                enemy.update()

            enemy.draw()

            if collisionchecker(player, enemy) and enemy.dead is False:
                if variabler.shield_up:
                    pass
                else:
                    enemydeadsound.play()
                    variabler.lives -= 1
                    variabler.taking_damage_player, variabler.time_of_damage = taken_damage()
                    enemy.dead, enemy.timeofdeath = taken_damage()

            for lasershot in Lasershot:
                if collisionchecker(enemy, lasershot):
                    Lasershot.remove(lasershot)
                    enemydeadsound.play()
                    variabler.minepoint += 1
                    enemy.dead, enemy.timeofdeath = taken_damage()

            for Mine in Mineshot:
                if collisionchecker_circle_square(Mine, enemy):
                    Mineshot.remove(Mine)

        for enemy in HommingFjender:
            if current - variabler.new_wave_begin >= variabler.new_wave_delay:
                enemy.update(player=player)

            enemy.draw()

            if collisionchecker(enemy, player) and enemy.dead is False:
                if variabler.shield_up:
                    pass
                else:
                    variabler.lives -= 1
                    enemydeadsound.play()
                    variabler.taking_damage_player, variabler.time_of_damage = taken_damage()
                    enemy.dead, enemy.timeofdeath = taken_damage()

            for lasershot in Lasershot:
                if collisionchecker(enemy, lasershot):
                    Lasershot.remove(lasershot)
                    enemydeadsound.play()
                    variabler.minepoint += 1
                    enemy.dead, enemy.timeofdeath = taken_damage()

            for Mine in Mineshot:
                if collisionchecker_circle_square(Mine, enemy):
                    Mineshot.remove(Mine)
                    enemydeadsound.play()
                    enemy.dead, enemy.timeofdeath = taken_damage()

        for astriod in Astroids:
            astriod.draw()
            astriod.move()

            if collisionchecker(player, astriod):
                variabler.lives = 0

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

        # ----------------------------------------Nye fjender bliver spawned når alle er døde
        if len(Fjender) == 0 and len(HeavyFjender) == 0 and len(MineswepperFjender) == 0 and len(HommingFjender) == 0:
            variabler.wave += 1
            variabler.new_wave_begin = time.time()

            if variabler.wave >= variabler.wavelives:
                if variabler.lives < 10:
                    variabler.lives += 1
                    if variabler.lives > health_bar.max_hp:
                        health_bar.max_hp += 1

                variabler.wavelives += 4

            if variabler.wave >= variabler.waveheavyspawn:
                variabler.antalfjenderheavy += 1
                variabler.waveheavyspawn += variabler.waveheavyspawnadd
                variabler.antalfjender -= 1
            else:
                variabler.antalfjender += 2

            if variabler.wave >= variabler.wavemineswepperspawn:
                variabler.antalfjendermineswpper += 1
                variabler.wavemineswepperspawn += variabler.wavemineswepperspawnadd

            if variabler.wave >= variabler.wavehommingspawn:
                variabler.antalfjenderhomming += 2
                variabler.antalfjender -= 2
                variabler.wavehommingspawn += variabler.wavehommingspawnadd

            if variabler.wave == variabler.changeinrate and variabler.waveheavyspawn > 1:
                variabler.waveheavyspawnadd -= 1
                variabler.changeinrate += 10

            for i in range(variabler.antalfjender):
                spawn_enemy(Fjender, EnemyClass, player, screenwith, screenheight, display,
                            random.randint(0, int(round(screenwith - 40*scalar, 0))),
                            random.randint(0, int(round(screenheight - 60*scalar, 0))), random.randint(1, 5),
                            random.randint(1, 10),
                            pygame.image.load('Image/Fjender/Normalfjendeimage.png').convert_alpha())

            for n in range(variabler.antalfjenderheavy):
                spawn_enemy(HeavyFjender, HeavyEnemyClass, player, screenwith, screenheight, display,
                            random.randint(0, int(round(screenwith - 60*scalar, 0))),
                            random.randint(0, int(round(screenheight - 60*scalar, 0))),
                            random.randint(1, 5), random.randint(1, 5),
                            pygame.image.load('Image/Fjender/Heavyfjendeimage.png').convert_alpha())

            for m in range(variabler.antalfjendermineswpper):
                spawn_enemy(MineswepperFjender, EnemyClass, player, screenwith, screenheight, display,
                            random.randint(0, int(round(screenwith - 40*scalar, 0))),
                            random.randint(0, int(round(screenheight - 40*scalar, 0))),
                            random.randint(1, 10), random.randint(1, 10),
                            pygame.image.load('Image/Fjender/Mineswepperfjendeimage.png').convert_alpha())

            for h in range(variabler.antalfjenderhomming):
                spawn_enemy(HommingFjender, HommingEnemyClass, player, screenwith, screenheight, display,
                            random.randint(0, int(round(screenwith - 50*scalar, 0))),
                            random.randint(0, int(round(screenheight - 50*scalar, 0))), 5, 5, pygame.image.load
                            ('Image/Fjender/HommingFjendeImage.png').convert_alpha())

        if variabler.shield_up is True and variabler.shield_charge > 0:
            shield.update(player)
            shield.draw()

            variabler.drain_time = time.time()

            if variabler.last_draintime is None:
                variabler.last_draintime = time.time()

            if variabler.drain_time - variabler.last_draintime >= variabler.drain_speed:
                variabler.shield_charge -= 1
                variabler.last_draintime = time.time()

            for enemy in Fjender:
                if collisionchecker_circle_square(shield, enemy) and enemy.dead is False:
                    enemydeadsound.play()
                    enemy.dead, enemy.timeofdeath = taken_damage()

            for enemy in HeavyFjender:
                if collisionchecker_circle_square(shield, enemy) and enemy.dead is False:
                    enemydeadsound.play()
                    variabler.shield_charge -= 2
                    enemy.dead, enemy.timeofdeath = taken_damage()

            for enemy in MineswepperFjender:
                if collisionchecker_circle_square(shield, enemy) and enemy.dead is False:
                    enemydeadsound.play()
                    enemy.dead, enemy.timeofdeath = taken_damage()

            for enemy in HommingFjender:
                if collisionchecker_circle_square(shield, enemy) and enemy.dead is False:
                    enemydeadsound.play()
                    enemy.dead, enemy.timeofdeath = taken_damage()

        if variabler.minepoint > 50:
            variabler.ArsenalMines += 1
            variabler.minepoint -= 50

        # Tegner player
        player.draw(variabler.taking_damage_player)
        player.update()

        # farver player rød når den tager skade
        if current - variabler.time_of_damage >= variabler.time_being_red:
            variabler.taking_damage_player = False

        # Kalder function til hver fjende type
        explosion_effekt(Fjender, current, variabler.explosion_time, explosion_effeckt, display)
        explosion_effekt(MineswepperFjender, current, variabler.explosion_time, explosion_effeckt, display)
        explosion_effekt(HeavyFjender, current, variabler.explosion_time, explosion_effeckt, display)
        explosion_effekt(HommingFjender, current, variabler.explosion_time, explosion_effeckt, display)

        # --------------------------------------------Debug menu--------------------------------------------------------
        if debug is True:
            # viser hitboxes
            player.draw_debug()

            for enemy in Fjender:
                enemy.draw_debug()

            for enemy in MineswepperFjender:
                enemy.draw_debug()

            for enemy in HeavyFjender:
                enemy.draw_debug()

            for enemy in HommingFjender:
                enemy.draw_debug()

            for mine in Mineshot:
                mine.draw_debug()

            for astriod in Astroids:
                astriod.draw_debug()

            # Displayer FPS
            tekst_render(Font, f"FPS: {int(round(clock.get_fps(), 0))}", (10, screenheight - 100), display, White,
                         False)

        # ---------------------------------------Main game igen---------------------------------------------------------
        health_bar.hp = variabler.lives
        health_bar.draw(display)

        tekst_render(Font, f"Wave: {variabler.wave}", (screenwith/2, 10), display, White, True)

        # tegener shield og teleport charge barerne
        shied_bar.hp = variabler.shield_charge
        shied_bar.draw(display)

        if current-last_teleport > 30:
            pass
        else:
            teleport_bar.hp = current-last_teleport
        teleport_bar.draw(display)

        tekst_render(Font, f"Mine: {variabler.ArsenalMines}", (screenwith-30, shied_bar.height*2+5), display, White,
                     None)

        if variabler.lives > 0:
            variabler.timer = time.time() - variabler.startgametime

        tekst_render(Font, f'Timer: {round(variabler.timer, 2)}', (10, health_bar.height+5), display, White, False)

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
                yastriond = random.randrange(screenheight + 100, screenheight + 200)
            elif direction == 4:
                xastriond = random.randrange(screenwith + 100, screenwith + 200)
                yastriond = random.randrange(1, screenheight)
            else:
                xastriond = 0
                yastriond = 0

            Astroids.append(AstroidClass(screen=display, xvalue=xastriond, yvalue=yastriond, speed=1,
                                         radius=50, direction=direction,
                                         picture=pygame.image.load("Image/effects/Asteroid.png").convert_alpha()))

        # Updater display
        pygame.display.flip()

        # ------------------------------------Pause screen--------------------------------------------------
        while pause is True:

            for eventpause in pygame.event.get():
                if eventpause.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if eventpause.type == pygame.KEYDOWN and eventpause.key == pygame.K_ESCAPE:
                    pause = False

            display.fill((0, 0, 0))
            baggrund.draw()

            pausetext = Fontbig.render('PAUSED', True, White)
            display.blit(pausetext,
                         (screenwith / 2 - pausetext.get_width() / 2, 10 + pausetext.get_height() / 2))

            if returntogame_button.draw(screenwith / 2 - returntogame_button.width / 2, screenheight / 2 - 70):
                pause = False
                player.xmove = 0
                player.ymove = 0

            if return_knap.draw(screenwith / 2 - return_knap.width / 2,
                                screenheight / 2 - 70 + returntogame_button.height):
                pause = False
                mainmenu = True
                maingame = False

            if quitgame_button.draw(screenwith / 2 - quitgame_button.width / 2,
                                    screenheight / 2 - 70 + returntogame_button.height * 2):
                if highscore < variabler.wave:
                    highscore = variabler.wave
                    with open('textfiler/highscore.txt', 'w') as file:
                        file.write(str(highscore))

                pygame.quit()
                sys.exit()

            mousecursor.update()
            mousecursor.draw(click=click)

            mouse = pygame.mouse.get_pos()
            if (return_knap.image_rect.collidepoint(mouse) or
                    returntogame_button.image_rect.collidepoint(mouse)
                    or quitgame_button.image_rect.collidepoint(mouse)):
                click = True
            else:
                click = False

            pygame.display.flip()

        # -------------------------------------Game Over----------------------------------------------------------------
        if variabler.lives <= 0:
            gameover = True
            gameoversound.play()

            if highscore < variabler.wave:
                highscore = variabler.wave
                with open('textfiler/highscore.txt', 'w') as file:
                    file.write(str(highscore))

            while gameover:
                # sætter framerate til 60
                clock.tick(60)

                # Farver baggrund
                display.fill((0, 0, 0))
                baggrund.draw()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                tekst_render(Fontbig, 'GAME OVER', (screenwith / 2, screenheight / 2 - 200), display, White, True)

                tekst_render(Font, f"WAVE: {variabler.wave}", (screenwith / 2, screenheight / 2 - 80), display, White,
                             True)

                tekst_render(Font, f"TIME: {round(variabler.timer, 2)}", (screenwith / 2, screenheight / 2 - 30),
                             display, White,
                             True)

                tekst_render(Font, f"Highscore: wave {highscore}", (screenwith / 2, 20), display, White, True)

                # Knapper til return til menu og quit game
                if quitgame_button.draw(screenwith/2-quitgame_button.width/2, screenheight-quitgame_button.height-10):
                    pygame.quit()
                    sys.exit()

                if return_knap.draw(screenwith/2-return_knap.width/2,
                                    screenheight-quitgame_button.height-10-return_knap.height) is True:
                    gameover = False
                    mainmenu = True
                    maingame = False

                mouse = pygame.mouse.get_pos()
                if return_knap.image_rect.collidepoint(mouse) or quitgame_button.image_rect.collidepoint(mouse):
                    click = True
                else:
                    click = False

                mousecursor.update()
                mousecursor.draw(click=click)

                pygame.display.flip()

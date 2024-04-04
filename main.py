# importer fra andre python filer
from Player import PlayerClass
from Shot_laser import ShotLaser

# importer libaries
import time
import pygame
import random

pygame.init()

# opsætting af skærm
screenwith, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((screenwith, screenheight))

# laver lister til classer der skal havde flere af gangen på skærmen
Lasershot = []

# laver player
player = PlayerClass(screen=display, xvalue=10, yvalue=10)

gamerunning = True

while gamerunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            gamerunning = False

        # controls til PlayerClass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.ymove -= player.movespeed
            if event.key == pygame.K_s:
                player.ymove += player.movespeed
            if event.key == pygame.K_d:
                player.xmove += player.movespeed
            if event.key == pygame.K_a:
                player.xmove -= player.movespeed
            if event.key == pygame.K_SPACE:
                Lasershot.append(ShotLaser(screen=display, xvalue=player.x+player.width/2,
                                           yvalue=player.y+player.height/2,
                                           speedx=player.xmove, speedy=player.ymove))

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

    # Updater display
    pygame.display.flip()

from Player import *
import time
import pygame

pygame.init()

# opsætting af skærm
screenwith, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((screenwith, screenheight))

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
    player.update()
    player.draw()

    # Updater display
    pygame.display.flip()

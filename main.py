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

    display.fill((0, 0, 0))

    player.draw()

    pygame.display.flip()

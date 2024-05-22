# Lavet af Hveppe

import time
import pygame

pygame.init()

# ---------------------------------------------Farver-------------------------------------------------------------------
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Yellow = (255, 255, 0)
Blue = (0, 0, 255)
DarkBlue = (0, 0, 200)
Orange = (255, 165, 0)
Grey = (128, 128, 128)
Purple = (128, 0, 128)
Pink = (212, 0, 255)
Cyan = (0, 255, 255)
Magenta = (255, 0, 255)
Silver = (192, 192, 192)

# -------------------------------------------Variabler------------------------------------------------------------------
debug = False

# finder scalar til fjender og player
scalar = pygame.display.Info().current_w/1500


class Variabler:
    def __init__(self):
        self.wave = 1
        self.waveheavyspawn = 5
        self.wavemineswepperspawn = 6
        self.wavehommingspawn = 7
        self.new_wave_delay = 0.1
        self.new_wave_begin = time.time()

        # andre ting
        self.lives = 5
        self.wavelives = 4
        self.minepoint = 0
        self.fjende_spawn = False
        self.taking_damage_player = False
        self.time_of_damage = time.time()
        self.time_being_red = 0.25
        self.explosion_time = 0.1
        self.ArsenalMines = 5

        # wave spawn ændringer
        self.waveheavyspawnadd = 5
        self.wavemineswepperspawnadd = 4
        self.wavehommingspawnadd = 4
        self.changeinrate = 10

        # laser
        self.delaylaser = 0.3
        self.last_time_shot = 0
        self.shotting = False
        self.lastmove = 'w'

        # shield varaibler
        self.shield_up = False
        self.shield_charge = 100
        self.drain_speed = 0.5
        self.last_draintime = None

        # giving time of start
        self.startgametime = time.time()
        self.timer = time.time()-self.startgametime

        self.antalfjender = 2
        self.antalfjenderheavy = 0
        self.antalfjendermineswpper = 0
        self.antalfjenderhomming = 0

    def reset(self):
        self.__init__()

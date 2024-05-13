# Lavet af Hveppe

import time

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

# -------------------------------------------Variabler------------------------------------------------------------------
debug = False


class Variabler:
    wave = 1
    waveheavyspawn = 5
    wavemineswepperspawn = 6
    wavehommingspawn = 7
    new_wave_delay = 0.1
    new_wave_begin = time.time()

    # andre ting
    lives = 5
    wavelives = 4
    minepoint = 0
    fjende_spawn = False
    taking_damage_player = False
    time_of_damage = time.time()
    time_being_red = 0.25
    explosion_time = 0.1

    # wave spawn ændringer
    waveheavyspawnadd = 5
    wavemineswepperspawnadd = 4
    wavehommingspawnadd = 4
    changeinrate = 10

    # laser
    delaylaser = 0.3
    last_time_shot = 0
    shotting = False
    lastmove = 'w'
    laser_color = Blue

    # shield varaibler
    shield_up = False
    shield_charge = 100
    drain_speed = 0.5
    last_draintime = None

    # giving time of start
    startgametime = time.time()
    timer = time.time()-startgametime

    antalfjender = 2
    antalfjenderheavy = 0
    antalfjendermineswpper = 0
    antalfjenderhomming = 0

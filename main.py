"""
Filename : window.py
Author : Archit
Date Created : 2/11/2025
Description : 
Language : python3
"""
import pygame as pg
import os
from dino import Dino

# Window constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

# Background constants
BACKGROUND_IMAGE = pg.image.load("assets/Other/Track.png")
BACKGROUND_CLOUD_IMAGE = pg.image.load("assets/Other/Cloud.png")
GAME_OVER_IMAGE = pg.image.load("assets/Other/GameOver.png")
RESET_IMAGE = pg.image.load("assets/Other/Reset.png")


def main():
    pg.init()
    screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption("Dino Game")
    clock = pg.time.Clock()
    dino = Dino()

    # Main loop
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Fill the screen with white

        dino.draw(screen)
        dino.update(pg.key.get_pressed())

        pg.display.flip()
        clock.tick(60)

    pg.quit()


main()

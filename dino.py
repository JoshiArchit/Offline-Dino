"""
Filename : dino.py
Author : Archit
Date Created : 2/11/2025
Description : Encapsulates the dino class for the dinosaur character
Language : python3
"""
import pygame as pg

# Asset constants
DINO_RUNNING_IMAGE = [pg.image.load("assets/Dino/DinoRun1.png"),
                      pg.image.load("assets/Dino/DinoRun2.png")]
DINO_JUMPING_IMAGE = pg.image.load("assets/Dino/DinoJump.png")
DINO_DUCKING_IMAGE = [pg.image.load("assets/Dino/DinoDuck1.png"),
                      pg.image.load("assets/Dino/DinoDuck2.png")]
DINO_STARTING_IMAGE = pg.image.load("assets/Dino/DinoStart.png")


class Dino:
    x_pos = 80
    y_pos = 310

    def __init__(self):
        # Image initialization
        self.duck_image = DINO_DUCKING_IMAGE
        self.run_image = DINO_RUNNING_IMAGE
        self.jump_image = DINO_JUMPING_IMAGE
        self.start_image = DINO_STARTING_IMAGE

        # Image state
        self.duck = False
        self.run = True
        self.jump = False

        self.steps = 0
        self.image = self.run_image[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

    def update(self, user_input):
        if self.run:
            self.dino_run()
        if self.jump:
            self.dino_jump()
        if self.duck:
            self.dino_duck()

        # Key events
        if user_input[pg.K_UP] and not self.jump:
            self.run = False
            self.jump = True
            self.duck = False
        elif user_input[pg.K_DOWN] and not self.jump:
            self.run = False
            self.jump = False
            self.duck = True
        elif not self.jump and not user_input[pg.K_DOWN]:
            self.run = True
            self.jump = False
            self.duck = False

    def dino_run(self):
        self.image = self.run_image[(self.steps // 5) % 2]  # Ensures index is always 0 or 1
        self.steps += 1
        if self.steps >= 10:  # Reset steps to keep it within a valid range
            self.steps = 0
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

    def dino_jump(self):
        pass

    def dino_duck(self):
        pass

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

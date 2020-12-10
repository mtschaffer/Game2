import os
import math
from random import randint

import pygame

from camera.camera import camera
from scene import state
from utils.audio import audio
from utils.screen_shake import screen_shake

class Player:
    def __init__(self, x=320, y=240):
        self.x = x
        self.y = y

        self.image = pygame.image.load(os.path.join('images', 'fuzzy.png')).convert_alpha()

        self.input_teleport = False

    def input(self, model, keystate, previous_keystate):
        self.reset_buffered_input()

        if keystate[pygame.K_SPACE] and not previous_keystate[pygame.K_SPACE]:
            audio.play_sfx('belup')
            self.input_teleport = True

            state.offset = screen_shake(2, 3)
            state.screen_shaking = True

    def reset_buffered_input(self):
        self.input_teleport = False

    def teleport(self, model):
        self.x = randint(32, 608)
        self.y = randint(32, 448)

    def update(self, model, lag_scalar):
        if self.input_teleport:
            self.teleport(model)

    def draw(self, screen):
        w, h = self.image.get_size()
        camera.blit(self.image, (self.x - w / 2, self.y - h / 2))

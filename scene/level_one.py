from itertools import combinations
from random import randint

import pygame

from characters.player import Player
from scene import state
from utils.audio import audio
from utils.text import Text


class LevelOneModel:
    _instance = None

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = LevelOneModel()

        return cls._instance

    @classmethod
    def clear_instance(cls):
        cls._instance = None

    def __init__(self):
        ## Foreground
        # A list of all on-screen elements.

        self.player = Player()
        self.welcome = Text("Welcome to Teamgame2!", 320, 100, 48, center=True)
        self.welcome2 = Text("Press [SPACE] to move", 320, 160, 24, center=True)


def enter(scene_args):
    audio.stop_all()
    audio.play_bgm('bg-music')

    model = LevelOneModel.instance()


def exit():
    LevelOneModel.clear_instance()


def draw(screen):
    model = LevelOneModel.instance()
    model.player.draw(screen)

    if model.welcome:
        model.welcome.draw(screen)
    if model.welcome2:
        model.welcome2.draw(screen)


def update(lag_scalar):
    model = LevelOneModel.instance()

    # Remove welcome text
    if model.welcome and state.time > 10000:
        model.welcome = None
    if model.welcome2 and state.time > 10000:
        model.welcome2 = None

    model.player.update(model, lag_scalar)


def input(keystate, previous_keystate):
    model = LevelOneModel.instance()
    model.player.input(model, keystate, previous_keystate)

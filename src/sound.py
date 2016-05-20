# coding: utf-8

import pygame

class SoundWorld(object):
    def __init__(self):
        self._mixer=pygame.mixer
        self._mixer.init()
        self._crashSound = pygame.mixer.Sound("../crash.wav")
        self._overtakeSound = pygame.mixer.Sound("../overtakeSound.wav")

    def crash(self):
        self._mixer.Sound.play(self._crashSound)
    def ambientSound(self):
        self._mixer.music.load("../ambience.wav")
        self._mixer.music.play(-1)
        
    def overtake(self):
        self._mixer.Sound.play(self._overtakeSound)



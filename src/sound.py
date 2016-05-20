# coding: utf-8

import pygame
class SoundWorld:
    def __init__(self):
        self._mixer=pygame.mixer
        self._mixer.init()
        self._crashSound = pygame.mixer.Sound("../crash.wav")
        self._overtakeSound = pygame.mixer.Sound("../overtakeSound.wav")
        self._honkSound = pygame.mixer.Sound("../honk.wav")
    def crash(self):
        self._mixer.Sound.play(self._crashSound)
    def honk(self):
        self._mixer.Sound.play(self._honkSound)
    def ambientSound(self):
        self._mixer.music.load("../ambience.wav")
        self._mixer.music.play(-1)
        
    def overtake(self):
        self._mixer.Sound.play(self._overtakeSound)

    def ambulSiren(self):
        self._mixer.music.load("../ambulance.wav")
        self._mixer.music.play(3)



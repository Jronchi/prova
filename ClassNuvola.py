import pygame
import os
import random

class Nuvola:
    def __init__(self, immagine, min, max, larghezza_schermo):
        self.larghezza_schermo = larghezza_schermo
        self.x = self.larghezza_schermo + random.randint(min, max) #prima 800,1000
        self.y = random.randint(80, 200)
        self.image = immagine
        self.larghezza = self.image.get_width() 

    def update(self, game_speed):
        self.x -= game_speed + 3
        if self.x < -self.larghezza:
            self.x = self.larghezza_schermo + random.randint (2500, 3000)
            self.y = random.randint (60, 160)

    def draw(self, SCREEN, immagine):
        SCREEN.blit(immagine, (self.x, self.y))

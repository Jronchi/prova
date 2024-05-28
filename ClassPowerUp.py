import pygame
import os
import random

class PowerUp:
    def __init__(self, image, larghezza_schermo):
        self.larghezza_schermo = larghezza_schermo
        self.image = image
        self.hitbox = self.image.get_rect()
        self.hitbox.x = self.larghezza_schermo + random.randint(100, 300)
        self.hitbox.y = random.randint(300, 400)

    def update(self, game_speed):
        self.hitbox.x -= game_speed
        a = random.randint(0, 750)
        if self.hitbox.x < -self.hitbox.width:
            if a == 370:
                self.hitbox.x = self.larghezza_schermo + random.randint(300, 900)
                self.hitbox.y = random.randint(300, 400)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.hitbox.x, self.hitbox.y))



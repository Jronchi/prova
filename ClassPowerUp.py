import pygame
import os
import random

class PowerUp:
    def __init__(self, image, larghezza_schermo):
        self.larghezza_schermo = larghezza_schermo
        self.image = image
        self.hitbox = self.image.get_rect()
        self.hitbox.x = random.randint(larghezza_schermo + 100, larghezza_schermo + 300)
        self.hitbox.y = 390

    def update(self, game_speed):
        self.hitbox.x -= game_speed
        a = random.randint(0, 15)
        if self.hitbox.x < -self.hitbox.width:
            if a == 1:
                self.hitbox.x = random.randint(self.larghezza_schermo + 100, self.larghezza_schermo + 300)
                self.hitbox.y = random.randint(300, 400)
            else:
                self.hitbox.x += game_speed

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.hitbox.x, self.hitbox.y))
       
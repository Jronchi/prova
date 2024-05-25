import pygame
import os
import random

class PowerUp:
    def __init__(self, image, larghezza_schermo):
        self.larghezza_schermo = larghezza_schermo
        self.image = image
        self.hitbox = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        # Genera una nuova posizione x randomica fuori dallo schermo
        self.hitbox.x = random.randint(self.larghezza_schermo + 50, self.larghezza_schermo + 900)
        # Genera una nuova posizione y randomica all'interno di un intervallo specificato
        self.hitbox.y = random.randint(300, 400)

    def update(self, game_speed):
        self.hitbox.x -= game_speed
        if self.hitbox.x < -self.hitbox.width:
            # Sposta il powerup fuori dallo schermo e poi lo riposiziona randomicamente
            if random.random() < 0.05:  # 5% di probabilità di spawnare un nuovo powerup
                self.reset_position()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.hitbox.x, self.hitbox.y))
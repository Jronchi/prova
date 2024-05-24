import pygame
import os
import random

class PowerUp:
    def __init__(self, larghezza_schermo):
        self.larghezza_schermo = larghezza_schermo
        self.image = pygame.image.load(os.path.join("level_up.png"))
        self.hitbox = self.image.get_rect()
        self.hitbox.x = random.randint(larghezza_schermo + 100, larghezza_schermo + 300)
        self.hitbox.y = 390

    def update(self, game_speed):
        self.hitbox.x -= game_speed
        if self.hitbox.x < -self.hitbox.width:
            self.hitbox.x = random.randint(self.larghezza_schermo + 100, self.larghezza_schermo + 300)
            self.hitbox.y = random.randint(300, 400)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.hitbox.x, self.hitbox.y))
       
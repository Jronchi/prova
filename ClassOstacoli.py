import pygame
import os
import random

class Ostacoli:
    def __init__(self, image, type, larghezza_schermo): 
        self.image = image
        self.type = type
        self.hitbox = self.image[self.type].get_rect()
        self.hitbox.x += larghezza_schermo 
    
    def update(self, game_speed, ostacoli):
        self.hitbox.x -= game_speed
        if self.hitbox.x < -self.hitbox.width:
            ostacoli.remove(self)

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.hitbox)

class Pianta(Ostacoli):                      #si pottrebbe fare tmp che controlla che non sia troppo vicino a x
    def __init__(self, image, larghezza_schermo):
        self.type = random.randint(0, 1)     
        super().__init__(image, self.type, larghezza_schermo)
        self.hitbox.y = 400
        self.hitbox.x += random.randint(600, 800)

class Bassi(Ostacoli):
    def __init__(self, image, larghezza_schermo):
        self.type = random.randint(0, 3)
        super().__init__(image, self.type, larghezza_schermo)
        self.hitbox.y = 430
        self.hitbox.x += random.randint(100, 400)

class Bird(Ostacoli):
    def __init__(self, image, larghezza_schermo):
        self.type = 0
        super().__init__(image, self.type, larghezza_schermo)
        self.hitbox.y = 310
        self.index = 0
    
    def draw(self, SCREEN): #il draw in Ostacoli non basta perchè è animata
        if self.index >= 30:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.hitbox)
        self.index += 1
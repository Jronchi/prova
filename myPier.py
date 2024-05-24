import pygame
import os
import random

pygame.init()

# IMMAGINI:
running = [pygame.image.load(os.path.join("immagini/Personaggio", "pier_run(1).png")), pygame.image.load(os.path.join("immagini/Personaggio", "pier_run(2.2).png")), pygame.image.load(os.path.join("immagini/Personaggio", "pier_run(1).png")), pygame.image.load(os.path.join("immagini/Personaggio", "pier_run(3.2).png"))]   
# 4 immagini perchè ha 3 pose ma torna alla prima 2 volte
jumping = pygame.image.load(os.path.join("immagini/Personaggio", "pier_jump.png"))

downing = [pygame.image.load(os.path.join("immagini/Personaggio", "pier_down.png")), pygame.image.load(os.path.join("immagini/Personaggio", "pier_down.png")), pygame.image.load(os.path.join("immagini/Personaggio", "pier_down.png")), pygame.image.load(os.path.join("immagini/Personaggio", "pier_down.png"))]   

dying = [pygame.image.load(os.path.join("immagini/Personaggio/death", "pier_death(1).png")), pygame.image.load(os.path.join("immagini/Personaggio/death", "pier_death(2).png")), pygame.image.load(os.path.join("immagini/Personaggio/death", "pier_death(2.2).png")), pygame.image.load(os.path.join("immagini/Personaggio/death", "pier_death(3).png")), pygame.image.load(os.path.join("immagini/Personaggio/death", "pier_death(3.2).png")), pygame.image.load(os.path.join("immagini/Personaggio/death", "pier_death(4).png")), pygame.image.load(os.path.join("immagini/Personaggio/death", "pier_death(4.2).png")),pygame.image.load(os.path.join("immagini/Personaggio/death", "pier_death(5).png")), pygame.image.load(os.path.join("immagini/Personaggio/death", "pier_death(5.2).png")), pygame.image.load(os.path.join("immagini/Personaggio/death", "pier_death(6).png")), pygame.image.load(os.path.join("immagini/Personaggio/death", "pier_death(7).png")), pygame.image.load(os.path.join("immagini/Personaggio/death", "pier_death(8).png")), pygame.image.load(os.path.join("immagini/Personaggio/death", "pier_death(9).png")), pygame.image.load(os.path.join("immagini/Personaggio/death", "pier_death(10).png")),]

powerup_image = pygame.image.load(os.path.join("level_up.png"))

class Pier:
    X = 50
    Y = 380
    Y_down = 405
    VEL_jump = 8.5  #velocità salto

    def __init__(self):
        self.run_img = running
        self.jump_img = jumping
        self.down_img = downing
        self.death_img = dying

        self.pier_run = True
        self.pier_jump = False
        self.pier_down = False
        self.pier_death = False

        self.step_index = 0
        self.index_death = 0
        self.vel_jump = self.VEL_jump
        self.image = self.run_img[0]
        self.pier_hitbox = self.image.get_rect()
        self.pier_hitbox.x = self.X
        self.pier_hitbox.y = self.Y

        self.immortal = False
        self.immortal_time_left = 0

        self.flag = False

    def update(self, userInput):
        if self.pier_run:
            self.Run()
        if self.pier_jump:
            self.Jump()
        if self.pier_down:
            self.Down()
        if self.pier_death:
            self.Death()
        
        if self.step_index >= 12:      # 12 multiplo del divisore in run
            self.step_index = 0

        if (userInput [pygame.K_UP] or userInput [pygame.K_SPACE]) and not self.pier_jump:
            self.pier_run = False
            self.pier_jump = True
            self.pier_down = False
        elif userInput [pygame.K_DOWN] and not self.pier_jump:
            self.pier_run = False
            self.pier_jump = False
            self.pier_down = True
        elif not (self.pier_jump or userInput[pygame.K_DOWN]):
            self.pier_run = True
            self.pier_jump = False
            self.pier_down = False
        if self.immortal:
            self.immortal_time_left -= 1
            if self.immortal_time_left <= 0:
                self.immortal = False

    def Run(self):   # step_index serve per far cambiare le immagini mentre corre
        self.image = self.run_img[self.step_index // 3] # 12:3 = 4 che è il numero di immagini che voglio 
        self.pier_hitbox = self.image.get_rect()
        self.pier_hitbox.x = self.X
        self.pier_hitbox.y = self.Y
        self.step_index += 1

    def Jump(self):
        self.image = self.jump_img
        if self.pier_jump:                        # velocità diminuisce mentre sale e aumenta menre scende
            self.pier_hitbox.y -= self.vel_jump * 4
            self.vel_jump -= 0.7
        if self.vel_jump < - self.VEL_jump:
            self.pier_jump = False
            self.vel_jump = self.VEL_jump
    
    def Down(self):
        self.image = self.down_img[self.step_index // 3]
        self.pier_hitbox = self.image.get_rect()
        self.pier_hitbox.x = self.X
        self.pier_hitbox.y = self.Y_down
        self.step_index +=1

    def Death(self):
        self.image = self.death_img[self.index_death]
        self.pier_hitbox = self.image.get_rect()
        self.pier_hitbox.x = self.X
        self.pier_hitbox.y = self.Y
        if self.index_death < 13:
            self.index_death += 1
        else:
            self.flag = True
            return 

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.pier_hitbox.x, self.pier_hitbox.y))

    def activate_powerup(self):
        self.immortal = True
        self.immortal_time_left = 100  # durata dell'immortalità in frames

class PowerUp:
    def init(self):
        self.image = powerup_image
        self.hitbox = self.image.get_rect()
        self.hitbox.x = random.randint(600, 800)
        self.hitbox.y = random.randint(300, 400)

    def update(self):
        self.hitbox.x -= 5
        if self.hitbox.x < -self.hitbox.width:
            self.hitbox.x = random.randint(600, 800)
            self.hitbox.y = random.randint(300, 400)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.hitbox.x, self.hitbox.y))

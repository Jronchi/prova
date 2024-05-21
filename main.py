import pygame
import os
import random

pygame.init()

# SCHERMATA DI GIOCO:
altezza_schermo = 600
larghezza_schermo = 1100
SCREEN = pygame.display.set_mode((larghezza_schermo, altezza_schermo))

# ostacoli vari:
pianta = [pygame.image.load(os.path.join("immagini/Ostacoli", "plant.png")), pygame.image.load(os.path.join("immagini/Ostacoli", "plant.png"))]
bassi = [pygame.image.load(os.path.join("immagini/Ostacoli", "bomb.png")), pygame.image.load(os.path.join("immagini/Ostacoli", "sasso.png"))]

# elementi del paesaggio:
terreno = pygame.image.load(os.path.join("immagini/Paesaggio", "terreno.png"))
nuvola1 = pygame.image.load(os.path.join("immagini/Paesaggio", "nuvole(1).png"))
nuvola2 = pygame.image.load(os.path.join("immagini/Paesaggio", "nuvole(2).png"))

from myPier import Pier

class Nuvola:
    def __init__(self, immagine, min, max):
        self.x = larghezza_schermo + random.randint(min, max) #prima 800,1000
        self.y = random.randint(80, 200)
        self.image = immagine
        self.larghezza = self.image.get_width() 

    def update(self):
        self.x -= game_speed
        if self.x < -self.larghezza:
            self.x = larghezza_schermo + random.randint (2500, 3000)
            self.y = random.randint (60, 160)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Ostacoli:
    def __init__(self, image, type): 
        self.image = image
        self.type = type
        self.hitbox = self.image[self.type].get_rect()
        self.hitbox.x = larghezza_schermo 
    
    def update(self):
        self.hitbox.x -= game_speed
        if self.hitbox.x < -self.hitbox.width:
            ostacoli.remove(self)

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.hitbox)

class Pianta(Ostacoli):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.hitbox.y = 400
        self.hitbox.x += random.randint(634, 867)

class Bassi(Ostacoli):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.hitbox.y = 430
        self.hitbox.x += random.randint(133, 397)

def main(): 
    global game_speed, x_sfondo, y_sfondo, punteggio, ostacoli
    run = True 
    clock = pygame.time.Clock()
    player = Pier()
    cloud1 = Nuvola(nuvola1, 400, 700)
    cloud2 = Nuvola(nuvola2, 1000, 1700)
    game_speed = 12
    x_sfondo = 0
    y_sfondo = 455
    punteggio = 0
    record = 0
    font = pygame.font.Font("freesansbold.ttf", 20)
    ostacoli = []
    death_count = 0

    def score():
        global punteggio, game_speed
        if not player.pier_death == True:
            punteggio += 0.4
        if punteggio % 100 == 0:
            game_speed += 1
        
        text = font.render("Punteggio: " + str(int(punteggio)), True, (0, 0, 0))
        text_hitbox = text.get_rect()
        text_hitbox.center = 1000, 40
        SCREEN.blit(text, text_hitbox)

        text = font.render("Record: " + str(int(record)), True, (0, 0, 0))
        text_hitbox = text.get_rect()
        text_hitbox.center = 70, 40
        SCREEN.blit(text, text_hitbox)

    def sfondo():
        global x_sfondo, y_sfondo
        image_widht = terreno.get_width()
        SCREEN.blit(terreno, (x_sfondo, y_sfondo))
        SCREEN.blit(terreno, (image_widht + x_sfondo, y_sfondo))
        if x_sfondo <= -image_widht:
            SCREEN.blit(terreno, (image_widht + x_sfondo, y_sfondo))
            x_sfondo = -25
        x_sfondo -= game_speed

    while run:
        # per uscire 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        SCREEN.fill((120,150,255))   #azzurro cielo (120, 150, 255)
        userInput = pygame.key.get_pressed()

        sfondo()

        cloud2.draw(SCREEN)
        cloud2.update()
        cloud1.draw(SCREEN)
        cloud1.update()

        player.draw(SCREEN)
        player.update(userInput)

        if len(ostacoli) < 2:
            a = random.randint(0, 2)
            if a == 0:
                ostacoli.append(Bassi(bassi))
            elif a == 2:
                ostacoli.append(Pianta(pianta))
        
        score()

        for ostacolo in ostacoli:
            ostacolo.draw(SCREEN)
            ostacolo.update()
            if player.pier_hitbox.colliderect(ostacolo.hitbox):

                if punteggio > record:
                    record = punteggio
                game_speed = 0
                pygame.draw.rect(SCREEN, (120, 150, 255), pygame.Rect(850, 0, 400, 60))
                death_count += 1

                pygame.time.delay(40)
                player.pier_death = True
            
            #if player.pier_hitbox.colliderect(ostacolo.hitbox) and type(ostacolo) == Bassi:
                
                

        clock.tick(35)     #la velocità con cui si muove
        pygame.display.update()

main()
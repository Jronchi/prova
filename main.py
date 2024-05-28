import pygame
import os
import random
import time

pygame.init()
pygame.mixer.init()

# SCHERMATA DI GIOCO:
altezza_schermo = 600
larghezza_schermo = 1100
SCREEN = pygame.display.set_mode((larghezza_schermo, altezza_schermo))
pygame.display.set_caption('Pier Run')

# PIER:
pier_img = pygame.image.load(os.path.join("immagini/Personaggio", "pier.png"))

# OSTACOLI:
pianta = [pygame.image.load(os.path.join("immagini/Ostacoli", "plant(1).png")), pygame.image.load(os.path.join("immagini/Ostacoli", "plant(2).png"))]
pianta_nott = [pygame.image.load(os.path.join("immagini/Ostacoli", "plant_nott.png")), pygame.image.load(os.path.join("immagini/Ostacoli", "plant_nott.png"))]


bassi = [pygame.image.load(os.path.join("immagini/Ostacoli", "log(2).png")), pygame.image.load(os.path.join("immagini/Ostacoli", "log(2).png")), pygame.image.load(os.path.join("immagini/Ostacoli", "bomb(1).png")), pygame.image.load(os.path.join("immagini/Ostacoli", "log(2).png"))]

uccello = [pygame.image.load(os.path.join("immagini/Bird", "bird(1).png")), pygame.image.load(os.path.join("immagini/Bird", "bird(2).png")), pygame.image.load(os.path.join("immagini/Bird", "bird(3).png")), pygame.image.load(os.path.join("immagini/Bird", "bird(4).png")), pygame.image.load(os.path.join("immagini/Bird", "bird(5).png")), pygame.image.load(os.path.join("immagini/Bird", "bird(6).png"))]
uccello_nott = [pygame.image.load(os.path.join("immagini/Bird", "bird(1)_nott.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(2)_nott.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(3)_nott.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(4)_nott.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(5)_nott.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(6)_nott.png"))]

# PAESAGGIO
terreno = pygame.image.load(os.path.join("immagini/Paesaggio", "terreno.png"))
terreno_nott = pygame.image.load(os.path.join("immagini/Paesaggio", "terreno_nott.png"))

nuvola1 = pygame.image.load(os.path.join("immagini/Paesaggio", "nuvole(1).png"))
nuvola2 = pygame.image.load(os.path.join("immagini/Paesaggio", "nuvole(2).png"))

nuvola_nott1 = pygame.image.load(os.path.join("immagini/Paesaggio", "nuvole(1)_nott.png"))
nuvola_nott2 = pygame.image.load(os.path.join("immagini/Paesaggio", "nuvole(2)_nott.png"))

# SUONI:
suonomorte = pygame.mixer.Sound("sounds/suonomorte1.mp3")
corsa = pygame.mixer.Sound("sounds/corsa1.mp3")
#loss = pygame.mixer.Sound("loss.mp3")
home_menu = pygame.mixer.Sound("sounds/menu.mp3")
corsapower = pygame.mixer.Sound("sounds/corsapuneo.mp3")
activation = pygame.mixer.Sound("sounds/activate.mp3")

#POWER UP 
immagine_powerUp = pygame.image.load(os.path.join("immagini/other", "level_up.png"))

from ClassPier import Pier
from ClassNuvola import Nuvola
from ClassOstacoli import Pianta, Bassi, Bird
from ClassPowerUp import PowerUp

record = 0

def main(): 
    global game_speed, x_terreno, y_terreno, punteggio, ostacoli, record
    run = True 
    orario = 500
    punteggio = 0
    clock = pygame.time.Clock()
    player = Pier()
    cloud1 = Nuvola(nuvola1, 400, 700, larghezza_schermo)
    cloud2 = Nuvola(nuvola2, 1000, 1700, larghezza_schermo) 
    game_speed = 12
    x_terreno = 0
    y_terreno = 455
    font = pygame.font.Font("freesansbold.ttf", 20)
    ostacoli = []
    powerup = PowerUp(immagine_powerUp, larghezza_schermo)
    death_count = 0
    avvio = True
    corsa.play()
    corsa.set_volume(0.5)
    corsapower.play()
    corsapower.set_volume(0.0)

    def score():
        global punteggio, game_speed
        if not player.pier_death == True:
            punteggio += 0.35
        if punteggio % 100 == 0:
            game_speed += 1
        
        if punteggio < orario: 
            text = font.render("Punteggio: " + str(int(punteggio)), True, (0, 0, 0))
        else:
            text = font.render("Punteggio: " + str(int(punteggio)), True, (255, 255, 255))

        text_hitbox = text.get_rect()
        text_hitbox.center = 1000, 40
        SCREEN.blit(text, text_hitbox)

        if punteggio < orario: 
            text = font.render("Record: " + str(int(record)), True, (0, 0, 0))
        else:
            text = font.render("Record: " + str(int(record)), True, (255, 255, 255))

        text_hitbox = text.get_rect()
        text_hitbox.center = 70, 40
        SCREEN.blit(text, text_hitbox)

    def suolo():
        global x_terreno, y_terreno
        if punteggio < orario:
            image_widht = terreno.get_width()
            SCREEN.blit(terreno, (x_terreno, y_terreno))
            SCREEN.blit(terreno, (image_widht + x_terreno, y_terreno))
            if x_terreno <= -image_widht + 200:
                SCREEN.blit(terreno, (image_widht + x_terreno, y_terreno))
                x_terreno = -25
            x_terreno -= game_speed

        if punteggio >= orario:
            image_widht_n = terreno_nott.get_width()
            SCREEN.blit(terreno_nott, (x_terreno, y_terreno))
            SCREEN.blit(terreno_nott, (image_widht_n + x_terreno, y_terreno))
            if x_terreno <= -image_widht_n + 200:
                SCREEN.blit(terreno_nott, (image_widht_n + x_terreno, y_terreno))
                x_terreno = -25
            x_terreno -= game_speed

    while run:
        # per uscire 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                corsa.stop()
                corsapower.stop()

        colore_giorno = (120,150,255) #azzurro cielo (120, 150, 255)
        colore_crepuscolo = (80, 90,180)
        colore_notte = (17,20,50)
         
        if punteggio + 100 < orario:
            SCREEN.fill(colore_giorno)  
        elif punteggio < orario:
            SCREEN.fill(colore_crepuscolo)
        elif punteggio >= orario:
            SCREEN.fill(colore_notte)

        userInput = pygame.key.get_pressed()

        #landscape()
        suolo()

        if punteggio < orario:
            cloud2.draw(SCREEN, nuvola2)
            cloud2.update(game_speed)
            cloud1.draw(SCREEN, nuvola1)
            cloud1.update(game_speed)
        else:
            cloud2.draw(SCREEN, nuvola_nott2)
            cloud2.update(game_speed)
            cloud1.draw(SCREEN, nuvola_nott1)
            cloud1.update(game_speed)

        player.draw(SCREEN)
        player.update(userInput)
        
        powerup.draw(SCREEN)
        powerup.update(game_speed)

        if len(ostacoli) < 2:
            a = random.randint(0, 2)
            if a == 0:
                ostacoli.append(Bassi(bassi, larghezza_schermo))
            elif a == 2:
                if punteggio + 20 < orario: 
                    ostacoli.append(Pianta(pianta, larghezza_schermo))
                else:
                    ostacoli.append(Pianta(pianta_nott, larghezza_schermo)) 
            elif a == 1 and punteggio > 200:
                if punteggio + 20 < orario: 
                    ostacoli.append(Bird(uccello, larghezza_schermo))
                else:
                    ostacoli.append(Bird(uccello_nott, larghezza_schermo))
        
        score()

        for ostacolo in ostacoli:
            ostacolo.draw(SCREEN)
            ostacolo.update(game_speed, ostacoli)
            if player.pier_hitbox.colliderect(ostacolo.hitbox) and not player.immortal:

                if punteggio > record:
                    record = punteggio
                game_speed = 0
                death_count += 1

                pygame.time.delay(40)
                player.pier_death = True
                
                if player.pier_death and avvio:
                    suonomorte.play()
                    suonomorte.set_volume(1.0)
                    avvio = False
                    corsa.stop()
                    corsapower.stop()
                    #loss.play()
                    #loss.set_volume(0.2)

        if not player.immortal:
            game_speed = 10
            activation.stop()
            corsa.set_volume(0.5)
            corsapower.set_volume(0.0)
            if player.pier_death:
                game_speed = 0
        
        if player.pier_hitbox.colliderect(powerup.hitbox):
            player.activate_powerup()
            powerup.hitbox.y = 1000
            corsa.set_volume(0.0)
            
            if player.immortal:
                player.immortal_time_left -= 1
                game_speed = 20
                activation.stop()
                activation.play()
                activation.set_volume(0.4)
                corsapower.set_volume(0.5)
                if player.immortal_time_left <= 0:
                    player.immortal = False

        if player.flag:
            menu(death_count)

            
        clock.tick(35)     #la velocità con cui si muove
        pygame.display.update()

def menu(death_count):
    global record
    run = True
    corsa.stop()
    #loss.stop()
    home_menu.play()
    home_menu.set_volume(0.5)

    while run:
        SCREEN.fill((50,50,50))
        font1 = pygame.font.Font("freesansbold.ttf", 80)
        font2 = pygame.font.Font("freesansbold.ttf", 30)

        # RETTANGOLO DI START
        size = (300, 150)
        pos = (400, 225)
        
        colore_r1 = (40,40,40)
        colore_r2 = (240, 240, 240)
        r1 = pygame.Rect(pos[0], pos[1], size[0], size[1])
        r2 = pygame.Rect(pos[0]-5, pos[1]-5, size[0]+10, size[1]+10)
        pygame.draw.rect(SCREEN, colore_r2, r2)
        pygame.draw.rect(SCREEN, colore_r1, r1)

        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if r1.collidepoint(pos):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    home_menu.stop()
                    main()

        if death_count == 0:
            text = font1.render("START", True, (colore_r2))
        elif death_count > 0:
            text = font1.render("START", True, (colore_r2))
            score = font2.render("Il tuo record: " + str(int(record)), True, (colore_r2))
            score_hitbox = score.get_rect()
            score_hitbox.center = (larghezza_schermo // 2, altezza_schermo // 2 + 150)
            SCREEN.blit(score, score_hitbox)

        text_hitbox = text.get_rect()
        text_hitbox.center = (larghezza_schermo // 2, altezza_schermo // 2)
        SCREEN.blit(text, text_hitbox)

        pier_img_s = pygame.transform.scale(pier_img, (70, 104))
        SCREEN.blit(pier_img_s, (larghezza_schermo // 2 - 100, altezza_schermo // 2 - 183))
        pygame.display.update()

menu(death_count = 0)
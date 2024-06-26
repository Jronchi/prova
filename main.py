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
pianta_nott = [pygame.image.load(os.path.join("immagini/Ostacoli", "plant(1)_nott.png")), pygame.image.load(os.path.join("immagini/Ostacoli", "plant(2)_nott.png"))]
pianta_inf = [pygame.image.load(os.path.join("immagini/Ostacoli", "plant_inf.png")), pygame.image.load(os.path.join("immagini/Ostacoli", "plant_inf.png"))]

bassi = [pygame.image.load(os.path.join("immagini/Ostacoli", "log(2).png")), pygame.image.load(os.path.join("immagini/Ostacoli", "log(2).png")), pygame.image.load(os.path.join("immagini/Ostacoli", "bomb(1).png")), pygame.image.load(os.path.join("immagini/Ostacoli", "log(2).png"))]

uccello = [pygame.image.load(os.path.join("immagini/Bird", "bird(1).png")), pygame.image.load(os.path.join("immagini/Bird", "bird(2).png")), pygame.image.load(os.path.join("immagini/Bird", "bird(3).png")), pygame.image.load(os.path.join("immagini/Bird", "bird(4).png")), pygame.image.load(os.path.join("immagini/Bird", "bird(5).png")), pygame.image.load(os.path.join("immagini/Bird", "bird(6).png"))]
uccello_nott = [pygame.image.load(os.path.join("immagini/Bird", "bird(1)_nott.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(2)_nott.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(3)_nott.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(4)_nott.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(5)_nott.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(6)_nott.png"))]
uccello_inf = [pygame.image.load(os.path.join("immagini/Bird", "bird(1)_inf.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(2)_inf.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(3)_inf.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(4)_inf.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(5)_inf.png")), pygame.image.load(os.path.join("immagini/Bird", "bird(6)_inf.png"))]

# PAESAGGIO
terreno = pygame.image.load(os.path.join("immagini/Paesaggio", "terreno.png"))
terreno_nott = pygame.image.load(os.path.join("immagini/Paesaggio", "terreno_nott.png"))
terreno_inf = pygame.image.load(os.path.join("immagini/Paesaggio", "terreno_inferno.png"))

nuvola1 = pygame.image.load(os.path.join("immagini/Paesaggio", "nuvole(1).png"))
nuvola2 = pygame.image.load(os.path.join("immagini/Paesaggio", "nuvole(2).png"))

nuvola_nott1 = pygame.image.load(os.path.join("immagini/Paesaggio", "nuvole(1)_nott.png"))
nuvola_nott2 = pygame.image.load(os.path.join("immagini/Paesaggio", "nuvole(2)_nott.png"))

nuvola_inf1 = pygame.image.load(os.path.join("immagini/Paesaggio", "nuvole(1)_inf.png"))
nuvola_inf2 = pygame.image.load(os.path.join("immagini/Paesaggio", "nuvole(2)_inf.png"))

# SUONI:
suonomorte = pygame.mixer.Sound("sounds/suonomorte1.mp3")
corsa = pygame.mixer.Sound("sounds/corsa1.mp3")
loss = pygame.mixer.Sound("sounds/loss.mp3")
home_menu = pygame.mixer.Sound("sounds/menu.mp3")
corsapower = pygame.mixer.Sound("sounds/corsapuneo.mp3")
activation = pygame.mixer.Sound("sounds/activate.mp3")

#ALTRO
immagine_powerUp = pygame.image.load(os.path.join("immagini/other", "level_up.png"))
imm_game_over = pygame.image.load(os.path.join("immagini/other", "game_over.png"))
imm_logo = pygame.image.load(os.path.join("immagini/other", "logo_PR.png"))
sfondo_menu = pygame.image.load(os.path.join("immagini/other", "sfondo_menu.png"))

from ClassPier import Pier
from ClassNuvola import Nuvola
from ClassOstacoli import Pianta, Bassi, Bird
from ClassPowerUp import PowerUp

NERO = (0,0,0)
BIANCO = (255,255,255)

record = 0

def main(): 
    global game_speed, x_terreno, y_terreno, punteggio, ostacoli, record
    run = True 
    orario_notte = 450
    orario_inferno = 800
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
    avvioloss = False
    
    # COLORI DELLE ORE DEL GIORNO:
    colore_giorno = (120,150,255) #azzurro cielo (120, 150, 255)
    colore_crepuscolo = (80, 90,180)
    colore_notte = (17,20,50)
    colore_inferno = (130, 110, 100)

    # SETTAGGI PER AUDIO
    corsa.play()
    corsa.set_volume(0.7)
    corsapower.play()
    corsapower.set_volume(0.0)

    def score():
        global punteggio, game_speed
        if not player.pier_death == True:
            punteggio += 0.35
        if punteggio % 100 == 0:
            game_speed += 1
        
        if punteggio < orario_notte: 
            text = font.render("Punteggio: " + str(int(punteggio)), True, NERO)
        elif punteggio >= orario_notte and punteggio < orario_inferno:
            text = font.render("Punteggio: " + str(int(punteggio)), True, BIANCO)
        elif punteggio >= orario_inferno:
            text = font.render("Punteggio: " + str(int(punteggio)), True, NERO)

        text_hitbox = text.get_rect()
        text_hitbox.center = 1000, 40
        SCREEN.blit(text, text_hitbox)

        if punteggio < orario_notte: 
            text = font.render("Record: " + str(int(record)), True, NERO)
        elif punteggio >= orario_notte and punteggio < orario_inferno:
            text = font.render("Record: " + str(int(record)), True, BIANCO)
        elif punteggio >= orario_inferno:
            text = font.render("Record: " + str(int(record)), True, NERO)

        text_hitbox = text.get_rect()
        text_hitbox.center = 70, 40
        SCREEN.blit(text, text_hitbox)

    def suolo():
        global x_terreno, y_terreno
        if punteggio < orario_notte:
            image_widht = terreno.get_width()
            SCREEN.blit(terreno, (x_terreno, y_terreno))
            SCREEN.blit(terreno, (image_widht + x_terreno, y_terreno))
            if x_terreno <= -image_widht + 200:
                SCREEN.blit(terreno, (image_widht + x_terreno, y_terreno))
                x_terreno = -25
            x_terreno -= game_speed

        if punteggio >= orario_notte and punteggio < orario_inferno:
            image_widht = terreno_nott.get_width()
            SCREEN.blit(terreno_nott, (x_terreno, y_terreno))
            SCREEN.blit(terreno_nott, (image_widht + x_terreno, y_terreno))
            if x_terreno <= -image_widht + 200:
                SCREEN.blit(terreno_nott, (image_widht + x_terreno, y_terreno))
                x_terreno = -25
            x_terreno -= game_speed
        
        if punteggio >= orario_inferno:
            image_widht = terreno_inf.get_width()
            SCREEN.blit(terreno_inf, (x_terreno, y_terreno))
            SCREEN.blit(terreno_inf, (image_widht + x_terreno, y_terreno))
            if x_terreno <= -image_widht + 200:
                SCREEN.blit(terreno_inf, (image_widht + x_terreno, y_terreno))
                x_terreno = -25
            x_terreno -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                corsa.stop()
                corsapower.stop()
                loss.stop()
         
        if punteggio + 50 < orario_notte:
            SCREEN.fill(colore_giorno)  
        elif punteggio < orario_notte:
            SCREEN.fill(colore_crepuscolo)
        elif punteggio >= orario_notte and punteggio < orario_inferno:
            SCREEN.fill(colore_notte)
        elif punteggio >= orario_inferno:
            SCREEN.fill(colore_inferno)

        userInput = pygame.key.get_pressed()

        suolo()

        if punteggio < orario_notte:
            cloud2.draw(SCREEN, nuvola2)
            cloud2.update(game_speed)
            cloud1.draw(SCREEN, nuvola1)
            cloud1.update(game_speed)
        elif punteggio < orario_inferno:
            cloud2.draw(SCREEN, nuvola_nott2)
            cloud2.update(game_speed)
            cloud1.draw(SCREEN, nuvola_nott1)
            cloud1.update(game_speed)
        else:
            cloud2.draw(SCREEN, nuvola_inf2)
            cloud2.update(game_speed)
            cloud1.draw(SCREEN, nuvola_inf1)
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
                if punteggio + 25 < orario_notte: 
                    ostacoli.append(Pianta(pianta, larghezza_schermo))
                elif punteggio + 25 < orario_inferno:
                    ostacoli.append(Pianta(pianta_nott, larghezza_schermo)) 
                elif punteggio -25 >= orario_inferno:
                   ostacoli.append(Pianta(pianta_inf, larghezza_schermo))  
            elif a == 1 and punteggio > 200:
                if punteggio + 25 < orario_notte: 
                    ostacoli.append(Bird(uccello, larghezza_schermo))
                elif punteggio + 25 < orario_inferno:
                    ostacoli.append(Bird(uccello_nott, larghezza_schermo))
                elif punteggio -25 >= orario_inferno:
                    ostacoli.append(Bird(uccello_inf, larghezza_schermo))
    
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

        if not player.immortal:
            game_speed = 10
            activation.stop()
            corsa.set_volume(0.7)
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
                activation.set_volume(0.2)
                corsapower.set_volume(0.7)
                if player.immortal_time_left <= 0:
                    player.immortal = False

        if player.flag:
            if not avvioloss:
                loss.play()
                loss.set_volume(0.4)
                avvioloss = True
            menu_morte(death_count)
            
        clock.tick(35)     #la velocità con cui si muove
        pygame.display.update()

def menu_morte(death_count):
    colore_menu_morte = (0, 0, 0, 190)  # trasparenza 
    menu_surface = pygame.Surface((larghezza_schermo, altezza_schermo), pygame.SRCALPHA)
    menu_surface.fill(colore_menu_morte)
    SCREEN.blit(menu_surface, (0, 0))

    font1 = pygame.font.Font(None, 30)
    text = font1.render("PREMI UN TASTO QUALSIASI", True, BIANCO)
    text_hitbox = text.get_rect()
    text_hitbox.center = (larghezza_schermo // 2, altezza_schermo // 2 + 80)
    SCREEN.blit(text, text_hitbox)

    size = (200, 70)
    pos = (880, 510)

    # RETTANGOLO DI MENU 
    colore_r1 = (255, 255, 255)
    r1 = pygame.Rect(pos[0], pos[1], size[0], size[1])
    pygame.draw.rect(SCREEN, colore_r1, r1, 5)
    font2 = pygame.font.Font("freesansbold.ttf", 30)
    text2 = font2.render("Menu", True, BIANCO)
    text2_hitbox = text2.get_rect()
    text2_hitbox.center = (980, 545)
    SCREEN.blit(text2, text2_hitbox)

    SCREEN.blit(imm_game_over, (larghezza_schermo //2 -320, altezza_schermo // 2 - 90))
    pygame.display.update()

    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os.sys()

        if r1.collidepoint(pos):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                loss.stop()
                menu_principale(death_count)

        if event.type == pygame.KEYDOWN:
            loss.stop()
            main()

    
def menu_principale(death_count):
    global record
    run = True
    corsa.stop()
    home_menu.play()
    home_menu.set_volume(0.8)

    x_pier_menu =  random.randint(70, larghezza_schermo - 70)
    y_pier_menu = - 100

    while run:
        SCREEN.blit(sfondo_menu, (0, 0))
        font1 = pygame.font.Font(None, 30)
        font2 = pygame.font.Font(None, 30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                os.sys()
            if event.type == pygame.KEYDOWN:
                    home_menu.stop()
                    main()

        if death_count == 0:
            text = font1.render("PREMI UN TASTO QUALSIASI", True, NERO)
        elif death_count > 0:
            text = font1.render("PREMI UN TASTO QUALSIASI", True, NERO)
            score = font2.render("Record di sessione: " + str(int(record)), True, NERO)
            score_hitbox = score.get_rect()
            score_hitbox.center = (130, altezza_schermo // 2 + 280)
            SCREEN.blit(score, score_hitbox)

        SCREEN.blit(imm_logo, (larghezza_schermo //2 -320, altezza_schermo // 2 - 90))

        text_hitbox = text.get_rect()
        text_hitbox.center = (larghezza_schermo // 2, altezza_schermo // 2 + 100)
        SCREEN.blit(text, text_hitbox)
        y_pier_menu += 3

        if y_pier_menu > altezza_schermo:
            a = random.randint(0,1100)

            if a == 30:
                x_pier_menu =  random.randint(0, larghezza_schermo)
                y_pier_menu = - 100

        pier_img_s = pygame.transform.scale(pier_img, (65, 100))
        SCREEN.blit(pier_img_s, (x_pier_menu, y_pier_menu))
        pygame.display.update()

menu_principale(death_count = 0)
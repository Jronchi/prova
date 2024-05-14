import pygame
import os

pygame.init()

# SCHERMATA DI GIOCO:
altezza_schermo = 600
larghezza_shermo = 1100
SCREEN = pygame.display.set_mode((larghezza_shermo, altezza_schermo))

# IMMAGINI:

# corsa = [pygame.image.load(os.path.join("immagini/Skibidi", "SkibiRun1.png")), pygame.image.load(os.path.join   ("immagini/Skibi", "SkibiRun2.png"))]   # lista di 2 immagini perchè quando corre cabia

# salto = [pygame.image.load(os.path.join("immagini/Skibidi", "SkibiJump.png"))]

# abbassato = [pygame.image.load(os.path.join("immagini/Skibidi", "SkibiDown1.png")), pygame.image.load(os.path.join("immagini/Skibidi", "SkibiDown2.png"))]

# ostacoli vari:

# elementi del paesaggio:

# -----------------------------------------------

# SKIBIDI
#class Skibidi:
#    x = 80
#    y = 300

#    def __init__(self):
#        self.giù = abbassato

def main(): 
    run = True 
    clock = pygame.time.Clock()
    #player = Skibidi()

    while run:
        # per uscire
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        SCREEN.fill((255,255,255))
        userInput = pygame.key.get_pressed()

        #player.draw(SCREEN)
        #player.update(userInput)

        #clock.tick(30)
        #pygame.display.update()

main()
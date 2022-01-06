import sys, pygame
import numpy as np
import time
#import matplotlib.pyplot as plt
pygame.init()

# Ancho y alto de la pantalla
size = width, height = 600, 600

# Número de celdas
nXC = 40
nYC = 40

# Dimensiones de la celda
dimCW = (width - 1) / nXC
dimCH = (width - 1) / nYC

# Color del fondo --> casi negro, casi oscuro
bg = 25, 25, 25

# Creación de la pantalla
screen = pygame.display.set_mode(size)

# Pintamos el fondo del color elegido
screen.fill(bg)

# Estado de las celdas. Vivas = 1; Muertas = 0
gameState = np.zeros((nXC, nYC))

# Autómata palo
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1

# Autómata móvil
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

# Control de la ejecunción del juego
pauseExect = False

# Bucle de ejecución
while True:

    new_gameState = np.copy(gameState)
    screen.fill(bg)
    time.sleep(0.1)

    # Registramos eventos de teclado y ratón
    ev = pygame.event.get()

    for event in ev:
        # Detectamos si se pulsa una tecla
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        # Detectamos si se presiona el raton
        mouseClick = pygame.mouse.get_pressed()
        #print(mouseClick)

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            new_gameState[celX, celY] = not mouseClick[2]


    for y in range(0, nYC):
        for x in range(0, nXC):

            if not pauseExect:

                # Calculamos el número de vecinos cercanos
                n_neigh = gameState[(x - 1) % nXC, (y - 1) % nYC] + \
                          gameState[(x)     % nXC, (y - 1) % nYC] + \
                          gameState[(x + 1) % nXC, (y - 1) % nYC] + \
                          gameState[(x - 1) % nXC, (y) % nYC] + \
                          gameState[(x + 1) % nXC, (y) % nYC] + \
                          gameState[(x - 1) % nXC, (y + 1) % nYC] + \
                          gameState[(x)     % nXC, (y + 1) % nYC] + \
                          gameState[(x +1 ) % nXC, (y + 1) % nYC]

                # print(n_neigh)

                # Rule #1: Una célula muerta con exactamente 3 células vecinas vivas, "nace".
                if gameState[x, y] == 0 and n_neigh == 3:
                    new_gameState[x, y] = 1

                # Rule #2: Una célula viva con 2 o 3 células vivas sigue con vida, en otro caso muere (por "soledad" o "superpoblación").
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    new_gameState[x, y] = 0


            # Creamos el polígo de cada celda a dibujar.
            poly = [((x)   * dimCW, (y) * dimCH),
                    ((x+1) * dimCW, (y) * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]

            # Y dibujamos la celda para cada par x e y.
            if new_gameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # Actualizamos el estado del juego
    gameState = np.copy(new_gameState)

    # Actualizamos la pantalla
    pygame.display.flip()
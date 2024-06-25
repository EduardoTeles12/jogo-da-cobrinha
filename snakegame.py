import pygame
import random

# Inicialização do Pygame e dos sons
pygame.init()
pygame.mixer.init()

# Definindo as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Configurações da janela do jogo
WINDOW_SIZE = (600, 400)
GRID_SIZE = 20
GRID_WIDTH = WINDOW_SIZE[0] // GRID_SIZE
GRID_HEIGHT = WINDOW_SIZE[1] // GRID_SIZE

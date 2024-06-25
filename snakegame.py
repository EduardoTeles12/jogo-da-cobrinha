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

# Configurações da cobra
INITIAL_LENGTH = 3
SNAKE_SPEED = 10

# Direções
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Carregando os sons
eat_sound = pygame.mixer.Sound("comendomaca.wav")
game_over_sound = pygame.mixer.Sound("burro_-burro.wav")
pygame.mixer.music.load("V E N O M - T Á F I C A N D O A P E R T A D O.mp3")
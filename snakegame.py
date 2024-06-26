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
game_over_sound = pygame.mixer.Sound("Burro_-Burro.wav")
pygame.mixer.music.load("V E N O M - T Á F I C A N D O A P E R T A D O.mp3")

# Carregando a imagem da maçã
apple_image = pygame.image.load("04-14.png")
apple_image = pygame.transform.scale(apple_image, (GRID_SIZE, GRID_SIZE))  # Redimensiona a imagem para o tamanho da grade

# Carregando imagens do menu
menu_bg = pygame.image.load("snake.png")
menu_bg = pygame.transform.scale(menu_bg, WINDOW_SIZE)

# Carregando imagens do game over
game_over_bg = pygame.image.load("images.png")
game_over_bg = pygame.transform.scale(game_over_bg, WINDOW_SIZE)

# Função para desenhar a cobra
def draw_snake(screen, snake):
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Função para exibir o menu inicial
def show_start_screen(screen):
    screen.blit(menu_bg, (0, 0))  # Desenha a imagem de fundo do menu inicial

    font = pygame.font.Font(None, 36)
    text = font.render("Pressione Enter para iniciar", True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 - 50))
    screen.blit(text, text_rect)

    font = pygame.font.Font(None, 24)
    text = font.render("Nome do jogador:", True, WHITE)
    screen.blit(text, (WINDOW_SIZE[0] // 2 - 220, WINDOW_SIZE[1] // 2 + 20)) 

    input_rect = pygame.Rect(WINDOW_SIZE[0] // 2 - 40, WINDOW_SIZE[1] // 2 + 20, 200, 30)
    pygame.draw.rect(screen, WHITE, input_rect, 2)

    pygame.display.flip()

    player_name = ""
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]  # Apaga o último caractere
                elif event.unicode.isalnum():  # Aceita apenas caracteres alfanuméricos
                    player_name += event.unicode

        input_surface = font.render(player_name, True, WHITE)
        screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.draw.rect(screen, WHITE, input_rect, 2)

        pygame.display.flip()

    return player_name

# Função para exibir o menu de jogo novamente (game over)
def show_game_over_screen(screen):
    pygame.mixer.music.stop()  # Parar música de fundo ao chegar ao game over
    screen.blit(game_over_bg, (0, 0))  # Desenha a imagem de fundo do game over

    font = pygame.font.Font(None, 36)
    text = font.render("Game Over - Pressione Enter para jogar novamente ou Shift para sair", True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
    screen.blit(text, text_rect)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.play(-1)  # Reinicia música de fundo ao jogar novamente
                    waiting = False
                elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    pygame.quit()
                    quit()
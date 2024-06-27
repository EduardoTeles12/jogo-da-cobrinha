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
pygame.mixer.music.set_volume(0.2)  # Define o volume inicial da música de fundo


# Carregando a imagem da maçã
apple_image = pygame.image.load("04-14.png")
apple_image = pygame.transform.scale(apple_image, (GRID_SIZE, GRID_SIZE)) 

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
    screen.blit(menu_bg, (0, 0))  

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
                    player_name = player_name[:-1]  
                elif event.unicode.isalnum():  
                    player_name += event.unicode

        input_surface = font.render(player_name, True, WHITE)
        screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.draw.rect(screen, WHITE, input_rect, 2)

        pygame.display.flip()

    return player_name

# Função para exibir a tela de game over
def show_game_over_screen(screen, apple_count):
    pygame.mixer.music.stop()  # Parar música de fundo ao chegar ao game over
    screen.blit(game_over_bg, (0, 0))  

    font = pygame.font.Font(None, 27)
    text = font.render(f"Maçãs comidas: {apple_count}", True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 50))
    screen.blit(text, text_rect)

    text = font.render("Pressione Enter para jogar novamente ou Shift para sair", True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 100))
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

# Função principal do jogo
def main():
    global screen

    # Inicialização da tela do jogo
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('COBRAO GAME')

    # Tocar música de fundo em loop
    pygame.mixer.music.play(-1)

    while True:  # Loop para permitir jogar novamente
        player_name = show_start_screen(screen)
        print("Nome do jogador:", player_name)

        # Variáveis para o jogo
        apple_count = 0

        # Inicialização da cobra
        snake = [[GRID_WIDTH // 2, GRID_HEIGHT // 2]]
        snake_direction = RIGHT
        snake_length = INITIAL_LENGTH

        # Posição inicial da maçã
        apple = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]

        # Controle de tempo
        clock = pygame.time.Clock()

        # Loop principal do jogo
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Verificação contínua das teclas pressionadas
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and snake_direction != DOWN:
                snake_direction = UP
            elif keys[pygame.K_DOWN] and snake_direction != UP:
                snake_direction = DOWN
            elif keys[pygame.K_LEFT] and snake_direction != RIGHT:
                snake_direction = LEFT
            elif keys[pygame.K_RIGHT] and snake_direction != LEFT:
                snake_direction = RIGHT

            # Movimento da cobra
            new_head = [snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1]]

            # Verificação de colisão da cobra com as bordas
            if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
                running = False

            # Verificação de colisão da cobra com ela mesma
            if new_head in snake[1:]:
                running = False

            # Verificação de colisão da cobra com a maçã
            if new_head == apple:
                apple = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]
                snake_length += 1
                apple_count += 1
                eat_sound.play()  # Reproduzir som ao comer a maçã
            else:
                snake.pop()

            snake.insert(0, new_head)

            # Desenhar na tela
            screen.fill(BLACK)
            draw_snake(screen, snake)
            screen.blit(apple_image, (apple[0] * GRID_SIZE, apple[1] * GRID_SIZE))  # Desenha a imagem da maçã

            # Exibir nome do jogador e quantidade de maçãs comidas
            font = pygame.font.Font(None, 27)
            text = font.render(f"Jogador: {player_name}  |  Maçãs comidas: {apple_count}", True, WHITE)
            screen.blit(text, (10, 10))

            pygame.display.flip()

            # Controle de velocidade da cobra
            clock.tick(SNAKE_SPEED)

        # Após sair do loop principal (jogo terminado)
        game_over_sound.play()  # Reproduzir som de game over
        show_game_over_screen(screen, apple_count)

if __name__ == "_main_":
    main()
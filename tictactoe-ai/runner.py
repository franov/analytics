import pygame
import sys
import time
import pathlib

# Importa el código de con la función Minimax
import tictactoe as ttt

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

fontPath = pathlib.Path.joinpath(pathlib.Path(__file__).parent.resolve(), "OpenSans-Regular.ttf")


mediumFont = pygame.font.Font(fontPath, 26)
largeFont = pygame.font.Font(fontPath, 40)
moveFont = pygame.font.Font(fontPath, 60)

user = None
board = ttt.initial_state()
ai_turn = False

running = True  # Variable para controlar el bucle del juego

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Salir del bucle del juego
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Maneja los eventos de clics del mouse aquí si es necesario
            pass

    screen.fill(black)

    # Let user choose a player.
    if user is None:

        # Draw title
        title = largeFont.render("Juega Tic-Tac-Toe", True, white)
        subtitle = mediumFont.render("#GATO", True, white)
        titleRect = title.get_rect()
        subtitleRect = subtitle.get_rect()
        titleRect.center = ((width / 2), 50)
        subtitleRect.center = ((width / 2), 100)
        screen.blit(title, titleRect)
        screen.blit(subtitle, subtitleRect)

        # Draw buttons
        playXButton = pygame.Rect((width / 8), (height / 2), width / 3, 50)
        playX = mediumFont.render("Juega con X", True, black)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, white, playXButton)
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect(4.5 * (width / 8), (height / 2), width / 3, 50)
        playO = mediumFont.render("Juega con O", True, black)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, white, playOButton)
        screen.blit(playO, playORect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.X
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.O

    else:

        # Draw game board
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != ttt.EMPTY:
                    move = moveFont.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = ttt.terminal(board)
        player = ttt.player(board)

        # Show title
        if game_over:
            winner = ttt.winner(board)
            if winner is None:
                title = f"Game Over: Empate."
            else:
                title = f"Game Over: {winner} gana."
        elif user == player:
            title = f"Jugando como {user}"
        else:
            title = f"Máquina pensando..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        # Check for AI move
        if user != player and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = ttt.minimax(board)
                board = ttt.result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        # Check for a user move
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if (board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse)):
                        board = ttt.result(board, (i, j))

        if game_over:
            againButton = pygame.Rect(width / 4, height - 65, width / 2, 50)
            again = mediumFont.render("Juega nuevamente", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    board = ttt.initial_state()
                    ai_turn = False

    pygame.display.flip()

pygame.quit()  # Cerrar Pygame correctamente
sys.exit()  # Salir del programa

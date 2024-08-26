"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Retorna el estado inicial del tablero.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Determina cuál jugador tiene el siguiente turno en el tablero dado.

    El jugador "X" siempre comienza el juego. Luego, los jugadores se alternan en cada turno.
    Esta función cuenta cuántas veces han jugado "X" y "O" para determinar a quién le toca jugar.

    Parámetros:
    board (list of list): El estado actual del tablero, representado por una lista de listas.
                          Cada sublista representa una fila del tablero.

    Retorno:
    str: "X" si es el turno de X, "O" si es el turno de O.
    """
    
    # Contar el número de veces que "X" y "O" aparecen en el tablero
    X_count = sum(row.count(X) for row in board)
    O_count = sum(row.count(O) for row in board)
    
    return X if X_count == O_count else O


def actions(board):
    """
    Devuelve un conjunto de todas las acciones posibles en el tablero dado.
    
    Una acción es una tupla (i, j) donde 'i' es el índice de la fila y 'j' es el índice
    de la columna. Las acciones solo se pueden realizar en casillas que están vacías
    (es decir, que contienen 'None').

    Parámetros:
    board (list of list): El estado actual del tablero, representado por una lista de listas.
                          Cada sublista representa una fila del tablero.

    Retorno:
    set: Un conjunto de todas las acciones posibles, representadas como tuplas (i, j).
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                actions.add((i, j))
                
    return actions

def result(board, action):
    """
    Devuelve el nuevo estado del tablero que resulta de aplicar la acción dada.

    Esta función no modifica el tablero original. En su lugar, realiza una copia del
    tablero, aplica la acción en la copia, y devuelve el tablero modificado.

    Parámetros:
    board (list of list): El estado actual del tablero, representado por una lista de listas.
                          Cada sublista representa una fila del tablero.
    action (tuple): Una tupla (i, j) que indica la posición donde el jugador actual
                    desea realizar su movimiento.

    Retorno:
    list of list: Un nuevo tablero, reflejando el estado después de aplicar la acción.
    
    Excepciones:
    ValueError: Si la acción no es válida (por ejemplo, si la casilla ya está ocupada).
    """
    # Extraer las coordenadas de la acción
    i, j = action
    
    # Verificar si la casilla en la posición (i, j) ya está ocupada
    if board[i][j] is not EMPTY:
        raise ValueError("Acción de juego inválida")
    
    else:
        # Hacer una copia profunda del tablero original para evitar modificarlo
        new_board = [row[:] for row in board]#board.copy()
        # Aplicar el movimiento del jugador actual en la casilla (i, j)
        new_board[i][j] = player(board)
        
        # Devolver el nuevo tablero que refleja el movimiento
        return new_board
        

def winner(board):
    """
    Determina si hay un ganador en el tablero.

    Un jugador gana si logra alinear tres de sus símbolos consecutivamente en una fila,
    columna o diagonal. Si hay un ganador, la función devuelve "X" o "O" según corresponda.
    Si no hay un ganador, la función devuelve None.

    Parámetros:
    board (list of list): El estado actual del tablero, representado por una lista de listas.
                          Cada sublista representa una fila del tablero.

    Retorno:
    str or None: "X" si el jugador X ha ganado, "O" si el jugador O ha ganado,
                 o None si no hay ningún ganador.
    """
    for i in range(3):
        # Verificar filas en busca de un ganador
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        # Verificar columnas en busca de un ganador
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Verifica la diagonal principal en busca de un ganador
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    
    # Verifica la diagonal secundaria en busca de un ganador
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    # Si no se encontró ganador, devuelve None
    return None

def terminal(board):
    """
    Determina si el juego ha terminado.

    El juego se considera terminado si hay un ganador o si todas las casillas del tablero
    están llenas, lo que indica un empate.

    Parámetros:
    board (list of list): El estado actual del tablero, representado por una lista de listas.
                          Cada sublista representa una fila del tablero.

    Retorno:
    bool: True si el juego ha terminado, ya sea por una victoria o por empate.
          False si el juego aún está en curso.
    """
    # Verificar si todas las casillas están llenas
    #for row in board:
    #    for cell in row:
    #        if cell is EMPTY:
    #            return False  # El juego no ha terminado porque aún hay casillas vacías
    
    # Si no hay ganador y no hay casillas vacías, el juego ha terminado en empate
    #return True

    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

def utility(board):
    """
    Devuelve la utilidad del tablero terminal.

    La utilidad se define como:
    - 1 si "X" ha ganado.
    - -1 si "O" ha ganado.
    - 0 si el juego ha terminado en empate.

    Se asume que la función solo se llama en un estado terminal del tablero.

    Parámetros:
    board (list of list): El estado actual del tablero, representado por una lista de listas.
                          Cada sublista representa una fila del tablero.

    Retorno:
    int: 1 si "X" ha ganado, -1 si "O" ha ganado, 0 si el juego ha terminado en empate.
    """
    
    # Determinar el ganador del juego
    win = winner(board)
    
    # Si "X" ha ganado, devolver 1
    if win == X:
        return 1
    # Si "O" ha ganado, devolver -1
    elif win == O:
        return -1
    # Si no hay ganador (empate), devolver 0
    else:
        return 0

def minimax(board):
    """
    Devuelve la acción óptima para el jugador actual en el tablero utilizando el algoritmo Minimax.
    El objetivo de Minimax es minimizar la pérdida máxima esperada, es decir, maximizar el resultado para 
    el jugador actual asumiendo que el oponente también juega de manera óptima.

    Parámetros:
    board (list of list): El estado actual del tablero, representado por una lista de listas.
                          Cada sublista representa una fila del tablero.

    Retorno:
    tuple: Una tupla (i, j) que indica la mejor acción para el jugador actual.
           Devuelve None si el tablero es un estado terminal.
    """
    
    # Si el tablero es un estado terminal, no hay movimientos válidos.
    if terminal(board):
        return None

    # Determinar el jugador actual
    current_player = player(board)
    
    # Función anidada para calcular el valor máximo
    def max_value(board):
        # Si es un estado terminal, devuelve el valor de utilidad
        if terminal(board):
            return utility(board)
        
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    # Función anidada para calcular el valor mínimo
    def min_value(board):
        # Si es un estado terminal, devuelve el valor de utilidad
        if terminal(board):
            return utility(board)
        
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v
    
    # Si el jugador actual es X (maximizador)
    if current_player == X:
        best_score = -math.inf
        best_action = None
        for action in actions(board):
            action_score = min_value(result(board, action))
            if action_score > best_score:
                best_score = action_score
                best_action = action
        return best_action
    
    # Si el jugador actual es O (minimizador)
    else:
        best_score = math.inf
        best_action = None
        for action in actions(board):
            action_score = max_value(result(board, action))
            if action_score < best_score:
                best_score = action_score
                best_action = action
        return best_action
# Tic-Tac-Toe AI con Minimax

## Descripción

Este proyecto implementa el clásico juego de Tic-Tac-Toe (conocido como "el gato") en Python, utilizando el algoritmo de inteligencia artificial Minimax para jugar de manera óptima. La IA es invencible y garantizará, al menos, un empate si ambos jugadores juegan de manera óptima.

## Archivos

- **`tictactoe.py`**: Contiene toda la lógica del juego, incluyendo el manejo del tablero, la detección de ganadores y la implementación del algoritmo Minimax para la IA.
- **`runner.py`**: Proporciona la interfaz gráfica para jugar Tic-Tac-Toe utilizando `pygame`. Este archivo gestiona la visualización del tablero y la interacción con el usuario.
- **`requirements.txt`**: Lista de dependencias necesarias para ejecutar el proyecto (principalmente `pygame`).

## Requisitos

- Python 3.x
- `pygame` (instalable a través de `pip`)

## Instalación

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/franov/analytics/tictactoe-ai.git
   ```

2. Navega al directorio del proyecto:
    ```bash
    cd tictactoe-ai
   ```

3. Instala las dependencias necesarias:
   ```bash 
   pip install -r requirements.txt
   ```

## Uso
Una vez instaladas las dependencias, puedes ejecutar el juego usando el siguiente comando:
   ```bash
   python runner.py
   ```
   
Esto abrirá una ventana del juego donde podrás jugar Tic-Tac-Toe contra la IA. Elige si deseas jugar como "X" o "O" y disfruta del desafío.

## Funciones Principales
tictactoe.py

    player(board): Determina qué jugador tiene el siguiente turno en el tablero.
    actions(board): Devuelve un conjunto de todas las acciones posibles en el tablero dado.
    result(board, action): Devuelve el nuevo estado del tablero después de que un jugador realiza una acción.
    winner(board): Determina si hay un ganador en el tablero.
    terminal(board): Determina si el juego ha terminado.
    utility(board): Devuelve la utilidad del tablero en un estado terminal.
    minimax(board): Implementa el algoritmo Minimax para determinar el mejor movimiento posible.

runner.py

    Proporciona una interfaz gráfica donde los jugadores pueden interactuar con el juego.
    Permite seleccionar si deseas jugar como "X" o "O".
    Muestra el tablero, maneja los turnos y muestra el resultado final del juego.

## Ejemplo de Juego
Al iniciar el juego, se te pedirá que elijas si deseas jugar como "X" o "O". La IA jugará automáticamente cuando sea su turno, utilizando el algoritmo Minimax para garantizar el mejor movimiento posible.

## Créditos
Este proyecto fue desarrollado como parte de un curso de Inteligencia Artificial para el Doctorado en IA.

## Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
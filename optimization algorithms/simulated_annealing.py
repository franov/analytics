"""_summary_
Recocido Simulado (Simulated Annealing)
El Recocido Simulado es un algoritmo de optimización estocástico que simula el proceso de enfriamiento de los metales. 
Es útil para escapar de óptimos locales.

"""

import math
import random

def recocido_simulado(funcion_objetivo, generar_vecino, temperatura_inicial, tasa_enfriamiento, max_iter):
    solucion_actual = random.uniform(-10, 10)
    valor_actual = funcion_objetivo(solucion_actual)
    temperatura = temperatura_inicial

    for i in range(max_iter):
        nuevo_vecino = generar_vecino(solucion_actual)
        nuevo_valor = funcion_objetivo(nuevo_vecino)
        delta_valor = nuevo_valor - valor_actual

        if delta_valor < 0 or random.uniform(0, 1) < math.exp(-delta_valor / temperatura):
            solucion_actual = nuevo_vecino
            valor_actual = nuevo_valor

        temperatura *= tasa_enfriamiento

    return solucion_actual, valor_actual

# Ejemplo de uso
def funcion_objetivo(x):
    return x**2  # Minimizar la función x^2

def generar_vecino(x):
    return x + random.uniform(-1, 1)

temperatura_inicial = 100
tasa_enfriamiento = 0.99
max_iter = 1000

resultado, valor = recocido_simulado(funcion_objetivo, generar_vecino, temperatura_inicial, tasa_enfriamiento, max_iter)
print(f"El valor óptimo encontrado es: {resultado} con valor de función: {valor}")
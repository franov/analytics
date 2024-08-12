"""_summary_
Algoritmo Genético
El Algoritmo Genético es un método de optimización inspirado en la evolución biológica. 
Utiliza operadores como selección, cruce y mutación para encontrar soluciones óptimas.

"""

import random

def algoritmo_genetico(fitness, generar_poblacion, cruce, mutacion, num_generaciones, tam_poblacion):
    poblacion = generar_poblacion(tam_poblacion)
    for _ in range(num_generaciones):
        poblacion = sorted(poblacion, key=fitness, reverse=True)
        nueva_poblacion = poblacion[:2]  # Elitismo, mantener los mejores dos
        while len(nueva_poblacion) < tam_poblacion:
            padre1, padre2 = random.choices(poblacion[:10], k=2)
            hijo = cruce(padre1, padre2)
            hijo = mutacion(hijo)
            nueva_poblacion.append(hijo)
        poblacion = nueva_poblacion
    return max(poblacion, key=fitness)

# Ejemplo de uso
def fitness(individuo):
    return sum(individuo)  # Ejemplo simple, maximizar la suma de genes

def generar_poblacion(tam_poblacion):
    return [[random.randint(0, 1) for _ in range(10)] for _ in range(tam_poblacion)]

def cruce(padre1, padre2):
    punto = random.randint(1, len(padre1) - 1)
    return padre1[:punto] + padre2[punto:]

def mutacion(individuo):
    punto = random.randint(0, len(individuo) - 1)
    individuo[punto] = 1 - individuo[punto]
    return individuo

resultado = algoritmo_genetico(fitness, generar_poblacion, cruce, mutacion, num_generaciones=100, tam_poblacion=20)
print(f"El mejor individuo encontrado es: {resultado}")

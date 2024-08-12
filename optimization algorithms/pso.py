"""_summary_
Optimización por Enjambre de Partículas (PSO)
La Optimización por Enjambre de Partículas es un algoritmo basado en el comportamiento social de las partículas (o individuos) que se mueven a través del espacio de soluciones.

"""

import random

def pso(funcion_objetivo, num_particulas, dim, max_iter):
    particulas = [ [random.uniform(-10, 10) for _ in range(dim)] for _ in range(num_particulas)]
    velocidades = [ [random.uniform(-1, 1) for _ in range(dim)] for _ in range(num_particulas)]
    mejor_personal = particulas[:]
    mejor_global = min(particulas, key=funcion_objetivo)
    
    for _ in range(max_iter):
        for i in range(num_particulas):
            for d in range(dim):
                r1, r2 = random.random(), random.random()
                velocidades[i][d] = 0.5 * velocidades[i][d] + r1 * (mejor_personal[i][d] - particulas[i][d]) + r2 * (mejor_global[d] - particulas[i][d])
                particulas[i][d] += velocidades[i][d]

            if funcion_objetivo(particulas[i]) < funcion_objetivo(mejor_personal[i]):
                mejor_personal[i] = particulas[i]

        mejor_global = min(particulas, key=funcion_objetivo)
    
    return mejor_global

# Ejemplo de uso
def funcion_objetivo(x):
    return sum([xi**2 for xi in x])  # Minimizar la suma de cuadrados

num_particulas = 30
dim = 2  # Problema en 2 dimensiones
max_iter = 100

resultado = pso(funcion_objetivo, num_particulas, dim, max_iter)
print(f"La mejor solución encontrada es: {resultado}")


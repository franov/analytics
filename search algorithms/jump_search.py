"""_summary_
Jump Search
El algoritmo Jump Search es útil para listas ordenadas. La idea es dividir la lista en bloques de un tamaño determinado y saltar bloques completos para encontrar el objetivo.

Ventajas:
    Eficiencia en listas grandes y ordenadas: Jump Search es más eficiente que la búsqueda lineal en listas ordenadas porque salta bloques completos en lugar de buscar elemento por elemento.
    Menos comparaciones: En comparación con la búsqueda lineal, realiza menos comparaciones, lo que mejora el tiempo de búsqueda en listas grandes.
    Simplicidad de implementación: Aunque es un poco más complejo que la búsqueda lineal, sigue siendo relativamente sencillo de implementar.

Desventajas:
    Requiere lista ordenada: Al igual que la búsqueda binaria, Jump Search requiere que la lista esté ordenada para funcionar correctamente.
    Elección del tamaño del salto: El rendimiento depende en gran medida del tamaño del salto, que típicamente se elige como la raíz cuadrada del tamaño de la lista. Si el tamaño de la lista cambia, el tamaño del salto podría no ser óptimo.
    No es tan eficiente como la búsqueda binaria: Aunque mejora sobre la búsqueda lineal, Jump Search generalmente no es tan eficiente como la búsqueda binaria en listas grandes.

"""

import math

def jump_search(lista, objetivo):
    n = len(lista)
    salto = int(math.sqrt(n))
    prev = 0

    while lista[min(salto, n) - 1] < objetivo:
        prev = salto
        salto += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(salto, n)):
        if lista[i] == objetivo:
            return i

    return -1

# Ejemplo de uso
lista = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]
numero_objetivo = 10
resultado = jump_search(lista, numero_objetivo)

if resultado != -1:
    print(f"El número {numero_objetivo} se encuentra en la posición: {resultado}")
else:
    print(f"El número {numero_objetivo} NO se encuentra en la lista.")
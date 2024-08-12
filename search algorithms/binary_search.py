"""_summary_
Búsqueda Binaria
El algoritmo de búsqueda binaria es un algoritmo muy eficiente que se aplica solo a listas ordenadas. }
Funciona dividiendo repetidamente la lista en dos mitades y comparando el elemento objetivo con el elemento del medio, esto reduce significativamente la cantidad de comparaciones necesarias.

Ventajas:
    Eficiencia de listas ordenadas: La principal ventaja de la búsqueda binaria es su eficiencia en listas ordenadas. Su tiempo de ejecución es de O(log n), lo que significa que disminuye rápidamente a medida que el tamaño de la lista aumenta.
    Menos comparaciones: Comparado con la búsqueda lineal, la búsqueda binaria realiza menos comparaciones en promedio, lo que lo hace más rápido para encontrar el objetivo.

Desventajas:
    Requiere una lista ordenada: La búsqueda binaria sólo es aplicable a listas ordenadas, Si la lista no está ordenada, se debe realizar una operación adicional para ordenarla antes de usar la búsqueda binaria.
    Mayor complejidad de implementación: Comparado con la búsqueda lineal, la búsqueda binaria es más compleja de implementar debido a su naturaleza recursiva.

"""

def binary_search(lista, objetivo, inicio, fin ):
    if inicio > fin:
        return -1

    centro = (inicio + fin) // 2
    if lista[centro] == objetivo:
        return centro
    elif lista[centro] < objetivo:
        return binary_search(lista, objetivo, centro + 1, fin)
    else:
        return binary_search(lista, objetivo, inicio, centro - 1)

# Ejemplo de uso
lista = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]
numero_objetivo = 27
inicio_busqueda = 0
fin_busqueda = len(lista) - 1

resultado = binary_search(lista, numero_objetivo, inicio_busqueda, fin_busqueda)

if resultado != -1:
    print(f"El número {numero_objetivo} se encuentra en la posición {resultado}.")
else:
    print(f"El númeor {numero_objetivo} NO se encuentra en la lista.")
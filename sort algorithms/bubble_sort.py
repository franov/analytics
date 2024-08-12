"""_summary_
Bubble Sort
El algoritmo de ordenamiento por burbuja es uno de los más simples pero menos eficientes. 
Funciona comparando pares de elementos e intercambiándolos si están en el orden incorrecto, 
este proceso se hace una y otra vez hasta que la lista esté ordenada de forma correcta.

Ventajas:
    Simplicidad: El algoritmo de burbuja es fácil de entender e implementar, lo que lo convierte en una buena opción para introducir conceptos de ordenamiento en la programación.
    Implementación sencilla: Requiere poca cantidad de código y no involucra estructuras de datos complejas.

Desventajas:
    Lento para listas grandes: Debido a su complejidad cuadrática el algoritmo de burbuja se vuelve lento en la práctica para listas de tamaño considerable.
    No considera el orden parcial: A diferencia de otros algoritmos, el algoritmo de burbuja realiza el mismo número de comparaciones e intercambios sin importar 
    si la lista ya está en gran parte ordenada.

"""

def bubble_sort(lista):
    length = len(lista)
    for i in range(length):
        for j in range(0, (length-i) - 1):
            if lista[j] > lista[j + 1]:
                auxiliar = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = auxiliar
    return lista

lista_desordenada = [3, 6, 7, 8, 3, 45, 23, 0, 16, 26, 6, 7, 50]

lista_ordenada = bubble_sort(lista_desordenada)

print(lista_ordenada) # output: [0, 3, 3, 6, 6, 7, 7, 8, 16, 23, 26, 45, 50]

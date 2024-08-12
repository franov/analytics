"""_summary_
Exponential Search
Exponential Search es útil cuando no sabemos el tamaño de la lista o es infinita. 
Comienza verificando los elementos en posiciones de potencias de 2, y luego usa Búsqueda Binaria en la subsección relevante.

Ventajas:
    Eficiencia en listas de tamaño desconocido o infinitas: Exponential Search es muy útil cuando no se conoce el tamaño de la lista o cuando se trata de una lista infinita, ya que puede rápidamente identificar el rango donde se encuentra el objetivo.
    Combina ventajas de búsqueda binaria: Después de identificar el rango adecuado, utiliza búsqueda binaria, aprovechando su eficiencia en listas ordenadas.
    Tiempo de ejecución eficiente: En el mejor de los casos, tiene un tiempo de ejecución O(log n), similar al de la búsqueda binaria.

Desventajas:
    Requiere lista ordenada: Como la mayoría de los algoritmos de búsqueda avanzada, Exponential Search también requiere que la lista esté ordenada.
    Más complejo de implementar: Es más complicado de implementar que la búsqueda lineal y binaria debido a la combinación de técnicas.
    No siempre es la opción más rápida: Para listas de tamaño conocido, la búsqueda binaria por sí sola podría ser más directa y eficiente.

"""

def binary_search(lista, objetivo, inicio, fin):
    if inicio > fin:
        return -1

    centro = (inicio + fin) // 2
    if lista[centro] == objetivo:
        return centro
    elif lista[centro] < objetivo:
        return binary_search(lista, objetivo, centro + 1, fin)
    else:
        return binary_search(lista, inicio, centro - 1)

def exponential_search(lista, objetivo):
    if lista[0] == objetivo:
        return 0

    i = 1
    while i < len(lista) and lista[i] <= objetivo:
        i = i * 2

    return binary_search(lista, objetivo, i // 2, min(i, len(lista) - 1))

# Ejemplo de uso
lista = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]
numero_objetivo = 20
resultado = exponential_search(lista, numero_objetivo)

if resultado != -1:
    print(f"El número {numero_objetivo} se encuentra en la posición: {resultado}")
else:
    print(f"El número {numero_objetivo} NO se encuentra en la lista.")
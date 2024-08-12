"""_summary_
Interpolation Search
Este algoritmo es útil cuando los elementos de la lista están distribuidos uniformemente. 
La búsqueda de interpolación estima la posición del objetivo calculando la posición de manera proporcional.

Ventajas:
    Eficiencia en listas con distribución uniforme: Cuando los datos están distribuidos uniformemente, Interpolation Search puede ser muy eficiente, incluso mejor que la búsqueda binaria.
    Tiempo de ejecución variable: En el mejor de los casos, puede tener un tiempo de ejecución cercano a O(log log n), lo que lo hace muy rápido para ciertas distribuciones de datos.

Desventajas:
    Requiere lista ordenada y distribución uniforme: Este algoritmo es eficiente solo cuando los datos están ordenados y distribuidos uniformemente. En distribuciones no uniformes, su rendimiento puede degradarse significativamente.
    Complejidad de implementación: Es más complejo de implementar que la búsqueda lineal y la búsqueda binaria, lo que puede dificultar su uso en algunas aplicaciones.
    Rendimiento variable: El rendimiento puede ser impredecible si la lista no cumple con las condiciones ideales de distribución uniforme.

"""

def interpolation_search(lista, objetivo):
    low = 0
    high = len(lista) - 1

    while low <= high and lista[low] <= objetivo <= lista[high]:
        if low == high:
            if lista[low] == objetivo:
                return low
            return -1

        pos = low + int(((float(high - low) / (lista[high] - lista[low])) * (objetivo - lista[low])))

        if lista[pos] == objetivo:
            return pos

        if lista[pos] < objetivo:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Ejemplo de uso
lista = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]
numero_objetivo = 15
resultado = interpolation_search(lista, numero_objetivo)

if resultado != -1:
    print(f"El número {numero_objetivo} se encuentra en la posición: {resultado}")
else:
    print(f"El número {numero_objetivo} NO se encuentra en la lista.")
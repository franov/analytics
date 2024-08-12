"""_summary_
Insertion Sort
El algoritmo de ordenamiento por inserción es un algoritmo simple pero eficiente. 
Funciona dividiendo la lista en dos partes, una parte ordenada y otra desordenada, a medida que se recorre la lista desordenada, 
se insertan elementos en la posición correcta en la parte ordenada.

Ventajas:
    Baja sobrecarga: Requiere menos comparaciones y movimientos que algoritmos como el ordenamiento de burbuja, lo que lo hace más eficiente en términos de intercambios de elementos.
    Simplicidad: el ordenamiento por inserción es uno de los algoritmos de ordenamiento más simples de implementar y entender. Esto lo hace adecuado para enseñar conceptos básicos de ordenamiento.

Desventajas:
    Ineficiencia en listas grandes: A medida que el tamaño de la lista aumenta, el rendimiento del ordenamiento por inserción disminuye. Su complejidad cuadrática de O(n^2) en el pero caso lo hace ineficiente para las listas grandes.
    No escalable: Al igual que otros algoritmos de complejidad cuadrática, el ordenamiento por inserción no es escalable para listas grandes, ya que su tiempo de ejecución aumenta considerablemente con el tamaño de la lista.

"""

def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        index = i 
        """
        Este bucle intercambia los dos número de posición 
        mientras que el número anterior sea más grande que el número actual
        """
        while index > 0 and lista[index - 1] > actual:
            lista[index] = lista[index - 1]
            index = index - 1
        lista[index] = actual

    return lista

lista_desordenada = [39, 45, 32, 4, 2, 85, 43, 7, 18, 16, 5, 67, 32]
lista_ordenada = insertion_sort(lista_desordenada)
print(lista_ordenada) # output: [2, 4, 5, 7, 16, 18, 32, 32, 39, 43, 45, 67, 85]
"""_summary_
Búsqueda Lineal
Los algoritmos de búsqueda lineal, también conocidos como búsqueda secuencial, implican recorrer una lista de elementos uno por uno hasta encontrar un elemento específico. 
Este algoritmo es muy sencillo de implementar en código pero puede ser muy ineficiente dependiendo del largo de la lista y la ubicación donde está el elemento. 

Ventajas:
    Sencillez: La búsqueda lineal es uno de los algoritmos de búsqueda más simples y fáciles de implementar. Solo requiere iterar a través de la lista de elementos uno por uno hasta encontrar el objetivo.
    flexibilidad: La búsqueda lineal puede aplicarse a cualquier tipo de lista, independientemente de si está ordenada o no.

Desventajas:
    Ineficiencia en listas grandes: La principal desventaja de la búsqueda lineal es su ineficiencia en listas grandes. Debido a que compara cada elemento uno por uno, su tiempo de ejecución crece de manera lineal con el tamaño de la lista.
    No es adecuada para listas ordenadas: Aunque puede funcionar en listas no ordenadas, la búsqueda lineal no es eficiente para listas ordenadas. En ta

"""

def linear_search(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

lista = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]
numero_objetivo = 39
resultado = linear_search(lista, numero_objetivo)

if resultado != -1:
    print(f"El número {numero_objetivo} se encuentra en la posición: {resultado}")
else:
    print(f"El número {numero_objetivo} NO se encuentra en la lista.")
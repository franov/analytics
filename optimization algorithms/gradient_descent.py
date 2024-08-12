"""_summary_
Gradiente Descendente
El Gradiente Descendente es un algoritmo de optimización utilizado para minimizar una función objetivo. 
Este algoritmo ajusta iterativamente los parámetros en la dirección del gradiente negativo.

"""

def gradient_descent(f_prime, x_init, learning_rate, max_iter):
    x = x_init
    for i in range(max_iter):
        grad = f_prime(x)
        x = x - learning_rate * grad
    return x

# Ejemplo de uso
def f_prime(x):
    return 2 * x  # Derivada de la función f(x) = x^2

x_init = 10  # Punto inicial
learning_rate = 0.1
max_iter = 100

resultado = gradient_descent(f_prime, x_init, learning_rate, max_iter)
print(f"El valor óptimo de x es: {resultado}")
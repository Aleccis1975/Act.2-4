# Función recursiva para calcular el factorial de un número mayor o igual a cero
def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser mayor o igual a cero.")
    
    if n == 0:
        return 1
    
    return n * factorial(n - 1)

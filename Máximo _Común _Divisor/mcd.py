# Función recursiva para calcular el MCD de dos números enteros
def mcd(a, b):
    """
    Calcula el MCD de dos números usando el algoritmo de Euclides.
    
    Args:
        a (int): Primer número.
        b (int): Segundo número.
        
    Returns:
        int: El MCD de los dos números.
    """
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

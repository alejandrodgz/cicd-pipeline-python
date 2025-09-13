"""
Módulo de operaciones aritméticas básicas.
"""


def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def restar(a, b):
    """Devuelve la resta de a y b."""
    return a - b


def multiplicar(a, b):
    """Devuelve el producto de a y b."""
    return a * b


def dividir(a, b):
    """Devuelve la división de a entre b. Lanza ZeroDivisionError si b es cero."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

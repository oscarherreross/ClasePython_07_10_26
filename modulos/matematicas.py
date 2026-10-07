"""Módulo con operaciones matemáticas reutilizables."""

# Constante: se escribe en mayúsculas porque su valor no debe cambiar
PI = 3.14159


def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b


def restar(a, b):
    """Resta b a a y devuelve el resultado."""
    return a - b


def area_circulo(radio):
    """Devuelve el área de un círculo: PI por el radio al cuadrado."""
    return PI * radio * radio

"""Ejercicio de pytest: tests de modulos/precios.py. Se ejecutan escribiendo en la terminal: pytest"""
from modulos.precios import precio_final


def test_precio_con_descuento():
    # Un producto de 100 € con un 20 % de descuento debe costar 80 €
    assert precio_final(100, 20) == 80


def test_precio_sin_descuento():
    # Un producto de 50 € sin descuento debe costar 50 €
    assert precio_final(50) == 50

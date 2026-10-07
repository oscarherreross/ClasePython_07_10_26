"""Módulo del ejercicio de pytest: precio final de un producto con descuento."""


def precio_final(precio, descuento=0):
    """Devuelve el precio aplicando un descuento en porcentaje (20 significa un 20 %)."""
    return precio - precio * descuento / 100

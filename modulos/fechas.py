"""Módulo con funciones para trabajar con fechas."""

# Tupla con los nombres de los meses: no van a cambiar, así que no hace falta una lista
MESES = (
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
)


def nombre_mes(numero):
    """Devuelve el nombre del mes a partir de su número (1 = enero, 12 = diciembre)."""
    if numero < 1 or numero > 12:
        return "Mes no válido"
    return MESES[numero - 1]  # restamos 1 porque los índices de la tupla empiezan en 0

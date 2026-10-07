"""Tests del módulo modulos/matematicas.py. Se ejecutan escribiendo en la terminal: pytest"""

# "as" importa el módulo con otro nombre (un alias): aquí matematicas pasa a llamarse math
from modulos import matematicas as math


# pytest ejecuta las funciones cuyo nombre empieza por "test", así que testear_suma también cuenta.
# Lo habitual es llamarlas test_algo, como las de abajo.
def testear_suma():
    assert math.sumar(2, 2) == 4


def test_sumar_negativos():
    assert math.sumar(-1, -2) == -3


def test_restar():
    assert math.restar(10, 4) == 6

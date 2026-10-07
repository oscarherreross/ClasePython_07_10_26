# Fundamentos de Python · Python 3

Apuntes y ejercicios resueltos de la sesión **Python 3** del Bloque 1 (Fundamentos) del Máster en Desarrollo Web, IA aplicada y DevOps: pedir datos al usuario, convertir tipos, controlar el flujo de los bucles, evitar que el programa se pare con un error y organizar el código en módulos con tests.

## Contenido

- **[`script.py`](script.py):** teoría y ejercicios, organizados en 7 secciones.
  1. Repaso: recorrer una lista de diccionarios con `for` y `while`.
  2. Entrada de datos con `input()`.
  3. Conversión de tipos con `int()` y `float()`, y redondeo con `round()`.
  4. Control de flujo con `continue` y `break`.
  5. Control de errores con `try`, `except` y `finally`, y validación de lo que escribe el usuario.
  6. Módulos: importar código propio y de la librería estándar.
  7. pip y tests con pytest.
- **[`modulos/`](modulos):** módulos propios que usa el script: `matematicas.py`, `saludos.py`, `fechas.py` y `precios.py`.
- **[`test_suma.py`](test_suma.py) y [`test_precios.py`](test_precios.py):** tests con pytest.

## Cómo ejecutarlo

```bash
python script.py      # pide algunos datos por teclado
pip install pytest
pytest                # ejecuta los tests
```

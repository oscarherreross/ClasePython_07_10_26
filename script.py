# ============================================================
# PYTHON 3: input, conversión de tipos, control de flujo, errores y módulos
# Para ejecutarlo, abre la terminal de VS Code y escribe: python script.py
# Ojo: las secciones 2 y 5 piden datos por teclado; escribe la respuesta y pulsa Enter.
# ============================================================

# ============================================================
# 1. REPASO: RECORRER UNA LISTA DE DICCIONARIOS
# ============================================================
productos = [
    {"nombre": "Teclado", "precio": 45, "stock": 30},
    {"nombre": "Monitor", "precio": 220, "stock": 12},
    {"nombre": "Ratón", "precio": 25, "stock": 50},
    {"nombre": "Portátil", "precio": 850, "stock": 8},
    {"nombre": "Auriculares", "precio": 120, "stock": 20},
]

# Con for: nombre de los productos que cuestan más de 100
for producto in productos:
    if producto["precio"] > 100:
        print(producto["nombre"])  # Monitor, Portátil, Auriculares

# Con while: de los 3 primeros productos, los que tienen 25 unidades o menos.
# El contador hace de índice de la lista y se suma 1 en cada vuelta.
contador = 0
while contador < 3:
    producto = productos[contador]
    if producto["stock"] <= 25:
        print(producto["nombre"])  # Monitor
    contador += 1

# ============================================================
# 2. ENTRADA DE DATOS: input()
# ============================================================
# input() muestra un mensaje, espera a que el usuario escriba algo y pulse Enter,
# y devuelve lo escrito SIEMPRE como texto (str), aunque sean números.
# Por eso, para operar con números hay que convertirlo antes con int() o float().
numero = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))
suma = numero + numero2
print(f"La suma de {numero} y {numero2} es {suma}")

# Ejercicio: pedir dos textos y decir si son iguales
primero = input("Primer texto: ")
segundo = input("Segundo texto: ")
if primero == segundo:  # == compara los dos textos
    print("Son iguales")
else:
    print("Son distintos")

# ============================================================
# 3. CONVERSIÓN DE TIPOS Y round()
# ============================================================
# int() convierte un valor a número entero.
# Acepta textos que representen enteros ("42") y números decimales.
texto_entero = "42"  # así es como llegaría un número escrito con input()
numero_entero = int(texto_entero)
print(type(texto_entero))   # <class 'str'>
print(type(numero_entero))  # <class 'int'>
print(int(3.99))            # 3: con un decimal corta la parte decimal, no redondea
# Con un texto que no es un entero, como int("hola") o int("3.14"), da ValueError (ver sección 5).

# float() convierte un valor a número decimal. Acepta textos como "2" o "1.5" y números enteros.
texto_decimal = "3.14159"
numero_decimal = float(texto_decimal)
print(type(texto_decimal))   # <class 'str'>
print(type(numero_decimal))  # <class 'float'>

# round(numero) redondea al entero más cercano y round(numero, decimales) a esos decimales
print(round(3.14159))     # 3
print(round(2.7))         # 3
# Redondeo "del banquero": si el número está justo en el medio, va al entero PAR más cercano
print(round(2.5))         # 2
print(round(3.5))         # 4
print(round(3.14159, 2))  # 3.14

# ============================================================
# 4. CONTROL DE FLUJO: continue Y break
# ============================================================
# continue salta el resto del código de la vuelta actual y pasa a la siguiente vuelta del bucle
numeros = [1, 2, 3, 4, 5, 6, 7]

for num in numeros:
    if num % 2 == 0:  # si el resto de dividir entre 2 es 0, el número es par
        print(f"Saltando el número par: {num}")
        continue  # no se ejecuta el print de abajo para los pares
    print(f"Procesando número impar: {num} (su cuadrado es {num * num})")

print("Fin del programa después del bucle.")

# break termina el bucle completo en ese momento, aunque queden elementos por recorrer
numeros = [1, 5, 8, 12, 15, 20]
numero_objetivo = 12
for num in numeros:
    print(f"Comprobando el número: {num}")
    if num == numero_objetivo:
        print(f"¡Encontrado! El número {numero_objetivo} está en la lista.")
        break  # sale del for: 15 y 20 ya no se comprueban
    print(f"El número {num} no es el objetivo.")
print("Fin del programa después del bucle.")

# Ejercicio: mostrar solo las edades de mayores de 18 y detener el bucle
# en cuanto aparezca una edad igual o superior a 65
lista_edades = [15, 22, 17, 30, 65, 45, 70, 19]
for edad in lista_edades:
    if edad >= 65:
        print(f"Edad {edad}: persona de 65 años o más, se detiene el bucle.")
        break     # 45, 70 y 19 ya no se procesan
    if edad <= 18:
        continue  # 15 y 17 se saltan sin mostrarse
    print(f"Edad {edad}: mayor de edad.")  # 22 y 30

# ============================================================
# 5. CONTROL DE ERRORES: try / except / finally
# ============================================================
# try: intenta ejecutar el código.
# except: si ocurre un error, en lugar de parar el programa ejecuta este bloque.
# finally: se ejecuta siempre, haya error o no (por ejemplo, para cerrar un archivo o una conexión).
# Un except sin tipo captura cualquier error; es mejor indicar el error que esperamos.
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Se produjo un error: División por cero.")
finally:
    print("Proceso finalizado, independientemente de si hubo un error o no.")

# ValueError aparece al convertir un texto que no es un número
try:
    numero_texto = int("hola")
except ValueError:
    print("No se puede convertir 'hola' a un número entero.")

# Ejercicio: pedir un número con un máximo de 5 intentos.
# Si lo escrito no es un número se avisa y se vuelve a pedir; si es válido, se sale del bucle.
contador = 0
while contador < 5:
    entrada = input("Ingrese un número: ")
    try:
        entrada_int = int(entrada)
    except ValueError:
        print("No es un número. Introduce un número")
        contador += 1  # cuenta el intento fallido
        continue       # vuelve a pedir el número
    print(f"El número ingresado es: {entrada_int}")
    break  # número válido: termina el bucle

# Ejercicio: pedir una clave numérica, también con un máximo de 5 intentos.
# Si int() consigue convertir la entrada, la clave ya es un entero; si no, salta el except.
contador = 0
while contador < 5:
    try:
        clave = int(input("Ingrese su clave: "))
        print("Numero válido")
        break
    except ValueError:
        print("Numero no válido, repítelo.")
        contador += 1

# ============================================================
# 6. MÓDULOS
# ============================================================
# Un módulo es un archivo .py con código reutilizable (funciones, constantes...)
# que se importa desde otro archivo para no repetir código.
# Si matematicas.py estuviera en la misma carpeta que este script bastaría con: import matematicas
# Como está dentro de la carpeta modulos/, se importa con: from carpeta import módulo
from modulos import matematicas
print(matematicas.sumar(5, 3))    # 8: llamada a la función sumar del módulo matematicas
print(matematicas.sumar(10, 20))  # 30
print(matematicas.restar(10, 4))  # 6
print(f"El valor de PI es: {matematicas.PI}")  # 3.14159: también se pueden importar constantes
print(matematicas.area_circulo(4))             # 50.26544

# Se pueden importar varios módulos de la misma carpeta a la vez
from modulos import saludos, fechas
print(saludos.saludar("Oscar"))  # ¡Hola, Oscar!: llamada a la función saludar
print(saludos.despedir("Pepe"))  # ¡Adiós, Pepe!: llamada a la función despedir
mes = fechas.nombre_mes(8)
print(f"El mes es: {mes}")       # El mes es: agosto

# También se puede importar solo una función y usarla sin poner el nombre del módulo delante
from modulos.matematicas import sumar
print(sumar(1, 2))  # 3

# Python trae sus propios módulos (la librería estándar), como math.
# Por eso no conviene llamar a nuestros archivos igual que ellos (math.py, random.py...).
import math
print(math.sqrt(16))  # 4.0: raíz cuadrada

# ============================================================
# 7. PIP Y TESTS CON PYTEST
# ============================================================
# pip es el gestor de paquetes de Python: instala librerías de terceros desde PyPI (https://pypi.org).
#   pip install pytest   -> instala pytest
#   pytest               -> busca los archivos test_*.py y ejecuta sus funciones que empiezan por test
# En un test, assert comprueba que algo es True; si no lo es, el test falla.
# Los tests de este repositorio están en test_suma.py y test_precios.py.

# Ejercicio: precio final de un producto aplicando un descuento (probado en test_precios.py)
from modulos import precios
print(precios.precio_final(100, 20))  # 80.0: 100 € con un 20 % de descuento
print(precios.precio_final(50))       # 50.0: sin descuento

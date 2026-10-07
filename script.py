# productos = [
#     {"nombre": "Teclado", "precio": 45, "stock": 30},
#     {"nombre": "Monitor", "precio": 220, "stock": 12},
#     {"nombre": "Ratón", "precio": 25, "stock": 50},
#     {"nombre": "Portátil", "precio": 850, "stock": 8},
#     {"nombre": "Auriculares", "precio": 120, "stock": 20},
# ]

# for producto in productos:
#     if producto["precio"] > 100:
#         print(producto["nombre"])

# contador = 0
# while contador < 3:
#     producto = productos[contador]
#     if producto["stock"] <= 25:
#         print(producto["nombre"])
#     contador += 1

# numero = int(input("Ingrese un número: "))
# numero2 = int(input("Ingrese otro número: "))
# suma = numero + numero2
# print(f"La suma de {numero} y {numero2} es {suma}")

# primero = input("Primer texto: ")
# segundo = input("Segundo texto: ")
# # Compara e imprime el resultado
# if primero == segundo:
#     print("Son iguales")
# else:
#     print("Son distintos")

# numeros = [1, 2, 3, 4, 5, 6, 7]

# for num in numeros:
#     if num % 2 == 0: 
#         print(f"Saltando el número par: {num}")
#         continue 
#     print(f"Procesando número impar: {num} (su cuadrado es {num * num})")

# print("Fin del programa después del bucle.")

# numeros = [1, 5, 8, 12, 15, 20]
# numero_objetivo = 12
# for num in numeros:
#     print(f"Comprobando el número: {num}")
#     if num == numero_objetivo:
#         print(f"¡Encontrado! El número {numero_objetivo} está en la lista.")
#         break 
#     print(f"El número {num} no es el objetivo.")
# print("Fin del programa después del bucle.")

# lista_edades = [15, 22, 17, 30, 65, 45, 70, 19]
# for edad in lista_edades:
#     if edad > 18:
#         if edad == 65:
#             print(f"Edad {edad}: Persona mayor, procesando.")
#             break
#         print(f"Edad {edad}: Mayor de edad, saltando.")
#         continue

# try:
#     resultado = 10 / 0
# except  ZeroDivisionError:
#     print("Se produjo un error: División por cero.")
# finally:
#     print("Proceso finalizado, independientemente de si hubo un error o no.")

# contador = 0
# while contador < 5:
#     entrada = input("Ingrese un número: ")
#     try:
#         entrada_int = int(entrada)
#     except ValueError:
#         print("No es un número. Introduce un número")
#         contador += 1
#         continue
#     print(f"El número ingresado es: {entrada_int}")
#     break

# contador = 0
# while contador < 5:
#     try:
#         clave = int(input("Ingrese su clave: "))

#         if type(clave) != int:
#             print("La clave debe ser un número entero.")
#         else:
#             print("Numero válido")
#             break
#     except:
#         print("Numero no válido, repítelo.")

# import matematicas
# print(matematicas.sumar(5, 3))  # Llamada a la función sumar del módulo matematicas

# from modulos import matematicas
# print(matematicas.sumar(10, 20))  # Llamada a la función sumar del módulo matematicas

from modulos import saludos
print(saludos.saludar("Oscar"))  # Llamada a la función saludar
print(saludos.despedir("Pepe"))  # Llamada a la función despedir
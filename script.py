productos = [
    {"nombre": "Teclado", "precio": 45, "stock": 30},
    {"nombre": "Monitor", "precio": 220, "stock": 12},
    {"nombre": "Ratón", "precio": 25, "stock": 50},
    {"nombre": "Portátil", "precio": 850, "stock": 8},
    {"nombre": "Auriculares", "precio": 120, "stock": 20},
]

for producto in productos:
    if producto["precio"] > 100:
        print(producto["nombre"])

contador = 0
while contador < 3:
    producto = productos[contador]
    if producto["stock"] <= 25:
        print(producto["nombre"])
    contador += 1
""" Parte 1 — Ciclo for
Nivel básico
Ejercicio 1 — Mostrar letras
Muestra cada letra de la palabra "python" en líneas separadas.

Guía: for letra in "python":"""

for letra in "python":
    print(letra)

"""Ejercicio 2 — Lista de videojuegos
Tienes esta lista:
juegos = ["Minecraft", "FIFA", "Mario Kart"]
Muestra cada juego en pantalla."""

juegos = ["Minecraft", "FIFA", "Mario Kart"]
for i in juegos:
    print(f"\nJuego: {i}")


"""Ejercicio 3 — Contar del 1 al 5
Muestra los números del 1 al 5 usando range().
Guía: for numero in range():"""
for numero in range(1,6):
    print(numero)

"""Nivel intermedio. Ejercicio 4 — Emojis de reacción
Muestra 10 veces el emoji:🔥 Tip: Usa range()."""
for numero in range(9):
    print("🔥")

"""Ejercicio 5 — Mostrar nombres largos
Tienes esta lista:
nombres = ["Ana", "Sebastian", "Luis", "Fernanda"]
Muestra solamente los nombres que tengan más de 5 letras.
Pista: Usa if."""

nombres = ["Ana", "Sebastian", "Luis", "Fernanda"]
for j in nombres:
    if len(j) > 5:
        print(j)

"""Ejercicio 6 — Tabla de multiplicar
Muestra la tabla del 7 del 1 al 10.
Tip: Usa multiplicación dentro del ciclo."""
for i in range(1,11):
    print("\n7 x ", i, "= ", 7*i )


"""Nivel avanzado
Ejercicio 7 — Contar vocales
Recorre una palabra ingresada por el usuario y cuenta cuántas vocales tiene.
Pistas: Usa un contador.
Revisa si la letra es "a", "e", "i", "o" o "u"."""

palabra = input("ingrese una palabra: ")
letras_vocales = "a", "e", "i", "o", "u"
for p in palabra:
    if p in letras_vocales:
        print(p)


"""Ejercicio 8 — Carrito de compras
Tienes esta lista de precios:
precios = [10, 25, 7, 30]
Calcula cuánto pagará el cliente en total.
Pista: Usa un acumulador.
"""
precios = [10, 25, 7, 30]
precio_acumulado = 0

for p in precios:
    precio_acumulado += p
print("Precio Acumulado: ", precio_acumulado)
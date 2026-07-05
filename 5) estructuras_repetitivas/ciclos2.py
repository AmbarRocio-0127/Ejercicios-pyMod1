""" Nivel básico
Ejercicio 1 — Contador simple
Muestra los números del 1 al 5 usando while.

Guía: contador = 1 """

counter = 0
while counter <= 5:
    print(counter)
    counter+=1
print()

"""Ejercicio 2 — Cuenta regresiva
Muestra una cuenta regresiva desde 5 hasta 1.

Tip: el contador debe disminuir.
Nivel intermedio"""

counter2 = 5
while counter2 <= 5 and counter2 > 0:
    print(counter2)
    counter2-=1
print()
    
counter3 = 5
while counter3 >= 1:
    print(counter3)
    counter3-=1
print()

"""Ejercicio 3 — Contraseña
Pide una contraseña hasta que el usuario escriba "python" correctamente.

Pista:

Usa input() y while."""

contrasena = input("Ingrese la contraseña: ")
while contrasena != "python":
    contrasena = input("Contraseña incorrecta. \nIngrese la contraseña nuevamente: ")
print("¡Acceso Concedido!")

"""Ejercicio 4 — Menú interactivo
Pide opciones al usuario hasta que escriba "salir"."""

opcion = int(input("\nSeleccione la opcion deseada: \n1)registrar Usuario \n2)Verificar Póliza \n3) Editar Usuario \n4)Salir"))

while opcion != 4:
    print(f"Opcion {opcion} seleccionada")
    opcion = int(input("\nSeleccione la opcion deseada: \n1)registrar Usuario \n2)Verificar Póliza \n3) Editar Usuario \n4)Salir   "))

print("\nSesión Cerrada. ¡Hasta Luego!")

"""Nivel avanzado
Ejercicio 5 — Acumulando puntos
Un videojuego entrega 15 puntos por ronda.

Usa un while para sumar puntos hasta llegar a 100.

Pistas:

Usa un acumulador.
El ciclo debe detenerse automáticamente."""

videojuego = 0
while videojuego <=100:
    videojuego += 15
    pass

"""Parte 3 — break
Nivel básico
Ejercicio 1 — Detener conteo
Muestra números del 1 al 10 pero detén el ciclo cuando aparezca el 6.

Guía:

if numero == 6:
    break"""
    
"""Nivel intermedio
Ejercicio 2 — Buscar un producto
Recorre esta lista:

productos = ["Pan", "Leche", "Huevos", "Arroz"]
Detén el ciclo cuando encuentres "Huevos"."""

"""Nivel avanzado
Ejercicio 3 — Número secreto
Crea un juego donde el usuario deba adivinar un número secreto.

Cuando acierte:

muestra "Ganaste"
usa break
Pista:

Combina while True con input()."""

"""Parte 4 — continue
Nivel básico
Ejercicio 1 — Saltar número
Muestra números del 1 al 5 pero omite el número 3.

Guía:

if numero == 3:
    continue"""
   
    
"""Nivel intermedio
Ejercicio 2 — Ignorar negativos
Recorre esta lista:

numeros = [4, -2, 7, -1, 8]
Muestra solamente los números positivos."""


"""Nivel avanzado
Ejercicio 3 — Filtrar comentarios vacíos
Recorre una lista de comentarios y evita mostrar los que estén vacíos.

Pistas:

Usa continue.
Un comentario vacío es ""."""


"""Parte 5 — Contadores y acumuladores
Nivel básico
Ejercicio 1 — Contador de likes
Simula 8 nuevos likes usando un contador.

Guía:

likes = 0"""


"""Ejercicio 2 — Acumulador de monedas
Un jugador recoge monedas con valores:

[5, 3, 10, 2]
Calcula el total.

Nivel intermedio"""


"""Ejercicio 3 — Contar aprobados
Recorre esta lista de notas:
[4, 2, 5, 1, 3]
Cuenta cuántos estudiantes aprobaron.
Pista:

Aprueba quien tenga nota mayor o igual a 3."""


"""Nivel avanzado
Ejercicio 4 — Promedio de compras
Pide 5 precios al usuario y calcula:

suma total
promedio
Pistas:

Usa acumulador.
Usa contador.
El promedio es:
promedio = total / cantidad
Documentación oficial de Python sobre ciclos

"""
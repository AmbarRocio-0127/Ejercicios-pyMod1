"""Ejercicios Progresivos y Guiados
Nivel 1 — Reconocimiento
Ejercicio 1
Observa el código:

def saludar():
    print("Hola")
Responde:

1) ¿Cuál es el nombre de la función? 
2) ¿Qué hace def? | Es la palabra reservada de python que se utiliza para crear una funcion
3) ¿Cuál es el bloque de código?""" 
# 1) saludar(): 2) def es la palabra reservada de python que se utiliza para crear una funcion 3) Da una salida diciendo Hola

"""Ejercicio 2
Indica cuáles de estos nombres serían adecuados para funciones:

calcular_total
x
mostrar_menu
hacer
procesar_pago
Explica por qué."""
#calcular_total, procesar_pago, calcular_total
#Porque define de manera directa una funcionalidad que ha de desarrollarse. 

"""Nivel 2 — Creación básica
Ejercicio 3
Crea una función llamada:

mostrar_nombre
Dentro debe imprimir tu nombre.
Luego ejecútala dos veces."""
def mostrar_nombre():
    print("Ambar Rocio")

"""Ejercicio 4
Crea una función llamada: mostrar_menu
Debe imprimir:

1. Jugar
2. Configuración
3. Salir
Invoca la función tres veces.
"""
def mostrar_menu():
    print("\n1. Jugar \n2. Configuración \n3. Salir")

mostrar_menu()
mostrar_menu()
mostrar_menu()

"""Nivel 3 — Análisis y comprensión. Ejercicio 5
Analiza el código:

def mensaje():
    print("Bienvenido")

mensaje()
mensaje()
Responde:

¿Cuántas veces se ejecuta la función?
¿Cuántas veces aparece el mensaje?
¿Por qué las funciones ayudan a reutilizar código?"""
#La función se ejecuta dos veces y dos veces aparece el mensaje tambien.
#Porque evita que escribamos las mismas instrucciones muchas veces al dividirlas en bloques pequeños
#hace que en parte se refactorice el codigo (por asi decirlo)

"""Ejercicio 6
Corrige el error:"""
def saludar() :
    print("Hola")
"""Explica qué estaba mal."""
#Faltaban los dos puntos que forman parte de la sintaxis para crear la funcion

"""Nivel 4 — Pensamiento computacional
Ejercicio 7
Piensa en una aplicación bancaria.
¿Qué funciones podrían existir?
Ejemplo:

iniciar_sesion()
retirar_dinero()
Escribe al menos 5 funciones posibles."""
#cambiar_contrasena()
#depositar_dinero()
#transferir dinero()
#retirar_dinero()
#agregar_beneficiario()
#realizar_reclamacion()
#solicitar_producto()

"""Ejercicio 8
Imagina un videojuego.

Escribe funciones para tareas como:

mover personaje
atacar
mostrar vida
recoger objetos
No necesitas programarlas completas. Solo diseña los nombres de las funciones."""
#iniciar_nivel()
#saltar()
#disparar()
#destruir_enemigo()
#recibir_daño()
#pausar_juego()
#reanudar_juego()
#finalizar nivel()

"""Nivel 5 — Mini reto
Ejercicio 9
Crea un programa que tenga:

una función para mostrar un saludo
una función para mostrar un menú
una función para despedirse
Luego ejecuta todas las funciones."""
def mostrar_saludo():
    print("\n¡Hola!")

def mostrar_menu():
    print("\n 1. Agregar Usuario \n2.Editar Usuario \n3. Eliminar Usuario \n4. Salir")
    
def mostrar_despedida():
    print("\n¡Adiós!")

mostrar_saludo()
mostrar_menu()
mostrar_despedida()
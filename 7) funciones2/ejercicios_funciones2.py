""" Ejercicio 1: El Conversor de Divisas "AirTravel"
Objetivo pedagógico: Este ejercicio busca que practiques cómo dividir un problema en pequeñas responsabilidades independientes.
Piensa como arquitecto de software: La meta no es solo que funcione, sino que el programa esté organizado correctamente.

1) ¿Qué parte calcula? | convertir_usd_a_eur()
2) ¿Qué parte muestra información? | mostrar_resumen()
3) ¿Qué parte coordina todo? | main()

Resultado esperado
--- BIENVENIDO A AIRTRAVEL EXCHANGE ---
¿Cuántos dólares desea cambiar?: 150

=== RESUMEN DE CONVERSIÓN ===
Monto original: 150.0 USD
Monto en Euros: 135.0 EUR
================================
Antes de programar, analiza

Preguntas clave: Sobre responsabilidades"""

"""1) ¿La función que convierte dinero debería usar print()?""" 
#- No, ya eso corresponde a otra funcionalidad.

"""2) ¿La función que imprime el resumen debería hacer cálculos? """
#- No debería, parecido al caso anterior, realizar los cálculos y mostrar los resultados corresponden a dos funcionalidades distintas; 
#si se juntan en una sola función ya no estaría cumpliendo con el principio de que cada funcionalidad sea dividida en bloques de código que
#esté organizado correctamente y que a largo plazo sea mas sencillo para darle mantenimiento. 

"""3) ¿Qué pasa si mañana cambia la tasa de conversión?"""
#- Se modificaría fácilmente el valor asignado a la variable correspondiente

"""4) ¿Qué pasa si luego quieren convertir a yenes o pesos?"""


"""Paso 1 — Diseña las responsabilidades
Debes crear:

Función         	  |  Responsabilidad
convertir_usd_a_eur() |	 Solo calcular
mostrar_resumen()	  |  Solo imprimir
main()	              |  Coordinar todo"""

"""Paso 2 — Completa la función matemática
Tu misión
Crear una función que:

reciba dólares
aplique la conversión
devuelva euros

Piensa antes de escribir
Preguntas guía:"""

"""¿Qué dato necesita la función para trabajar?"""
 # Necesita la cantidad de dolares para poder realizar los cálculos correspondientes

"""¿Debe pedir datos con input()?"""
 # No, porque el objetivo es calcular
 
"""¿Debe mostrar resultados?"""
 # No
 
"""¿Qué debería retornar?"""
 # Euros

def convertir_usd_a_eur(dolares):
    tasa_conversion = 0.90
    euros = dolares * tasa_conversion
    return euros
    
"""Paso 3 — Completa la función visual
Tu misión
Esta función no calcula.

Solo recibe datos ya listos y los muestra de forma ordenada.

Preguntas guía
¿Esta función necesita saber cómo se hizo el cálculo? | No
¿Debería existir una multiplicación dentro de esta función? | No
¿Qué datos necesita recibir para poder imprimir? | El monto de los dolares y la conversion de los euros
"""
def mostrar_resumen(dolares, euros):

    print("\n=== RESUMEN DE CONVERSIÓN ===")
    print(f"\tMonto Original: {dolares}")
    print(f"\tMonto en euros: {euros}")
    print("================================")
    
    
"""Paso 4 — Construye el orquestador
Tu misión
La función principal será el “director de la película”.

Debe:

pedir datos
llamar la función de cálculo
llamar la función visual
Preguntas guía
¿Quién debe pedir el input()?
¿Quién conecta todas las funciones?
¿Dónde debería almacenarse el resultado de la conversión?
¿Qué función conoce todo el flujo completo?"""

def main():
    print("--- BIENVENIDO A AIRTRAVEL EXCHANGE ---")
    dolares = float(input("¿Cuántos dólares desea cambiar?: "))
    euros = convertir_usd_a_eur(dolares)
    mostrar_resumen(dolares, euros)

main()

"""Reto adicional (Opcional)
Nivel 2
Haz que el sistema también convierta a:

pesos colombianos
yenes
libras
Preguntas para pensar
¿Conviene crear una sola función gigante? | No
¿O varias funciones pequeñas? | varias funciones refactorizadas
¿Cómo evitar repetir código?""" 

"""Ejercicio 2: El Validador de Acceso "SecurePass"
Objetivo pedagógico
Aprenderás a separar:

la lógica de decisión
la visualización
la coordinación del sistema
Tu programa debe pensar como un sistema real de seguridad.

Resultado esperado
--- CONTROL DE ACCESO SECUREPASS ---
Ingrese la edad del empleado: 17

=== ESTADO DE SEGURIDAD ===
Resultado: ACCESO DENEGADO. Área restringida para menores de edad.
==============================

Analiza antes de programar
Preguntas clave

¿Quién decide si alguien entra? | validar_acceso()
¿Quién solo muestra mensajes? | mostrar_estado()
¿La función que valida debería usar print()? | No deberia ya que la funcionalidad esta fuera de
¿La función visual debería contener condiciones if? | No
¿Qué ventaja tiene devolver True o False?"""


"""Paso 1 — Diseña la arquitectura
Debes crear:

Función             |	Responsabilidad
validar_acceso()    |	Decide acceso
mostrar_estado()    |	Imprime resultado
main()              |	Coordina el flujo"""

"""Paso 2 — Completa la función lógica
Tu misión
La función debe:

recibir una edad
verificar si es mayor o igual a 18
devolver True o False

Preguntas guía

¿La función necesita imprimir mensajes? | No
¿Qué tipo de dato debería retornar? | si, booleana
¿Qué operador de comparación necesitas? | >=
¿Qué ocurre exactamente cuando una función retorna un booleano? 
- El valor de la misma es verdadero o falso y ha de utilizarse en varias validaciones en caso de ser necesario
Código base"""

def validar_acceso(edad):
    mayor_de_edad = True
    if edad >= 18:
        return mayor_de_edad 
    else:
        return not mayor_de_edad
    
    
"""Paso 3 — Completa la función visual
Tu misión
Esta función debe:
recibir el resultado (True o False)
mostrar el mensaje correcto

Preguntas guía
¿La función sabe cómo se hizo la validación? | No
¿Solo necesita conocer el resultado? | Solo el resultado de la validación
¿Qué estructura condicional usarás? | if, else
Código base"""

def mostrar_estado(acceso):

    print("\n=== ESTADO DE SEGURIDAD ===")
    if acceso:
       print("Resultado: ACCESO DENEGADO. Área restringida para menores de edad.")
    else:
        print("Resultado: ACCESO PERMITIDO. Área Permitida para mayores de edad.")
    print("==============================")
    
    
"""Paso 4 — Construye el sistema central
Tu misión
La función principal debe:

solicitar edad
llamar la validación
enviar el resultado al panel visual

Preguntas guía
¿Quién debe usar input()? | main2()
¿Dónde se conecta todo?   | en main2()
¿Qué variable almacenará el resultado booleano? | validacion
¿Qué significa realmente “orquestar” un programa? 
- En mis propias palabras sería estructurarlo de la manera correcta, uniendo y combinando las partes que
  sean necesarias entre sí para que no haya redundancia de codigo y el mismo pueda ser reutilizable
"""

def main2():
    print("--- CONTROL DE ACCESO SECUREPASS ---")
    edad = int(input("Ingrese la edad del empleado: "))
    validacion = validar_acceso(edad)
    mostrar_estado(validacion)

main2()
"""**Ejercicio 1 — Mayor de edad
Solicita la edad de una persona.

Si tiene 18 o más → mostrar: "Eres mayor de edad"
Si no → mostrar: "Eres menor de edad"
Tip
Piensa qué conjunto representa: edad >= 18"""

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

"""**Ejercicio 2 — Temperatura
Solicita una temperatura.

Si es mayor a 30 → mostrar: "Hace calor"
Tip
Aquí solo necesitas un if."""

temperatura = float(input("\nIngrese la temperatura: "))
if temperatura > 30:
    print("Hace calor")

"""**Ejercicio 3 — Contraseña básica
Pide una contraseña.

Si la contraseña es "python123": mostrar "Acceso permitido"
Si no: mostrar "Contraseña incorrecta"
Tip
Usa: == para comparar textos."""

password_onfile = "python123"
password_inserted = input("\nIngrese la contraseña: ")
if password_inserted == password_onfile:
    print("Acceso Concedido")
else: 
    print("Contraseña Incorrecta")

"""**Ejercicio 4 — Número positivo o negativo
Solicita un número.

Si es positivo → mostrar: "Número positivo"
Si es negativo → mostrar: "Número negativo"
Si es cero → mostrar: "Es cero"
Tip
Observa cómo las condiciones son independientes, no hay subconjuntos."""

numero = int(input("\nIngrese el numero: "))
if numero == 0:
    print("es cero")
elif numero > 0:
    print("¡El número es positivo!")
else: print("¡El número es negativo!")

"""**Ejercicio 5 — Semáforo
Solicita un color:

"rojo"
"amarillo"
"verde"
Inventa una acción para cada color y muestra la acción correspondiente.

Tip
Puedes resolverlo con if-elif o con match-case."""
color = input("\nIngrese uno de estos colores (Rojo, Amarillo o Verde)): ")
match color:
    case "rojo":
        print("¡Peligro! Mantengase Alejado")
    case "Amarillo":
        print("¡Precaución! Sea precavid@ al gravitar por esta área")
    case "verde":
        print("Zona fuera de peligro")

"""**Ejercicio 6 — Sistema de notas
Solicita una nota.

4.5 o más → "Excelente"
3.0 o más → "Aprobado"
menos de 3.0 → "Reprobado"
Tip importante
Las condiciones más específicas deben ir primero."""

nota = float(input("\nIngrese la calificación: "))
match nota:
    case _ if nota >= 4.5:
        print("¡Excelente!")
    case _ if nota >= 3.0:
        print("¡Aprobado!")
    case _ if nota < 3.0:
        print("¡Reprobado!") 

"""**Ejercicio 7 — Sistema de descuentos
Solicita el valor de una compra.

mayor a 500 → 30% descuento
mayor a 100 → 10% descuento
cualquier otro caso → sin descuento
Mostrar:

descuento aplicado
total a pagar
Tip
Piensa en subconjuntos o subrangos contenidos unos dentro de otros."""

compra = float(input("\nIngrese el valor de la compra: "))
if compra > 500:
    print(f"El valor de la compra con el 30% de descuento: {compra - (compra*0.30)}")
elif compra > 100:
    print(f"El valor de la compra con el 10% de descuento: {compra - (compra*0.10)}")
else: print(f"Valor: {compra} , no descuento aplicado.")
from datetime import datetime

""" NIVEL AVANZADO
Ejercicio 16 — Sistema de envío de paquetes
Solicita:

peso del paquete
tipo de envío
Reglas:

Envío nacional
hasta 1kg → $5
hasta 5kg → $10
más de 5kg → $20
Envío internacional
hasta 1kg → $15
hasta 5kg → $30
más de 5kg → $50
Tip
Combina match-case con if."""

peso = float(input("Ingrese el peso del paquete: "))
tipo_de_envio = int(input("\nSeleccione el tipo de envio: \n1) Envío Nacional \n2) Envío Internacional " ))

match tipo_de_envio:
    case 1:
        if peso >= 0.1 and peso <= 1.0:
            print("Precio: $5")
        elif peso >= 1.1 and peso <= 5.0:
            print("Precio: $10")
        elif peso > 5.0:
            print("Precio: $20")
    case 2:
        if peso >= 0.1 and peso <=1.0:
            print("Precio: $15")
        elif peso >= 1.1 and peso <= 5.0:
            print("Precio: $30")
        elif peso > 5.0:
            print("Precio: $50")
    
"""Ejercicio 17 — Sistema de autenticación bancaria
Solicita:

usuario
contraseña
código de seguridad
Reglas:

Usuario correcto: "cliente"
Contraseña correcta: "banco123"
Código correcto: "9999"
Mensajes posibles:

acceso completo
contraseña incorrecta
código inválido
usuario no encontrado
Tip
Piensa en decisiones jerárquicas."""

usuario_correcto = "cliente"
contrasena_correcta = "banco123"
codigo_correcto = "9999"
usuario = input("Usuario: ")
contrasena = input("Contraseña: ")
codigo = int(input("Codigo OTP(4 dígitos): "))

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Acceso Completo")
    if codigo == codigo:
            print("Código OTP Correcto")
    else: print("Código OTP incorrecto")
elif usuario != usuario_correcto or contrasena != contrasena_correcta:
    print("Usuario o Contraseña incorrecta, Intente de nuevo.")

"""Ejercicio 18 — Diagnóstico básico médico
Solicita:

temperatura corporal
si tiene tos (si/no)
si tiene dificultad respiratoria (si/no)
Reglas:

fiebre + tos + dificultad respiratoria → "Atención médica urgente"
fiebre + tos → "Posible infección"
solo fiebre → "Monitorear síntomas"
ningún síntoma → "Estado estable"
Tip
Aquí las condiciones pueden superponerse."""

temperatura_corporal = float(input("Temperatura Corporal: "))
tos = int(input("¿Tiene tos? \n\n1) Si \n2) No "))
dificultad_respiratoria = int(input("¿Tiene dificultad respiratoria? \n\n1) Si \n2) No "))

if temperatura_corporal > 37.5 and tos == 1 and dificultad_respiratoria == 1:
    print("¡COVID, Atención médica urgente!")
elif temperatura_corporal > 37.5 and tos == 1:
    print("Posible infección")
elif temperatura_corporal > 37.5:
    print("Monitorear síntomas")
else: print("Estado Estable")

"""Ejercicio 19 — Sistema de niveles de videojuego
Solicita:

vida
energía
armadura
Reglas:

vida <= 0 → "Game Over"
vida < 20 y armadura == 0 → "Estado crítico"
energía < 10 → "Energía baja"
cualquier otro caso → "Jugador estable"
Tip
Las condiciones más específicas primero."""

vida = int(input("Vida: "))
energia = int(input("energía: "))
armadura = int(input("Armadura: "))

if vida <= 0:
    print("Game Over!")
elif vida < 20 and armadura == 0:
    print("Estado Crítico")
elif energia < 10:
    print("Energía Baja")
else: print("Jugador estable")

"""Ejercicio 20 — Plataforma de descuentos premium
Solicita:

valor de compra
si es miembro premium
si tiene cupón
Reglas:

compra > 1000 y premium → 40% descuento
compra > 500 o tiene cupón → 20% descuento
compra > 100 → 10% descuento
cualquier otro caso → sin descuento
Mostrar:

descuento
total final
Tip
Aquí practicarás:

subconjuntos
condiciones compuestas
orden lógico """

valor_compra = float(input("\n\nValor de la compra: "))
miembro_premium = int(input("¿Tiene usted membresía premium?: 1) Sí 2) No"))
cupon = ("¿Tiene usted un cupón activo?")

if valor_compra > 1000 and miembro_premium == 1:
    print(f"Valor de compra con 40% de descuento: {round(valor_compra - (valor_compra*0.40), 2)}")
elif valor_compra > 500 or cupon == 1:
    print(f"Valor de compra con 20% de descuento: {round(valor_compra - (valor_compra*0.20), 2)}")
elif valor_compra > 100:
    print(f"Valor de compra con 10% de descuento: {round(valor_compra - (valor_compra*0.10), 2)}")
else: print("Descuento No Aplicable")

"""Ejercicio 21 — Asistente virtual
Solicita un comando:

"hora"
"fecha"
"clima"
"salir"
Usa match-case.

Además:

si el comando está vacío: mostrar "Entrada inválida"
Tip
Valida antes del match."""

comando = input(f"Hola soy Emma, Asistente virtual. Ingresa un comando (hora, fecha, clima, salir): ")
match comando:
    case "hora":
        print(f"Emma, Asistente Virtual: Hola! la hora actual es: {datetime.now().time()} ;)")
    case "fecha":
        print(f"Emma, Asistente Virtual: Hola! la fecha actual es: {datetime.now().date()} :D")
    case "clima":
        print(f"Emma, Asistente Virtual: Hola! el clima actual es: Soleado :)")
    case "salir":
        print("¡Le asistio Emma, asistente virtual. Quet tenga buen día! ;*")
    case _:
        print("Entrada inválida")
        
"""Ejercicio 22 — Clasificador de triángulos
Solicita tres lados.

Reglas:

todos iguales → equilátero
dos iguales → isósceles
todos diferentes → escaleno
Validar además:

ningún lado puede ser menor o igual a cero
Tip
Aquí aparecen múltiples comparaciones."""


lado1 = int(input("Ingrese el valor del primer lado"))
lado2 = int(input("Ingrese el valor del segundo lado"))
lado3 = int(input("Ingrese el valor del tercer lado"))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Valor inválido. Ningún lado puede ser menor o igual a cero.")
if lado1 == lado2 == lado3:
    print("Todos los lados son iguales. Este es un triángulo Equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("sólo dos lados del triángulo son iguales. Este es un triángulo Isóceles.")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Todos los lados son distintos. Este es un triángulo Escaleno.")



"""Ejercicio 23 — Sistema de permisos
Solicita:

rol
estado de cuenta
Reglas:

admin
acceso total
editor
acceso parcial
visitante
solo lectura
Pero:

si la cuenta está suspendida: bloquear acceso completamente
Tip
La suspensión debe evaluarse primero."""

rol = int(input("\nSeleccione la opción correcta de acuerdo con su rol asignado: \n\n1) Administrador \n2) Editor \n3) Visitante: "))
estado_cuenta = int(input("\nSeleccione el estado de cuenta actual: \n\n1) Activa \n2)Suspendida:"))

if estado_cuenta == 2:
    print("Acceso Bloqueado. Contacte al administrador.")
elif rol == 1 and estado_cuenta == 1:
    print("Acceso total concedido. \n\n Cuenta Activa")
elif rol == 2 and estado_cuenta == 1:
    print("Acceso parcial concedido. \n\n Cuenta Activa")
elif rol == 3 and estado_cuenta == 1:
    print("Acceso de solo lectura. \n\n Cuenta Activa")
"""Ejercicio 24 — Plataforma educativa
Solicita:

nota
porcentaje de asistencia
Reglas:

nota >= 4.5 y asistencia >= 80 → "Aprobado con honores"
nota >= 3.0 y asistencia >= 60 → "Aprobado"
nota >= 3.0 y asistencia < 60 → "Reprobado por inasistencia"
cualquier otro caso → "Reprobado"
Tip
Las condiciones compiten entre sí."""

calificacion = float(input("Ingrese la Calificación: "))
asistencia = int(input("Ingrese el porcentaje de la asistencia (en escala del 1 al 100): "))
match (calificacion, asistencia):
    case (c,a) if c >= 4.5 and a >= 80:
        print("Aprobado con honores")
    case (c,a) if c >= 3.0 and a >= 60:
        print("Aprobado")
    case (c,a) if c >= 3.0 and a < 60:
        print("Reprobado por inasistencia")
    case _ :
        print("Reprobado")

"""Ejercicio 25 — Sistema de recomendaciones musicales
Solicita:

estado de ánimo
Opciones:

feliz
triste
relajado
motivado
Mostrar recomendación musical diferente para cada caso usando match-case.

Agregar:

caso por defecto para estados desconocidos."""

animo = int(input("Seleccione el estado de ánimo: \n\n1)Feliz \n2) Triste \n3) Relajado \n4) Motivado"))

match animo:
    case 1:
        print("Recomendaciones cuando estás Feliz: Salsa, Merengue, Bachata, Regueton, entre otras opciones")
    case 2:
        print("Recomendaciones cuando estás Triste: Baladas, Baladas Pop, entre otras opciones")
    case 3: 
        print ("Recomendaciones cuando estás Relajado: Jazz, Instrumental, Clásica, Acústico o Falk suave, entre otras opciones")
    case 4:
        print("Recomendaciones cuando estás Motivado: Pop, R&B, HipHop, Rap, Rock Clásico, Soul, Funk, Disco, Electronic entre otras opciones")
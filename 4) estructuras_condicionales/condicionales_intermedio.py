""" NIVEL INTERMEDIO
Ejercicio 8 — Login de plataforma
Solicita:

usuario
contraseña
Reglas:

Si el usuario es "admin" y la contraseña es "1234": mostrar "Bienvenido administrador"
Si el usuario existe pero la contraseña es incorrecta: mostrar "Contraseña incorrecta"
Si el usuario no existe: mostrar "Usuario no encontrado"
Tip
Aquí aparecen condiciones compuestas."""

admin = "admin"
password = 1234

usuario = input("Usuario: ")
contrasena = int(input("Contraseña: "))

if usuario == admin and contrasena == password:
    print("¡Bienvenido Usuario Administrador!")
elif usuario == admin and contrasena != password:
    print("Contraseña incorrecta")
else: print("Usuario No Encontrado")

"""Ejercicio 9 — Cajero automático
Solicita:

saldo disponible
valor a retirar
Reglas:

Si el retiro es mayor que el saldo: mostrar "Fondos insuficientes"
Si el retiro es igual al saldo: mostrar "Retiro realizado. Cuenta vacía"
Si el retiro es menor: mostrar saldo restante
Si el retiro es negativo: mostrar "Valor inválido"
Tip
La validación del número negativo debe ir primero porque los datos inválidos deben bloquear el resto del sistema."""

saldo_disponible = float(input("Saldo Disponible: "))
retiro = float(input("Saldo a retirar: "))

match retiro:
    case x if x < 0:
        print("Valor inválido. Sistema Bloqueado.")
    case x if x > saldo_disponible:
        print("Fondos Insuficientes.")
    case x if x == saldo_disponible:
        print("Retiro realizado. Cuenta vacía.")
    case x if x < saldo_disponible:
        saldo_disponible = saldo_disponible - retiro
        print(f"Saldo Restante: {saldo_disponible}")

"""Ejercicio 10 — Clasificación de usuarios
Solicita la edad.

Clasificar:

menor de 13 → niño
menor de 18 → adolescente
menor de 60 → adulto
cualquier otro caso → adulto mayor
Tip
Piensa en rangos contenidos."""

edad = int(input("Ingrese su edad: "))
if edad < 13:
    print("Niño")
elif edad < 18:
    print("Adolescente")
elif edad < 60:
    print("Adulto")
else: print("Adulto Mayor")

"""Ejercicio 11 — Streaming de películas
Solicita:

edad
tipo de contenido
Reglas:

contenido "terror" requiere 18 años
contenido "acción" requiere 13 años
contenido "infantil" disponible para todos
Mostrar si puede acceder o no.

Tip
Usa condiciones compuestas con and."""

edad_ = int(input("Ingrese su edad: "))
pelicula = int(input("Seleccione la opcion, tipo de pelicula que desea ver: 1) Terror  2) Acción  3) Infantil"))
if edad_ > 18 and pelicula == 1:
    print("Acceso Concedido para peliculas de terror.")
elif edad_ > 13 and pelicula == 2:
    print("Acceso Concedido para peliculas de acción.")
elif edad_ > 0 and pelicula == 3:
    print("Acceso concedido para peliculas infantiles.")

"""Ejercicio 12 — Validación de correo
Solicita un correo electrónico.

Reglas:

Si contiene "@" y "." → "Correo válido"
Si no: → "Correo inválido"
Tip
Usa: in"""

email = input("Ingrese su correo electrónico: ")

if "@" in email and "." in email:
    print("Correo Válido")
else: print("Correo Inválido")

"""Ejercicio 13 — Menú interactivo
Mostrar:

1. Ver perfil
2. Configuración
3. Ayuda
4. Salir
Solicitar opción y responder según el caso.

Tip
Ideal para practicar match-case."""

opcion = int(input("Seleccione la opción deseada: \n\n1) Ver perfil. \n2) Configuración  \n3) Ayuda  \n4)Salir"))

match opcion:
    case 1:
        print("Ver Perfil")
    case 2:
        print("Configuración")
    case 3:
        print("Ayuda")
    case 4:
        print("Salir")

"""Ejercicio 14 — Clasificación de batería
Solicita porcentaje de batería.

80 o más → "Batería alta"
30 a 79 → "Batería media"
1 a 29 → "Batería baja"
0 → "Dispositivo apagado"
Tip
Piensa cómo ordenar las condiciones."""

bateria = int(input("Ingrese el porcentaje de la batería: "))


if bateria >= 80:
    print("Batería Alta")
elif bateria > 30 and bateria <= 79:
    print("Batería Media")
elif bateria > 1 and bateria <= 29:
    print("Batería Baja")
elif bateria == 0:
    print("Dispositivo Apagado")    

"""Ejercicio 15 — Validación de acceso a evento
Solicita:

edad
si tiene boleta (si/no)
Reglas: Solo entra si: tiene 18 o más
y posee boleta Mostrar:

acceso permitido
acceso denegado
Tip
Usa: and"""

age = int(input("Ingrese su edad: "))
boleta = int(input("¿Tiene usted una boleta? 1. Si 2. No: "))
if age >= 18 and boleta == 1:
    print("Acceso Concedido") 
else: print("Acceso Denegado")
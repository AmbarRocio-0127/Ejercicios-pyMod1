""" 1. Operadores Aritméticos. El objetivo es dominar los números y los símbolos especiales (//, %, **).
- El Reparto: Tienes 45 manzanas y quieres darle 7 a cada uno de tus amigos. ¿Cuántas manzanas te sobran?
Usa el operador de módulo (%).

- El Cubo: Calcula cuánto es 5 ** 3 usando el operador de potencia.

- Billetera Vacía: Si tienes $100 y compras 3 hamburguesas de $22 cada una, ¿cuánto dinero te queda?

- Cajas Completas: Tienes 130 libros y en cada caja caben 12. ¿Cuántas cajas completamente llenas tendrás?
Usa división entera (//).

- Promedio Rápido: Calcula el promedio de estas tres notas: 80, 95 y 100. Recuerda usar paréntesis.
"""
Manzanas = 45
distribucion = 7
print(f"\n1) Total de manzanas: {Manzanas}", f" para distribuirse entre {distribucion}")
print(f"Manzanas sobrantes: {Manzanas%distribucion}")

print(f"\n 2) El cubo de la operacion 5**2 es: {5**3}")

print(f"\n 3) Si tienes $100 y compras 3 hamburguesas de $22 cada una, ¿cuánto dinero te queda? : {100-(22*3)}")

print(f"\n 4) Tienes 130 libros y en cada caja caben 12. ¿Cuántas cajas completamente llenas tendrás?: {130//12}")

print(f"\n 5) Calcula el promedio de estas tres notas: 80, 95 y 100: {(80+95+100)//3}")

"""  2. Operadores Relacionales. Aquí la respuesta siempre debe ser True o False.
- ¿Es Par? Escribe una comparación que verifique si el residuo de la expresión numero % 2 es igual a 0. Siendo numero una variable que puedes cambiar.

- Cupo Lleno: Tienes una variable: invitados = 50. Escribe una comparación para saber si los invitados son menores o iguales a 60.

- Contraseña. Tienes: clave_real = "Python123", intento = "python123" Compara si son exactamente iguales. Observa cuidadosamente las mayúsculas y minúsculas.

- Diferencia: Verifica si el resultado de 10 / 2 es diferente de 5.

- Edad Legal: Crea una variable edad. Escribe la comparación para saber si esa edad es mayor o igual a 18.

"""
number = int(input("Introduzca el numero: "))
result = number%2 == 0
print("\n",result)

invitados = 50
validacion = invitados <= 60
print("\n",validacion)

clave_real = "Python123"
intento = "python123"
comparacion = clave_real == intento
print("\n",comparacion)

resultado = 10/2!= 5
print("\n",resultado)


edad = int(input("\nIntroduzca la edad: "))
validation = edad >= 18
print("\n",validation)

""" 3. Operadores Lógicos (and, or, not) Combinando condiciones de la vida real.

1) Examen y Asistencia: Un alumno aprueba si su nota es mayor a 70 y su asistencia es mayor al 80%.
2) Día de Descanso: Es día de descanso si es sábado o si es domingo.
3) Sensor de Luz: Una lámpara se enciende si hay movimiento y no es de día.
4) Bono de Regalo: Un cliente recibe un regalo si su compra es mayor a $500 o si es su primer pedido (True).
5) Validación Inversa: Tienes la variable: usuario_baneado = True
Escribe una expresión usando not que devuelva True solo si el usuario no está baneado."""

nota = int(input("Ingrese la calificacion: "))
asistencia = int(input("Ingrese el porcentaje de asistencia: "))
Aprobado = nota > 70 and asistencia > 80
print("\n1) ",Aprobado)

dia_actual = input("Ingrese dia actual: ")
dia_de_descanso = dia_actual == "sabado" or dia_actual == "domingo"
dia_laboral = not dia_de_descanso
print(dia_de_descanso)

hay_movimiento = True
es_noche = True
encendido = hay_movimiento and es_noche
print(encendido)

es_mayor = int(input("Ingrese el monto: "))
primer_pedido = int(input("¿es este su primer pedido? Seleccione la opción: 1) Si. 2)No "))
bono_regalo = es_mayor > 500 and primer_pedido == 1
print(bono_regalo)

usuario_baneado = True
acceso_autorizado = not usuario_baneado
print(usuario_baneado)

""" 4. Evaluación de Expresiones (Mezcla de Todo)
Resuelve paso a paso en papel o en la consola.

Nivel Básico
resultado = 10 + 5 * 2 ** 2
¿Qué operación se realiza primero?

Nivel Lógico
resultado = (5 > 3) and (10 < 5 or 7 == 7)
Nivel "Sistemas"
acceso = (usuario == "admin") or (intentos < 3 and not bloqueado)
Prueba con:

usuario = "user"
intentos = 2
bloqueado = False
Nivel Matemático
valor = 20 // 3 + 10 % 3
Resuelve mentalmente o en papel antes de usar la consola.

El Mega Reto
final = (100 / 2 > 40) and (10 * 2 == 20) and not (5 + 5 <= 9)"""

resultado_ = 10 + 5 * 2 ** 2
print(resultado_)
#Se evalua la potencia primero, luego la multiplicacion y luego la suma

resultado2 = (5 > 3) and (10 < 5 or 7 == 7)
print(resultado2)
#El resultado es true porque dentro de la segunda se cumple al menos 1 de las condiciones
#lo que hace que sea true. De la misma forma que es true la primera validacion en base al resultado que devuelve

usuario = "user"
intentos = 2
bloqueado = False

acceso = (usuario == "admin") or (intentos < 3 and not bloqueado)
#devuelve true porque se cumple al menos 1 de las 2 condiciones

valor = 20 // 3 + 10 % 3
print(valor)
#Se ejecuta primero la division entera, Luego el residuo y luego se efectua la suma de los resultados de las operaciones anteriores

""" 5. Casos de "Lógica de Negocio"
Situaciones reales para pensar como programador.

Escribe el código que resuelva cada caso usando operadores lógicos y relacionales.

1) Cajero Automático
Puedes sacar dinero si: monto_a_retirar es menor o igual al saldo_cuenta y el monto es múltiplo de 10
Pista: monto_a_retirar % 10 == 0

2) Streaming
Una película es apta si: edad_usuario es mayor a 13 o si tiene permiso_parental (True)

3) Tienda Online
El envío es gratis si: la compra es mayor a $100 y el destino es "Local"

4) Videojuego
El jugador pierde una vida si: toca lava o cae al vacío Pero no pierde vida si tiene el escudo_activo.

5) Login Seguro: El botón de "Entrar" se activa solo si: el usuario no está vacío
y la contraseña tiene más de 8 caracteres Pista: len(password) > 8""" 

saldo_cuenta = float(input("Depósito: "))
monto_a_retirar = float(input("Monto a retirar: "))
monto_a_retirar = monto_a_retirar <= saldo_cuenta and monto_a_retirar % 10 == 0
print(monto_a_retirar) #True or False

permiso_parental = True
edad_usuario = int(input("Ingrese su edad: "))
pelicula = edad_usuario > 13 or permiso_parental
print(pelicula) #True or False

compra = float(input("Ingrese el monto de la compra: "))
destino = input("Destino de entrega: ")
envio_gratis = compra > 100 and destino == "Local"
print(envio_gratis) #True or False

#OJO
toca_lava = True
cae_vacio = True
escudo_activo = False
vida_jugador = (toca_lava == True or cae_vacio == True) and not escudo_activo
print(vida_jugador) #True or False

boton_entrar = False
usuario_ = input("Usuario: ")
contrasena = input("Contraseña: ")
login_seguro = (usuario_ != "" and len(contrasena) > 8) and not boton_entrar
print(login_seguro)
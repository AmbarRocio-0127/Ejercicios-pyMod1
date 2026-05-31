""" **Ejercicio 1. Saludo Personalizado.**
- Practicar input() y print().
  Instrucciones
- Solicita el nombre del usuario.
- Guarda el valor en una variable.
- Muestra un saludo personalizado."""

nombre =input("Introduce tu nombre: ")
print(f"\nHola como te llamas?",nombre)
print(f"\nHola {nombre}", "Bienvenido a Python")

""" Ejercicio 2
Practicar conversión a int
**Instrucciones**
-Solicita la edad del usuario.
-Convierte el valor a entero.
 Muestra:
- la edad actual
- la edad dentro de 10 años"""

edad = int(input("Introduzca su edad: "))
print("\nTu edad es: ", edad)
print("En 10 años tendras: ", edad+10)

"""Ejercicio 3
Practicar variables numéricas.
#Instrucciones#
- Solicita dos números enteros.
- Convierte ambos valores.
Muestra:
- suma
- resta
- multiplicación"""

Numero1 = int(input("\nIntroduzca el primer numero: "))
Numero2 = int(input("Introduzca el segundo numero: "))

print("\nSuma:", (Numero1 + Numero2))
print("resta: ", (Numero1 - Numero2))
print("Multiplicacion: ", (Numero1 * Numero2))

print(f"\nSuma:{Numero1+Numero2}")
print(f"\nResta:{Numero1-Numero2}")
print(f"\nMultiplicación:{Numero1*Numero2}")

""" Promedio de Notas. Practicar float.
**Instrucciones**
- Solicita 3 notas decimales.
- Calcula el promedio.
- Muestra el resultado con 2 decimales."""

Nota1 = float(input("\nIntroduzca la primera calificación: "))
Nota2 = float(input("Introduzca la segunda calificación: "))
Nota3 = float(input("Introduzca la tercera calificación: "))

Promedio = ((Nota1+Nota2+Nota3)/3)

print(f"\nEl promedio de las calificaciones es de: {round(Promedio,2)}")

"""Ejercicio 5. Datos personales
- Combinar varios tipos de datos.
**Instrucciones**
Solicita:

- nombre (str)
- edad (int)
- altura (float)
- si es estudiante (bool simulado)
Luego muestra toda la información organizada."""

Nombre_ = str(input("\nintroduzca su nombre: "))
Edad_ = int(input("Introduzca su edad: "))
Altura = float(input("Introduzca su altura: "))
Estudiante = input("¿Eres estudiante? Y/N: ")

print(f"\n Nombre: {Nombre_}")
print(f"Edad: {Edad_}")
print(f"Altura: {Altura}")

if Estudiante == "Y":
    print("Estudiante: Activo")
if Estudiante == "N":
    print("Estudiante: Inactivo/No registrado")
    
""" Ejercicio 6. Conversion de temperatura
Operaciones con Float.
F = (C × 9/5) + 32
- Solicita una temperatura en Celsius.
- Convierte a float.
- Calcula Fahrenheit.
- Muestra el resultado."""

temperaturaCelsius = float(input("\nIntroduzca la temperatura en Grados Celsius: "))
F = round((temperaturaCelsius * 9/5) + 32,2)
print(f"\nTemperatura en Grados Farenheit: {F}")

""" Ejercicio 7. Calculo del area de un rectángulo
Practicar variables y float.
A = base × altura
Solicita:
- base
- altura
- Calcula el área.
- Muestra el resultado con 2 decimales."""

base = float(input("Introduzca la base: "))
altura = float(input("Introduzca la altura: "))
area = base*altura

print(f"El área del rectángulo equivale a: {area}")

"""Ejercicio 8. Conversión de texto a número
Comprender que input() devuelve texto.
**Instrucciones**
- Solicita dos números SIN convertirlos.
- Intenta sumarlos.
- Observa el resultado.
- Luego conviértelos usando int().
- Realiza nuevamente la suma."""

numero3 = int(input("\nIngrese el primer número: "))
numero4 = int(input("\nIngrese el segundo número: "))

resultado = numero3 + numero4
print(f"\nEl resultado es: {resultado}")
#Sin la conversion a entero simplemente se leen los valores introducidos como si fuera una cadena de texto
#y esos valores introducidos los muestra juntos, porque esta concatenando esas cadenas
# sin efectuar la operacion

"""Mini formulario
Practicar múltiples entradas.
* Solicita: nombre, ciudad, edad y peso"""

Name = input("Introduzca su nombre: ")
City = input("Introduzca su ciudad: ")
Age = int(input("Introduzca su edad: "))
Weight = float(input("Introduzca su peso: "))

print(f"Nombre: {Name}")
print(f"Ciudad: {City}")
print(f"Nombre: {Age}")
print(f"Peso: {Weight}")

""" Ejercicio 10 — Precio con IVA
Practicar float y formato.
*total = precio + (precio × iva)*
Solicita el precio de un producto.
- Usa IVA = 0.19
- Calcula el total.
- Muestra:
  subtotal
  IVA
  total final"""
  
IVA = 0.19
Precio = float(input("\nIntroduzca el Precio del producto seleccionado: "))
total = round(Precio + (Precio*IVA))
print("\n==========================================")
print("\t TECNOLOGY COMPANY SRL")
print("\t   RNC: 123-45678-9")
print("\t   Santo Domingo, RD")
print("==========================================")
print("\nFactura No: 0016574")
print("Fecha: 13/05/2026")
print("------------------------------------------")
print("\nCantidad\t Precio\t\tTotal")
print(f"\n1\t\t {Precio}",f"\t{total}")
print("\n\n------------------------------------------")
print(f"\nSubtotal: {total}")
print(f"\nIVA: {total*IVA}")
print("\n------------------------------------------")
print("\n¡Gracias por su compra!")

"""Conversion de Tipos
*Practicar conversiones explícitas.*
Crea variables: numero_texto = "100", decimal_texto = "3.14" """

a = "100"
pi = "3.14"
entero = 2
print(type(a))
print(type(pi))
print(type(entero))

print(type(int(a)))
print(type(float(pi)))
print(type(str(entero)))

"""Ejercicio 12 — Información del producto
**Instrucciones**
**Solicita:
- nombre del producto
- precio
- cantidad

**Calcula:
- subtotal
- total a pagar"""

Producto = str(input("\nNombre del producto: "))
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
subtotal = round(float(precio*cantidad))

print(f"Producto: {Producto}")
print(f"Precio: {precio}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: {subtotal}")
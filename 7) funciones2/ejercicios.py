# Ejercicio 1 - Conversor de divisas "AirTravel"

def convertir_usd_a_eur(dolares): 
    tasa_conversion = 0.90
    euros = dolares * tasa_conversion
    return euros

def mostrar_resumen(dolares, euros):
    print("\n=== RESUMEN DE CONVERSIÓN ===")
    print(f"\tMonto Original: {dolares}")
    print(f"\tMonto en euros: {euros}")
    print("================================")
    
def main():
    print("--- BIENVENIDO A AIRTRAVEL EXCHANGE ---")
    dolares = float(input("¿Cuántos dólares desea cambiar?: "))
    euros = convertir_usd_a_eur(dolares)
    mostrar_resumen(dolares, euros)
    
main()

#Ejercicio 2: El Validador de Acceso "SecurePass

def validar_acceso(edad):
    mayor_de_edad = True
    if edad >= 18:
        return mayor_de_edad 
    else:
        return not mayor_de_edad
    
def mostrar_estado(acceso):

    print("\n=== ESTADO DE SEGURIDAD ===")
    if acceso:
       print("Resultado: ACCESO DENEGADO. Área restringida para menores de edad.")
    else:
        print("Resultado: ACCESO PERMITIDO. Área Permitida para mayores de edad.")
    print("==============================")
    
def main2():
    print("--- CONTROL DE ACCESO SECUREPASS ---")
    edad = int(input("Ingrese la edad del empleado: "))
    validacion = validar_acceso(edad)
    mostrar_estado(validacion)

main2()
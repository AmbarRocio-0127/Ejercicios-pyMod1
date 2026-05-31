# 1. Sistema de evaluación de puntaje. (Este ejercicio fue desarollado en clase)
#***------¡CORREGIDO!--------***
puntaje = 95

if puntaje > 90:
    print("Excelente")
elif puntaje > 70:
    print("Aprobado")
else:
    print("Reprobado")

edad_usuario = 14
if edad_usuario < 15:
    print("Mostrar catalogo de: Dibujos animados")
elif edad_usuario < 18:
    print("mostrar catalogo: series juveniles")
else:
    print("mostrar catalogo: peliculas de accion/terror")


# EJERCICIOS PARA CODE REVIEW MIENTRAS VAS EN EL METRO

# 2. Sistema de clasificación de incidencias en una plataforma bancaria
#***------¡CORREGIDO!--------***
monto_fraudulento = 7500

if monto_fraudulento > 10000:
    print("Bloqueo total y reporte a entidades regulatorias")

elif monto_fraudulento > 5000:
    print("Congelar cuenta y notificar al equipo antifraude")

elif monto_fraudulento > 1000:
    print("Caso marcado como sospechoso")

else:
    print("Transacción considerada normal")

# ------------------------------------------------------------------

# 3. Sistema de alertas de ciberseguridad
#***------¡CORREGIDO!--------***
intentos_fallidos = 12

if intentos_fallidos > 20:
    print("Bloqueo permanente y reporte automático")

elif intentos_fallidos > 10:
    print("Bloquear cuenta y notificar al equipo de seguridad")

elif intentos_fallidos > 3:
    print("Mostrar captcha al usuario")

else:
    print("Acceso normal")


"""
A. El código está mal planteado porque las condiciones más generales
   aparecen antes que las más específicas, haciendo que algunos bloques
   nunca puedan ejecutarse. (correcta, cuando el codigo estaba desorganizado) ✅

B. El código está bien escrito porque Python siempre evalúa automáticamente
   primero las condiciones más específicas aunque estén debajo.  (X)

C. El código funciona correctamente porque si una condición es más grave,
   Python la ejecutará después de pasar por las anteriores. (X)
"""

# 4. Sistema de asignación de soporte técnico en una empresa SaaS
#***------¡CORREGIDO!--------***
tiempo_caido = 180

if tiempo_caido > 300:
    print("Activar protocolo de emergencia y compensación automática")

elif tiempo_caido > 120:
    print("Escalar incidente al equipo senior")

elif tiempo_caido > 30:
    print("Asignar caso al soporte estándar")

else:
    print("Monitoreo normal")

"""

A. El código tiene un problema lógico porque las condiciones generales
   aparecen antes que las críticas, evitando que ciertos niveles de
   escalamiento se ejecuten. ✅

B. El código está correctamente estructurado porque Python detecta
   automáticamente cuál condición representa el caso más grave.

C. El código funciona bien porque un incidente debe pasar primero por
   todos los niveles inferiores antes de activar acciones mayores.
"""

# 5. Sistema de moderación automática en una red social

reportes_usuario = 25

if reportes_usuario > 50:
    print("Bloqueo permanente y eliminación de contenido")

elif reportes_usuario > 15:
    print("Suspender cuenta y enviar a revisión manual")

elif reportes_usuario > 5:
    print("Limitar temporalmente algunas funciones de la cuenta")

else:
    print("Cuenta operando normalmente")

"""
A. El código presenta un error lógico porque las condiciones más amplias
   están antes que las más específicas, haciendo que sanciones más graves
   nunca lleguen a ejecutarse. ✅

B. El código está bien diseñado porque Python revisa todas las condiciones
   antes de decidir cuál acción aplicar.

C. El código funciona correctamente porque las penalizaciones severas
   deben evaluarse después de las leves dentro de un if-elif.
"""
"""
Programa: Determinar si un estudiante puede acceder a una beca.

El estudiante obtiene la beca si cumple alguna de estas condiciones:
1. Promedio >= 80 y asistencia >= 85%.
2. Pertenece a un programa de apoyo institucional y asistencia >= 75%.
"""

print("=== Evaluación de beca estudiantil ===")

# Solicitud de datos por teclado
promedio_academico = float(input("Ingrese el promedio académico (0-100): "))
porcentaje_asistencia = float(input("Ingrese el porcentaje de asistencia (0-100): "))
respuesta_apoyo = input("¿Pertenece a un programa de apoyo institucional? (si/no): ").strip().lower()

# Convertimos la respuesta a True (si pertenece) o False (no pertenece)
pertenece_programa_apoyo = respuesta_apoyo == "si" or respuesta_apoyo == "sí"

# Se evalúan las dos condiciones con los operadores lógicos and y or
if (promedio_academico >= 80 and porcentaje_asistencia >= 85) or (pertenece_programa_apoyo and porcentaje_asistencia >= 75):
    print("Felicidades, el estudiante obtiene la beca.")
else:
    print("Lo siento, el estudiante no obtiene la beca.")
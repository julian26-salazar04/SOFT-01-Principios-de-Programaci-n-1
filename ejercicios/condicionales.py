'''
Una institución organiza un evento presencial y necesita un sistema que determine si una persona puede ingresar y, en caso afirmativo, qué tipo de acceso recibirá.

Para tomar la decisión, el sistema debe conocer los siguientes datos:
    - La edad de la persona (age).
    - Si posee una entrada válida (hasValidTicket).
    - Si pertenece a la institución (belongsToInstitution).
    - La hora en la que intenta ingresar (entryHour).

La organización ha establecido las siguientes reglas:
    - Para ingresar, la persona debe tener una entrada válida.
    - Si no tiene una entrada válida, el acceso es denegado, independientemente de las demás condiciones.
    - Las personas menores de 18 años no pueden ingresar al evento.
    - Las personas de 18 años o más pueden continuar con la evaluación de las demás condiciones.
    - Si la persona pertenece a la institución y llega antes de las 18:00, recibe acceso preferencial.
    - Si pertenece a la institución pero llega a las 18:00 o después, recibe acceso general.
    - Si no pertenece a la institución, puede ingresar únicamente con acceso general.
'''
# Ejercicio: Crear las variables o constantes necesarias para solicitar los datos al usuario

# Ejercicio: Crear la estructura condicional para determinar si la persona puede ingresar y qué tipo de acceso recibirá
hasValidTicket = bool(input("¿La persona tiene una entrada válida? (True/False): "))
if hasValidTicket == True:
    age = int(input("Ingrese la edad de la persona: "))
    if age >= 18:
        belongsToInstitution = bool(input("¿La persona pertenece a la institución? (True/False): "))
        if belongsToInstitution == True:
            entryHour = int(input("Ingrese la hora en la que intenta ingresar (digite hora del 0 al 23): "))
            if entryHour < 18:
                print("Acceso preferencial: La persona puede ingresar al evento con acceso preferencial.")
            else:
                print("Acceso general: La persona puede ingresar al evento con acceso general.")
        else:
            print("Acceso general: La persona puede ingresar al evento con acceso general.")
    else:
        print("Acceso denegado: La persona es menor de edad y no puede ingresar al evento.")
else:
    print("Acceso denegado: La persona no tiene una entrada válida.")
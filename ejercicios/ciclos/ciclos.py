print("----------------- Ejemplo 1 (while): Se repite el ciclo 3")
intentos = 1    # Intentos fallidos 

while intentos <= 3:
    print("Intento", intentos)
    intentos += 1 # intentos = intentos + 1 

print("Cuenta bloqueada")


print("----------------- Ejemplo 2: Se repite el N veces, hasta que el usuario ingrese una nota entre 0 y 100")
nota = float(input("Ingrese la nota obtenida (0-100): "))

while nota < 0 or nota > 100:
    nota = float(input("Nota no válida. Ingrese la nota obtenida (0-100): "))

print("Nota válida")

print("----------------- Ejemplo 3: Se repite el N veces, hasta que el usuario ingrese la palabra salir")
quiereSalir = "no"

while quiereSalir == "no":
    respuesta = input("Ingrese una nota o ingrese la palabra 'salir' para terminar el programa: ")

    if respuesta == "salir":
        print("Saliendo del programa")
        quiereSalir = "si"

print("----------------- Ejemplo 1 (for): Se repite el ciclo 3")
for intento in range(3):
    print("Intento", intento + 1)

print("Cuenta bloqueada")

print("----------------- Ejemplo 2 (for): Se repite desde 1 hasta 5 con range(1, 6)")
for numero in range(1, 6):
    print("Número:", numero)

print("Fin del ciclo")

print("----------------- Ejemplo 3: Números pares del 0 al 10 con range(0, 11, 2)")
for par in range(0, 11, 2):
    print("Par:", par)

print("Fin de los pares")

print("----------------- Ejemplo 4: Cuenta regresiva con range(5, 0, -1)")
for numero in range(5, 0, -1):
    print(numero)

print("¡Despegue!")

print("----------------- Ejemplo 5: Recorrer un string letra por letra")
palabra = input("Ingrese una palabra para presentarla letra por letra")

for letra in palabra:
    print("Letra:", letra)

print("Fin de la palabra")

print("----------------- Ejemplo 6: Contar vocales en un string")

palabra = input("Ingrese una palabra: ")
contadorVocales = 0

for letra in palabra.lower():
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contadorVocales += 1

print("La palabra tiene", contadorVocales, "vocales")
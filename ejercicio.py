# ejercicio - agregar tres variables

print("Buenos dias!")
nombre = str(input("Cual es su nombre? "))
peso = float(input("Ingrese su peso actual: "))
estatura = input("Ingrese su estatura en metros: ")

print("A continuacion se mostrara su informacion personal:")
print("Nombre:", nombre)
print("Peso:", peso)
print("Estatura:", estatura)

op = input("Escriba 'si' si esta bien la informacion, de lo contrario escriba 'no': ")

if op == "si":
    print("Informacion correcta.")
else:
    print("Por favor, corrija su informacion.")
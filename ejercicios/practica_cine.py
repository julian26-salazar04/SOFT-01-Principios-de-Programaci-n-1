# Cine con amigos
# Pide la cantidad de entradas y luego la edad de cada una,
# aplica el descuento segun la edad y muestra el resultado final.

PRECIO_NORMAL = 3500

datos_correctos = False

while datos_correctos == False:
    cantidad = int(input("Ingrese la cantidad de entradas: "))
    print(f"\nUsted indico que desea comprar {cantidad} entrada(s).")
    respuesta = input("¿Es correcto? (si/no): ")

    if respuesta == "si" or respuesta == "SI":
        datos_correctos = True
    else:
        print("\nVolvamos a ingresar la cantidad.\n")

# --- Pedir la edad de cada entrada y calcular su precio ---
subtotal = 0
descuento_total = 0
contador = 1

while contador <= cantidad:
    edad = int(input(f"Ingrese la edad de la persona de la entrada #{contador}: "))

    if edad < 12:
        descuento_entrada = PRECIO_NORMAL * 0.20
    elif edad >= 65:
        descuento_entrada = PRECIO_NORMAL * 0.15
    else:
        descuento_entrada = 0

    subtotal = subtotal + PRECIO_NORMAL
    descuento_total = descuento_total + descuento_entrada
    contador = contador + 1

# --- Calcular el total y revisar la bebida gratis ---
total = subtotal - descuento_total

if cantidad >= 4:
    bebida_gratis = "Si"
else:
    bebida_gratis = "No"

# --- Mostrar el resultado ---
print("\n----- Resumen de la compra -----")
print(f"Subtotal: ₡{subtotal}")
print(f"Descuento aplicado: ₡{descuento_total}")
print(f"Total a pagar: ₡{total}")
print(f"¿Recibe bebida gratis?: {bebida_gratis}")
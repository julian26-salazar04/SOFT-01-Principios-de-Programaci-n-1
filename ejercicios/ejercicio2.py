# Se piden las cuatro variables del usuario.

# ---Datos de entrada---
nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio del producto unitario: "))
cantidad = int(input("Ingrese la cantidad del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento (0 si no aplica en este producto): "))

# ---Cálculo del monto total---
total = precio_unitario * cantidad
monto_descuento = total * (descuento / 100)
monto_final = total - monto_descuento

# ---Datos de salida---
print("\n--- Resumen de la compra ---")
print("Producto:", nombre_producto) 
print("Precio unitario: ", precio_unitario)
print("Cantidad comprada:", cantidad)
print("Descuento aplicado (%): ", descuento, "%")

#---Monto total y monto con descuento---
print("\nMonto total: ", total)
print("Monto con descuento: ", monto_final)

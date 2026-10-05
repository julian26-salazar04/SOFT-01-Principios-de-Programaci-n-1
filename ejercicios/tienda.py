# Codigo corregido

compra = float(input("Monto de la compra: "))
descuento = 0

if compra >= 100000:
    descuento = compra * 0.15
elif compra >= 60000:
    descuento = compra * 0.10
elif compra >= 30000:
    descuento = compra * 0.05

total = compra - descuento
print("Descuento:", descuento)
print("Total:", total)

# entrada: 20.000
# salida: 
# descuento: 0.0
# total: 20000.0

# entrada: 29.999
# salida: 
# descuento: 0
# total: 29999.0

# entrada: 30.000
# salida:
# descuento: 1500.0
# total: 28500.0

# entrada: 45.000
# salida:
# descuento: 2250.0
# total: 42750.0

# entrada: 60.000
# salida:
# descuento: 6000.0
# total: 54000.0

# entrada: 80.000
# salida:
# descuento: 8000.0
# total: 72000.0

# entrada: 100.000
# salida:
# descuento: 15000.0
# total: 85000.0

# entrada: 150.000
# salida:
# descuento: 22500.0
# total: 127500.0
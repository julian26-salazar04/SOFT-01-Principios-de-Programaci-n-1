IVA_CR = 0.13
IVA_PANAMA = 0.07

PI  = 3.14 

precioProducto = float(input("Ingrese el precio del producto: "))

totalImpuestos = precioProducto * IVA_CR

print("Debe pagar:", totalImpuestos, "de impuestos")
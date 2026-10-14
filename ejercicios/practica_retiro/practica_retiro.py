saldo = 250000
retiros_exitosos = 0
respuesta = "s"

print("Saldo inicial: ₡", saldo)

while respuesta == "s" and saldo > 0:
    monto = int(input("Monto a retirar: ₡"))

    if monto < 5000 or monto > 100000:
        print("Retiro rechazado: el monto debe estar entre ₡5000 y ₡100000.")
    elif monto > saldo:
        print("Retiro rechazado: fondos insuficientes.")
    else:
        saldo = saldo - monto
        retiros_exitosos = retiros_exitosos + 1
        print("Retiro exitoso.")

    print("Saldo actualizado: ₡", saldo)

    if saldo > 0:
        respuesta = input("¿Desea continuar retirando? (s/n): ")
        while respuesta != "s" and respuesta != "n":
            respuesta = input("Respuesta inválida. Escriba s o n: ")

print("--- Resumen final ---")
print("Saldo restante: ₡", saldo)
print("Retiros exitosos:", retiros_exitosos)
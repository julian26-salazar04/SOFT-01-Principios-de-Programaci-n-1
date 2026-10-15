# Nombre del estudiante: Julián Salazar Solis
# Contexto seleccionado: Problema 1. Cajero automático
# Descripción: permite realizar varios retiros consecutivos sobre un saldo
# inicial, valida cada monto y muestra el saldo restante y la cantidad de
# retiros exitosos al finalizar.

# --- Constantes ---
SALDO_INICIAL = 250000
RETIRO_MINIMO = 5000
RETIRO_MAXIMO = 100000

# --- Inicialización ---
saldo_actual = SALDO_INICIAL
retiros_exitosos = 0

respuesta = input("¿Desea realizar un retiro? (s/n): ")

# --- Ciclo principal ---
while respuesta == "s" and saldo_actual > 0:
    monto_retiro = int(input("Ingrese el monto a retirar (₡): "))

    if monto_retiro < RETIRO_MINIMO:
        print("Monto menor al mínimo. Retiro NO realizado")
    elif monto_retiro > RETIRO_MAXIMO:
        print("Monto mayor al máximo. Retiro NO realizado")
    elif monto_retiro > saldo_actual:
        print("Fondos insuficientes. Retiro NO realizado")
    else:
        saldo_actual = saldo_actual - monto_retiro
        retiros_exitosos = retiros_exitosos + 1
        print("Retiro realizado")

    print("Saldo:", saldo_actual)

    if saldo_actual > 0:
        respuesta = input("¿Desea realizar otro retiro? (s/n): ")
    else:
        print("Saldo agotado")

# --- Salida final ---
print("\n----------- Resumen -----------")
print("Saldo restante:", saldo_actual)
print("Retiros exitosos:", retiros_exitosos)
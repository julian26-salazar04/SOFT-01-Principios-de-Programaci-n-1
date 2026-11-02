# ============================================================
# Archivo: 04_mezcla.py
# Curso: SOFT-01 Principios de Programación 1
# Descripción: Ordenamiento por mezcla (Merge sort): divide la lista en mitades, ordena
#              cada mitad y luego las mezcla en orden.
# Ejecución: python 04_mezcla.py
# ============================================================
import random
import time

# Tamaños de lista que se usan para medir el tiempo
TAMANOS = (100, 1000, 3000)
LISTA_EJEMPLO = [5, 2, 8, 1, 9, 3]


def mezclar(izquierda, derecha, contador):
    """Une dos listas ordenadas en una sola lista ordenada."""
    resultado = []
    i = 0
    j = 0
    while i < len(izquierda) and j < len(derecha):
        contador[0] = contador[0] + 1                 # una comparación
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i = i + 1
        else:
            resultado.append(derecha[j])
            j = j + 1
        contador[1] = contador[1] + 1                 # un movimiento
    # Agregar lo que sobre de cualquiera de las dos mitades
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i = i + 1
        contador[1] = contador[1] + 1
    while j < len(derecha):
        resultado.append(derecha[j])
        j = j + 1
        contador[1] = contador[1] + 1
    return resultado


def dividir_y_mezclar(lista, contador, mostrar, nivel):
    """Función recursiva: se llama a sí misma con cada mitad."""
    if len(lista) <= 1:
        resultado = lista
    else:
        mitad = len(lista) // 2
        izquierda = dividir_y_mezclar(lista[:mitad], contador, mostrar, nivel + 1)
        derecha = dividir_y_mezclar(lista[mitad:], contador, mostrar, nivel + 1)
        resultado = mezclar(izquierda, derecha, contador)
        if mostrar:
            print("  " + "  " * nivel + f"Mezclar {izquierda} + {derecha} -> {resultado}")
    return resultado


def mezcla(lista, mostrar):
    """Ordena la lista con mezcla. Devuelve (lista, comparaciones, movimientos)."""
    contador = [0, 0]                                 # [comparaciones, movimientos]
    resultado = dividir_y_mezclar(lista, contador, mostrar, 0)
    return resultado, contador[0], contador[1]


def medir(lista):
    """Ordena una copia de la lista y devuelve (segundos, comparaciones, movimientos)."""
    copia = lista[:]                      # se ordena una copia para no alterar la original
    inicio = time.perf_counter()
    resultado, comparaciones, movimientos = mezcla(copia, False)
    fin = time.perf_counter()
    if resultado != sorted(lista):        # comprobación: el resultado debe estar ordenado
        print("¡Error! La lista no quedó ordenada.")
    return fin - inicio, comparaciones, movimientos


def main():
    print("=" * 60)
    print("ORDENAMIENTO POR MEZCLA (MERGE SORT)")
    print("=" * 60)

    # 1. Ejemplo paso a paso con una lista pequeña
    print("\nLista inicial:", LISTA_EJEMPLO)
    resultado, comparaciones, movimientos = mezcla(LISTA_EJEMPLO[:], True)
    print("Lista ordenada:", resultado)
    print("Comparaciones:", comparaciones, "| Movimientos:", movimientos)

    # 2. Medición de tiempo con listas aleatorias de distintos tamaños
    random.seed(2026)                     # misma semilla: todos obtienen las mismas listas
    print("\nTiempo con listas aleatorias:")
    print(f"{'Tamaño':>8} {'Segundos':>12} {'Comparaciones':>15} {'Movimientos':>13}")
    for tamano in TAMANOS:
        lista = [random.randint(1, 10000) for _ in range(tamano)]
        segundos, comparaciones, movimientos = medir(lista)
        print(f"{tamano:>8} {segundos:>12.5f} {comparaciones:>15} {movimientos:>13}")

    # 3. Mejor y peor caso con 1000 elementos
    print("\nCon 1000 elementos según el orden inicial:")
    casos = (("Ya ordenada", list(range(1000))),
             ("Orden inverso", list(range(1000, 0, -1))),
             ("Aleatoria", [random.randint(1, 10000) for _ in range(1000)]))
    for nombre, lista in casos:
        segundos, comparaciones, movimientos = medir(lista)
        print(f"{nombre:>14}: {segundos:.5f} s | {comparaciones} comparaciones | {movimientos} movimientos")


main()
# ============================================================
# Archivo: 02_seleccion.py
# Curso: SOFT-01 Principios de Programación 1
# Descripción: Ordenamiento por selección (Selection sort): busca el menor de la parte
#              sin ordenar y lo coloca al inicio de esa parte.
# Ejecución: python 02_seleccion.py
# ============================================================
import random
import time

# Tamaños de lista que se usan para medir el tiempo
TAMANOS = (100, 1000, 3000)
LISTA_EJEMPLO = [5, 2, 8, 1, 9, 3]


def seleccion(lista, mostrar):
    """Ordena la lista con selección. Devuelve (lista, comparaciones, movimientos)."""
    comparaciones = 0
    movimientos = 0
    n = len(lista)
    for i in range(n - 1):
        # Buscar la posición del menor entre i y el final
        pos_menor = i
        for j in range(i + 1, n):
            comparaciones = comparaciones + 1
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        # Llevar el menor a la posición i
        if pos_menor != i:
            lista[i], lista[pos_menor] = lista[pos_menor], lista[i]
            movimientos = movimientos + 1
        if mostrar:
            print(f"  Paso {i + 1}: menor = {lista[i]} -> {lista}")
    return lista, comparaciones, movimientos


def medir(lista):
    """Ordena una copia de la lista y devuelve (segundos, comparaciones, movimientos)."""
    copia = lista[:]                      # se ordena una copia para no alterar la original
    inicio = time.perf_counter()
    resultado, comparaciones, movimientos = seleccion(copia, False)
    fin = time.perf_counter()
    if resultado != sorted(lista):        # comprobación: el resultado debe estar ordenado
        print("¡Error! La lista no quedó ordenada.")
    return fin - inicio, comparaciones, movimientos


def main():
    print("=" * 60)
    print("ORDENAMIENTO POR SELECCIÓN (SELECTION SORT)")
    print("=" * 60)

    # 1. Ejemplo paso a paso con una lista pequeña
    print("\nLista inicial:", LISTA_EJEMPLO)
    resultado, comparaciones, movimientos = seleccion(LISTA_EJEMPLO[:], True)
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
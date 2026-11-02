# ============================================================
# Archivo: 03_insercion.py
# Curso: SOFT-01 Principios de Programación 1
# Descripción: Ordenamiento por inserción (Insertion sort): toma cada elemento y lo
#              inserta en su lugar dentro de la parte ya ordenada.
# Ejecución: python 03_insercion.py
# ============================================================
import random
import time

# Tamaños de lista que se usan para medir el tiempo
TAMANOS = (100, 1000, 3000)
LISTA_EJEMPLO = [5, 2, 8, 1, 9, 3]


def insercion(lista, mostrar):
    """Ordena la lista con inserción. Devuelve (lista, comparaciones, movimientos)."""
    comparaciones = 0
    movimientos = 0
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        # Correr hacia la derecha los elementos mayores que 'actual'
        seguir = True
        while j >= 0 and seguir:
            comparaciones = comparaciones + 1
            if lista[j] > actual:
                lista[j + 1] = lista[j]
                movimientos = movimientos + 1
                j = j - 1
            else:
                seguir = False
        lista[j + 1] = actual
        if mostrar:
            print(f"  Insertar {actual}: {lista}")
    return lista, comparaciones, movimientos


def medir(lista):
    """Ordena una copia de la lista y devuelve (segundos, comparaciones, movimientos)."""
    copia = lista[:]                      # se ordena una copia para no alterar la original
    inicio = time.perf_counter()
    resultado, comparaciones, movimientos = insercion(copia, False)
    fin = time.perf_counter()
    if resultado != sorted(lista):        # comprobación: el resultado debe estar ordenado
        print("¡Error! La lista no quedó ordenada.")
    return fin - inicio, comparaciones, movimientos


def main():
    print("=" * 60)
    print("ORDENAMIENTO POR INSERCIÓN (INSERTION SORT)")
    print("=" * 60)

    # 1. Ejemplo paso a paso con una lista pequeña
    print("\nLista inicial:", LISTA_EJEMPLO)
    resultado, comparaciones, movimientos = insercion(LISTA_EJEMPLO[:], True)
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
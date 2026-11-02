# ============================================================
# Archivo: 05_rapido.py
# Curso: SOFT-01 Principios de Programación 1
# Descripción: Ordenamiento rápido (Quicksort): elige un pivote, deja a la izquierda los
#              menores y a la derecha los mayores, y repite en cada parte.
# Ejecución: python 05_rapido.py
# ============================================================
import random
import time

# Tamaños de lista que se usan para medir el tiempo
TAMANOS = (100, 1000, 3000)
LISTA_EJEMPLO = [5, 2, 8, 1, 9, 3]


def particionar(lista, inicio, fin, contador):
    """Usa el elemento del medio como pivote; devuelve su posición final."""
    medio = (inicio + fin) // 2
    lista[medio], lista[fin] = lista[fin], lista[medio]   # el pivote pasa al final
    pivote = lista[fin]
    posicion = inicio
    for j in range(inicio, fin):
        contador[0] = contador[0] + 1
        if lista[j] < pivote:
            lista[posicion], lista[j] = lista[j], lista[posicion]
            contador[1] = contador[1] + 1
            posicion = posicion + 1
    lista[posicion], lista[fin] = lista[fin], lista[posicion]
    contador[1] = contador[1] + 1
    return posicion


def ordenar_parte(lista, inicio, fin, contador, mostrar):
    """Función recursiva: ordena la parte de la lista entre inicio y fin."""
    if inicio < fin:
        p = particionar(lista, inicio, fin, contador)
        if mostrar:
            print(f"  Pivote {lista[p]}: {lista[inicio:p]} < {lista[p]} < {lista[p + 1:fin + 1]}")
        ordenar_parte(lista, inicio, p - 1, contador, mostrar)
        ordenar_parte(lista, p + 1, fin, contador, mostrar)


def rapido(lista, mostrar):
    """Ordena la lista con quicksort. Devuelve (lista, comparaciones, movimientos)."""
    contador = [0, 0]                                     # [comparaciones, movimientos]
    ordenar_parte(lista, 0, len(lista) - 1, contador, mostrar)
    return lista, contador[0], contador[1]


def medir(lista):
    """Ordena una copia de la lista y devuelve (segundos, comparaciones, movimientos)."""
    copia = lista[:]                      # se ordena una copia para no alterar la original
    inicio = time.perf_counter()
    resultado, comparaciones, movimientos = rapido(copia, False)
    fin = time.perf_counter()
    if resultado != sorted(lista):        # comprobación: el resultado debe estar ordenado
        print("¡Error! La lista no quedó ordenada.")
    return fin - inicio, comparaciones, movimientos


def main():
    print("=" * 60)
    print("ORDENAMIENTO RÁPIDO (QUICKSORT)")
    print("=" * 60)

    # 1. Ejemplo paso a paso con una lista pequeña
    print("\nLista inicial:", LISTA_EJEMPLO)
    resultado, comparaciones, movimientos = rapido(LISTA_EJEMPLO[:], True)
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
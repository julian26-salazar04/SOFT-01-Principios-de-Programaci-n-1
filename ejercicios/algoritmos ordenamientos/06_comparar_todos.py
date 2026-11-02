# ============================================================
# Archivo: 06_comparar_todos.py
# Curso: SOFT-01 Principios de Programación 1
# Descripción: Compara el tiempo de los cinco algoritmos y de sorted() de Python
#              con las mismas listas aleatorias.
# Ejecución: python 06_comparar_todos.py
# ============================================================
import random
import time

# Tamaños de lista que se usan para medir el tiempo
TAMANOS = (100, 500, 1000, 2000, 3000)


# ---------- Ordenamiento Por Burbuja (Bubble Sort) ----------

def burbuja(lista, mostrar):
    """Ordena la lista con burbuja. Devuelve (lista, comparaciones, movimientos)."""
    comparaciones = 0
    movimientos = 0
    n = len(lista)
    hubo_intercambio = True
    pasada = 0
    # Se repite mientras en la pasada anterior haya habido algún intercambio
    while hubo_intercambio:
        hubo_intercambio = False
        pasada = pasada + 1
        for j in range(n - pasada):
            comparaciones = comparaciones + 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                movimientos = movimientos + 1
                hubo_intercambio = True
        if mostrar:
            print(f"  Pasada {pasada}: {lista}")
    return lista, comparaciones, movimientos

# ---------- Ordenamiento Por Selección (Selection Sort) ----------

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

# ---------- Ordenamiento Por Inserción (Insertion Sort) ----------

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

# ---------- Ordenamiento Por Mezcla (Merge Sort) ----------

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

# ---------- Ordenamiento Rápido (Quicksort) ----------

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


def ordenar_con_sorted(lista, mostrar):
    """Referencia: sorted() usa Timsort, un algoritmo optimizado (mezcla + inserción)."""
    return sorted(lista), 0, 0


ALGORITMOS = (("Burbuja", burbuja), ("Selección", seleccion), ("Inserción", insercion),
              ("Mezcla", mezcla), ("Rápido", rapido), ("sorted()", ordenar_con_sorted))


def main():
    print("=" * 72)
    print("COMPARACIÓN DE ALGORITMOS DE ORDENAMIENTO (tiempo en segundos)")
    print("=" * 72)
    random.seed(2026)
    listas = {}
    for tamano in TAMANOS:
        listas[tamano] = [random.randint(1, 10000) for _ in range(tamano)]

    encabezado = f"{'Algoritmo':<11}"
    for tamano in TAMANOS:
        encabezado = encabezado + f"{'n = ' + str(tamano):>12}"
    print(encabezado)
    print("-" * len(encabezado))

    tiempos_3000 = {}
    for nombre, funcion in ALGORITMOS:
        fila = f"{nombre:<11}"
        for tamano in TAMANOS:
            copia = listas[tamano][:]
            inicio = time.perf_counter()
            resultado = funcion(copia, False)[0]
            segundos = time.perf_counter() - inicio
            if resultado != sorted(listas[tamano]):
                print("¡Error!", nombre, "no ordenó la lista.")
            fila = fila + f"{segundos:>12.5f}"
            tiempos_3000[nombre] = segundos
        print(fila)

    # Cuántas veces más lento que el más rápido de los cinco (con el tamaño mayor)
    mayor = TAMANOS[-1]
    mas_rapido = tiempos_3000["Rápido"]
    if tiempos_3000["Mezcla"] < mas_rapido:
        mas_rapido = tiempos_3000["Mezcla"]
    print(f"\nCon n = {mayor}, cuántas veces más tiempo que el más rápido de los cinco:")
    for nombre, funcion in ALGORITMOS[:5]:
        veces = tiempos_3000[nombre] / mas_rapido
        barra = "#" * min(60, int(veces))
        print(f"{nombre:<11}{veces:>8.1f} veces  {barra}")
    print("\nNota: los tiempos cambian según la computadora; compare las proporciones, no los valores exactos.")


main()
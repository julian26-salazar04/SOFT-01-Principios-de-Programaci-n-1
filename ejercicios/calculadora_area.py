PI = 3.1416
OPCION_SALIR = 4


def mostrar_encabezado():
    print("=" * 30)
    print("CALCULADORA DE ÁREAS")
    print("=" * 30)


def mostrar_menu():
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Círculo")
    print("4. Salir")


def calcular_area_rectangulo():
    base = float(input("Digite la base: "))
    altura = float(input("Digite la altura: "))
    area = base * altura
    print(f"Área del rectángulo: {area}")


def calcular_area_triangulo():
    base = float(input("Digite la base: "))
    altura = float(input("Digite la altura: "))
    area = base * altura / 2
    print(f"Área del triángulo: {area}")


def calcular_area_circulo():
    radio = float(input("Digite el radio: "))
    area = PI * radio * radio
    print(f"Área del círculo: {round(area, 2)}")


def main():
    mostrar_encabezado()
    opcion = 0
    while opcion != OPCION_SALIR:
        mostrar_menu()
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            calcular_area_rectangulo()
        elif opcion == 2:
            calcular_area_triangulo()
        elif opcion == 3:
            calcular_area_circulo()
        elif opcion != OPCION_SALIR:
            print("Opción no válida.")
    print("Gracias por usar la calculadora.")


main()
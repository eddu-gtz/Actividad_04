from figuras import Figuras

f = Figuras()

while True:
    print("1. Cálcular área de una figura")
    print("2. Conocer mi signo zodiacal")
    print("3. Cálculo del Número e")
    print("0. Salir")
    op = input("opcion: ")

    if op == "1":
        print("1. Calcular area de un cuadrado")
        print("2. Calcular area de un triangulo")
        print("3. Calcular area de un circulo")

        op = input("opcion: ")

        if op == "1":
            lado = int(input("Ingresa el lado: "))
            f.areaCuadrado(lado)
            f.imprimirArea()

        elif op == "2":
            base = int(input("Ingresa la base: "))
            altura = int(input("Ingresa la altura: "))
            f.areaTriangulo(base, altura)
            f.imprimirArea()

        elif op == "3":
            radio = int(input("Ingresa el radio: "))
            f.areaCirculo(radio)
            f.imprimirArea()

    elif op == "2":
        pass
    elif op == "3":
        pass
    elif op == "0":
        break
from figuras import Figuras
from zodiaco import Zodiaco
from numeroe import Numeroe

f = Figuras()

while True:
    print("\n\n1. Cálcular EL área de una figura")
    print("2. Conocer mi signo zodiacal")
    print("3. Cálculo del Número e")
    print("0. Salir")
    op = input("opcion: ")

    #Area de un cuadrado
    if op == "1":
        print("\n\n1. Area de un cuadrado")
        print("2. Area de un triangulo")
        print("3. Area de un circulo")

        op = input("opcion: ")
        print("\n")
        if op == "1":
            lado = int(input("Ingresa el lado: "))
            f.areaCuadrado(lado)

        elif op == "2":
            base = int(input("Ingresa la base: "))
            altura = int(input("Ingresa la altura: "))
            f.areaTriangulo(base, altura)

        elif op == "3":
            radio = int(input("Ingresa el radio: "))
            f.areaCirculo(radio)

        f.imprimirArea()
        
    #Signo zodiacal
    elif op == "2":
        print("\n")
        dia = int(input("Ingresa tu dia de nacimiento: "))
        mes = int(input("Ingresa tu mes de nacimiento: "))
        
        z = Zodiaco(dia, mes)

        print("\n")
        z.calcularZodiaco()

    elif op == "3":

        limite = int(input("\nIngresa el limite de ciclos: "))

        e = Numeroe(limite)

        print("\nEl numero e con un limite de ", limite, " es: ", e.calcularE())

    elif op == "0":
        break
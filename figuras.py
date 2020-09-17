class Figuras:
    def __init__(self):
        self.__area = 0

    def areaCuadrado(self, lado):
        self.__area = lado * lado

    def areaTriangulo(self, b, h):
        self.__area = ( b * h ) / 2

    def areaCirculo(self, radio):
        self.__area = (3.1416) * (radio ** 2)

    def imprimirArea(self):
        print("\nEl area de la figura es: ", self.__area)


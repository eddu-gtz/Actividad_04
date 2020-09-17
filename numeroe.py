class Numeroe:
    def __init__(self, limite):
        self.__limite = limite

    def factorial(self, n):
        fact = n

        if n == 0:
            return 1
        else:
            #Ciclo For en rango de 1 hasta n-1
            for x in range(1, n):
                fact = fact * x
        return fact

    def calcularE(self):
        n = 0
        e = 0
        while n < self.__limite:
            e += 1 / self.factorial(n)
            n = n + 1
            
        return e
    
    
    
            


    
    
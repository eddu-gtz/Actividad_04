class Zodiaco:
    def __init__(self, dia, mes):
        self.__dia = dia
        self.__mes = mes

    def calcularZodiaco(self):
        #Enero
        if self.__mes == 1:
            if self.__dia >= 1 and self.__dia <= 20:
                print("Tu signo zodiacal es Capricornio")#Capricornio
            elif self.__dia >= 21 and self.__dia <= 30:
                print("Tu signo zodiacal es Acuario")#Acuario

        #Febrero  
        elif self.__mes == 2:
            if self.__dia >= 1 and self.__dia <= 19:
                print("Tu signo zodiacal es Acuario")#Acuario
            elif self.__dia >= 20 and self.__dia <= 28:
                print("Tu signo zodiacal es Picis")#Picis

        #Marzo   
        elif self.__mes == 3:
            if self.__dia >= 1 and self.__dia <= 20:
                print("Tu signo zodiacal es Picis")#Picis
            elif self.__dia >= 21 and self.__dia <= 31:
                print("Tu signo zodiacal es Aries")#Aries

        #Abril   
        elif self.__mes == 4:
            if self.__dia >= 1 and self.__dia <= 20:
                print("Tu signo zodiacal es Aries")#Aries
            elif self.__dia >= 21 and self.__dia <= 30:
                print("Tu signo zodiacal es Tauro")#Tauro

        #Mayo 
        elif self.__mes == 5:
            if self.__dia >= 1 and self.__dia <= 21:
                print("Tu signo zodiacal es Tauro")#Tauro
            elif self.__dia >= 22 and self.__dia <= 31:
                print("Tu signo zodiacal es Geminis")#Geminis

        #Junio
        elif self.__mes == 6:
            if self.__dia >= 1 and self.__dia <= 21:
                print("Tu signo zodiacal es Geminis")#Geminis
            elif self.__dia >= 22 and self.__dia <= 30:
                print("Tu signo zodiacal es Cancer")#Cancer

        #Julio
        elif self.__mes == 7:
            if self.__dia >= 1 and self.__dia <= 22:
                print("Tu signo zodiacal es Cancer")#Cancer
            elif self.__dia >= 23 and self.__dia <= 31:
                print("Tu signo zodiacal es Leo")#Leo

        #Agosto   
        elif self.__mes == 8:
            if self.__dia >= 1 and self.__dia <= 23:
                print("Tu signo zodiacal es Leo")#Leo
            elif self.__dia >= 24 and self.__dia <= 31:
                print("Tu signo zodiacal es Virgo")#Virgo

        #Septiembre   
        elif self.__mes == 9:
            if self.__dia >= 1 and self.__dia <= 22:
                print("Tu signo zodiacal es Virgo")#Virgo
            elif self.__dia >= 23 and self.__dia <= 30:
                print("Tu signo zodiacal es Libra")#Libra

        #Octubre
        elif self.__mes == 10:
            if self.__dia >= 1 and self.__dia <= 22:
                print("Tu signo zodiacal es Libra")#Libra
            elif self.__dia >= 23 and self.__dia <= 30:
                print("Tu signo zodiacal es Escorpion")#Escorpion
        
        #Noviembre       
        elif self.__mes == 11:
            if self.__dia >= 1 and self.__dia <= 21:
                print("Tu signo zodiacal es Escorpion")#Escorpion
            elif self.__dia >= 22 and self.__dia <= 31:
                print("Tu signo zodiacal es Sagitario")#Sagitario

        #DICIEMBRE
        elif self.__mes == 12:
            if self.__dia >= 1 and self.__dia <= 21:
                print("Tu signo zodiacal es Sagitario")#Sagitario
            elif self.__dia >= 22 and self.__dia <= 31:
                print("Tu signo zodiacal es Capricornio")#Capricornio


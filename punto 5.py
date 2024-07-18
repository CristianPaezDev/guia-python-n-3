# Escribir un programa que calcule la longitud y el área de una circunferencia: Radio = 4
# Longitud de la circunferencia = 2 * PI * radio
# Área de la circunferencia = PI * radio˄2

import math
class calcular:
    def __init__(self, radio) :
        self.radio = radio
        self.longitud = 2 * math.pi * self.radio
        self.area = math.pi * (self.radio ** 2)

    def calcular_longitud(self):
        return self.longitud
    
    def calcular_area(self):
        return self.area
    
def main():
    print("Programa para calcular la longitud y el área de una circunferencia")
    radio = float(input("Ingrese el radio de la circunferencia: "))
    circ = calcular(radio)
    print("Longitud de la circunferencia:", circ.calcular_longitud())
    print("Área de la circunferencia:", circ.calcular_area())

if __name__ == "__main__":
    main()
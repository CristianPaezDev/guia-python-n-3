# Escribir un programa que calcule el volumen de una esfera:
# Radio = 3 volumen de la esfera = 4/3 * PI * radio˄3

import math

class calcular:
    def __init__(self, radio):
        self.radio = radio
        self.volumen = self.calcula_volumen()
    
    def calcula_volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)
    
    def imprimir_volumen(self):
        print(f"El volumen de la esfera es: {self.volumen}")
    
def main():
    radio = float(input("Ingrese el radio de la esfera: "))
    calculo = calcular(radio)
    calculo.imprimir_volumen()

if __name__ == "__main__":
    main()


# Escribir un programa que calcule el área de un triángulo:
# Base = 7 altura = 4 área del triángulo = (base * altura)/2

class calcular():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = (self.base * self.altura) / 2

        print("El área del triángulo es: ", self.area)

def main():
    print("Programa para calcular el área de un triángulo")
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    triangulo = calcular(base, altura)
    triangulo.area

if __name__ == "__main__":
    main()
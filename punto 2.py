# 2. Escribir un programa que calcule el área de un rectángulo:
# lado1 = 3 lado2 = 4 área del rectángulo= lado1 * lado2

class rectangulo:
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.area = self.lado1 * self.lado2

def main():
    lado1 = float(input("Ingrese el lado 1 del rectángulo: "))
    lado2 = float(input("Ingrese el lado 2 del rectángulo: "))

    rectangulo1 = rectangulo(lado1, lado2)
    print("Area del rectangulo:", rectangulo1.area)

main()

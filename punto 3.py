# Un programa que lea 4 números y calcule la media.
# Media= (num1 + num2 + num3 + num4)/4

class media:
    def __init__(self, num1, num2, num3, num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
    
    def calcular_media(self):
        return (self.num1 + self.num2 + self.num3 + self.num4) / 4
    
    def imprimir_media(self):
        print("La media de los números es: ", self.calcular_media())

def main():
    print("Programa para calcular la media de 4 números")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    num4 = float(input("Ingrese el cuarto número: "))
    
    media_obj = media(num1, num2, num3, num4)
    
    media_obj.imprimir_media()

if __name__ == "__main__":
    main()

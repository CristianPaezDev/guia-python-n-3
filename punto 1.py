# 1. Escribir un programa que sume, reste, multiplique y divida dos números

class calcular():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: No se puede dividir por 0"
        
def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    calculo = calcular(num1, num2)
    
    print("Suma:", calculo.suma())
    print("Resta:", calculo.resta())
    print("Multiplicación:", calculo.multiplicacion())
    print("División:", calculo.division())

if __name__ == "__main__":
    main()
# Escribir un programa que calcule la velocidad de un proyectil que recorre 2 Km en 5 minutos. Expresar
# el resultado en metros/segundo. Velocidad = espacio/tiempo.

class calcular:
    def __init__(self, km, min):
        self.km = km
        self.min = min
        self.velocidad = self.calcular_velocidad()

    def calcular_velocidad(self):
        metros = self.km * 1000
        segundos = self.min * 60
        return metros / segundos
    
    def mostrar_velocidad(self):
        return f"La velocidad del proyectil es {self.velocidad:.2f} m/s"

def main():
    km = 2
    min = 5
    calculo = calcular(km, min)
    print(calculo.mostrar_velocidad())

if __name__ == "__main__":
    main()



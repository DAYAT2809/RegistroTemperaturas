# Crear una matriz 3D para almacenar datos de temperaturas
import random

def generar_temperaturas(ciudades, dias, semanas):
    """Genera una matriz 3D con temperaturas aleatorias entre 10 y 30 grados Celsius."""
    return [[[random.randint(25, 36) for _ in dias] for _ in range(semanas)] for _ in ciudades]

def calcular_promedios(temperaturas, ciudades, dias, semanas):
    """Calcula y muestra el promedio de temperaturas por ciudad y semana."""
    for i, ciudad in enumerate(ciudades):
        print(f"Ciudad: {ciudad}")
        for j in range(semanas):
            suma = sum(temperaturas[i][j])
            promedio = suma / len(dias)
            print(f"  Semana {j+1}: Promedio de temperatura = {promedio:.2f}°C")
        print("-")

def main():
    ciudades = ["Quito", "Guayaquil", "Cuenca"]
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    semanas = 5

    temperaturas = generar_temperaturas(ciudades, dias, semanas)
    calcular_promedios(temperaturas, ciudades, dias, semanas)

if __name__ == "__main__":
    main()

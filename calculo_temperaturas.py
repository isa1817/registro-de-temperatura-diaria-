import random

def generar_temperaturas(ciudades, semanas, dias_semana):
    """
    Genera una matriz tridimensional con temperaturas aleatorias
    """
    return [[[random.randint(15, 30) for _ in range(len(dias_semana))] 
             for _ in range(semanas)] for _ in range(len(ciudades))]

def calcular_temperaturas_promedio(temperaturas, ciudades, semanas, dias_semana):
    """
    Calcula y muestra el promedio de temperaturas por ciudad y semana
    """
    for i, ciudad in enumerate(ciudades):
        for semana in range(semanas):
            suma_temperaturas = sum(temperaturas[i][semana])  # Suma de temperaturas de la semana
            promedio = suma_temperaturas / len(dias_semana)  # Cálculo del promedio
            print(f"Promedio de temperaturas en {ciudad} para la Semana {semana + 1}: {promedio:.2f}°C")

# Definimos los parámetros
temperaturas = generar_temperaturas(["Ciudad A", "Ciudad B", "Ciudad C"], 4, 
                                     ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])

# Llamamos a la función para calcular y mostrar los promedios
calcular_temperaturas_promedio(temperaturas, ["Ciudad A", "Ciudad B", "Ciudad C"], 4, 
                               ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])

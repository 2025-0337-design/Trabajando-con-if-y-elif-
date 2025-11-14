# ejercicio 12 Pide una muestra de números separados por comas
# Muestra la media y la desviación típica (poblacional)

import math

entrada = input("Introduce números separados por comas: ")

numeros = [float(n) for n in entrada.split(",")]

media = sum(numeros) / len(numeros)

suma_cuadrados = 0
for n in numeros:
    suma_cuadrados += (n - media) ** 2

desviacion = math.sqrt(suma_cuadrados / len(numeros))

print("\nResultados:")
print("Media:", media)
print("Desviación típica:", desviacion)

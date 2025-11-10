# ejercicio 12 Pide una muestra de números separados por comas
# Muestra la media y la desviación típica (poblacional)

import math

entrada = input("Introduce números separados por comas (ej: 1,2,3,4): ")

partes = entrada.split(",")
numeros = []

for p in partes:
    p = p.strip()
    if p != "":
        numeros.append(float(p))

if len(numeros) == 0:
    print("No se introdujeron números válidos.")
else:
    
    suma = 0
    for x in numeros:
        suma = suma + x
    media = suma / len(numeros)

    # calcular varianza (poblacional): media de (x - media)^2
    suma_cuadrados = 0
    for x in numeros:
        suma_cuadrados = suma_cuadrados + (x - media) ** 2
    varianza = suma_cuadrados / len(numeros)

    desviacion = math.sqrt(varianza)

    print("Números:", numeros)
    print("Media:", media)
    print("Desviación típica (poblacional):", desviacion)

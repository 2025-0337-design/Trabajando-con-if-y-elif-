# ejercicio 4 Programa que guarda los números ganadores de la lotería

numeros = []

print("Introduce los números ganadores de la lotería (6 en total).")

for i in range(6):
    num = int(input("Número " + str(i + 1) + ": "))
    numeros.append(num)


numeros.sort()

# Mostramos los números ordenados
print("\nLos números ganadores ordenados son:")
print(numeros)

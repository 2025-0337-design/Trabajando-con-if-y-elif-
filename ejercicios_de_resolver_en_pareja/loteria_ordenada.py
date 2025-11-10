# ejercicio 4 Programa que guarda los números ganadores de la lotería

# Lista vacía para guardar los números
numeros = []

print("Introduce los números ganadores de la lotería (6 en total).")

# Pedimos los números uno por uno
for i in range(6):
    num = int(input("Número " + str(i + 1) + ": "))
    numeros.append(num)

# Ordenamos la lista de menor a mayor
numeros.sort()

# Mostramos los números ordenados
print("\nLos números ganadores ordenados son:")
print(numeros)

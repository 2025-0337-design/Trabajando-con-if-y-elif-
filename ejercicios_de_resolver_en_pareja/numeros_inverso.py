# ejercicio 5 Programa que muestra los números del 1 al 10 en orden inverso

# lista con los números del 1 al 10
numeros = [1,2,3,4,5,6,7,8,9,10]

print("Números del 10 al 1:")

# Recorremos la lista desde el final al principio
for i in range(len(numeros)-1, -1, -1):
    if i != 0:
        print(numeros[i], end=", ")
    else:
        print(numeros[i])

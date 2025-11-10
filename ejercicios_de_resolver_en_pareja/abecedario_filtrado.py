# Ejercicio 7 - Abecedario y eliminación de posiciones múltiplos de 3
# (Se considera la primera posición como 1: se eliminan 3, 6, 9, ...)

# Creamos la lista con el abecedario en minúsculas
abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
              "n","o","p","q","r","s","t","u","v","w","x","y","z"]

print("Abecedario original:")
print(abecedario)

# Lista donde guardaremos las letras que quedan
resultado = []

for i in range(len(abecedario)):
    posicion_humana = i + 1  
    # si la posición es múltiplo de 3, la saltamos (no se añade)
    if posicion_humana % 3 == 0:
 
        continue

    resultado.append(abecedario[i])

print("\nAbecedario después de eliminar posiciones múltiplos de 3:")
print(resultado)

# ejercicio 8 Programa para saber si una palabra es palíndromo

palabra = input("Escribe una palabra: ")

# Convertimos todo a minúsculas para evitar errores por mayúsculas
palabra = palabra.lower()

# Invertimos la palabra
invertida = palabra[::-1]

if palabra == invertida:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")

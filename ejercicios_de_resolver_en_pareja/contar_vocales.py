# ejercicio 9 Pide una palabra y muestra cuántas veces aparece cada vocal

palabra = input("Escribe una palabra: ")
palabra = palabra.lower()

a = palabra.count("a")
e = palabra.count("e")
i = palabra.count("i")
o = palabra.count("o")
u = palabra.count("u")

print("Cantidad de vocales en la palabra:")
print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)

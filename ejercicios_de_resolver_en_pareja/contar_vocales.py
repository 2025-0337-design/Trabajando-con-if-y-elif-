# ejercicio 9 Pide una palabra y muestra cuántas veces aparece cada vocal

palabra = input("Escribe una palabra: ")
vocal = palabra.lower()

a = vocal.count("a")
e = vocal.count("e")
i = vocal.count("i")
o = vocal.count("o")
u = vocal.count("u")

print("Cantidad de vocales en la palabra:")
print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)

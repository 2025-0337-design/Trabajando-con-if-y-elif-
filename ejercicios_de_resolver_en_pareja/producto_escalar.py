# ejercicio 11 Calcula el producto escalar entre dos vectores dados

v1 = [1, 2, 3]
v2 = [-1, 0, 2]


if len(v1) != len(v2):
    print("Los vectores no tienen la misma dimensión.")
else:
    producto = 0
    
    for i in range(len(v1)):
        producto = producto + (v1[i] * v2[i])

    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("El producto escalar es:", producto)

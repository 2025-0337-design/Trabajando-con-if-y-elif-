#ejercicio 3 Programa que pide las notas de cada asignatura

# Lista con las asignaturas del curso
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Lista vacía para guardarlas
notas = []

# se piden las notas una por una
for materia in asignaturas:
    nota = input("¿Qué nota sacaste en " + materia + "? ")
    notas.append(nota)

# Mostramos los resultados
print("\nResultados finales:\n")
for i in range(len(asignaturas)):
    print("En", asignaturas[i], "has sacado", notas[i])

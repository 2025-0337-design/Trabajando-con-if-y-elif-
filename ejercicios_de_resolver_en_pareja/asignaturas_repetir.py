# ejercicio 6 Programa que muestra las asignaturas que se deben repetir

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
repetir = []

for materia in asignaturas:
    while True:
        entrada = input("¿Qué nota sacaste en " + materia + " (0-10)? ")
        # intentamos convertir a número
        try:
            nota = float(entrada)
        except ValueError:
            print("Entrada inválida. Escribe un número (por ejemplo 7.5).")
            continue

        if nota < 0 or nota > 10:
            print("La nota debe estar entre 0 y 10. Intenta de nuevo.")
            continue

        break

    if nota < 5:
        repetir.append(materia)

# Mostrar resultado
print("\nDebes repetir las siguientes asignaturas:")
if len(repetir) == 0:
    print("¡Felicidades! No tienes que repetir ninguna.")
else:
    for materia in repetir:
        print("-", materia)

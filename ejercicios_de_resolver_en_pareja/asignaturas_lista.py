# ejercicio 1 Programa para guardar asignaturas y agregar más

# Lista de asignaturas basicas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

print("Las asignaturas actuales son:")
print(asignaturas)

# Agregar nuevas asignaturas
while True:
    nueva_asignatura = input("Escribe una nueva asignatura (o deja vacío para terminar): ")

    if nueva_asignatura == "":
        break

    asignaturas.append(nueva_asignatura)
    print("Asignatura agregada correctamente.")

# Mostrar todas las asignaturas al final
print("\nLa lista final de asignaturas es:")
for materia in asignaturas:
    print("-", materia)

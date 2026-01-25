estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

#recorre las lineas simultaneamente y ponle un indice
for n,(nombre, mat, fis, qui) in enumerate(zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica),start = 1):
    print(n,(nombre, mat, fis, qui))

#media de las notas
    media = (mat + fis + qui) / 3

    if media >= 6.5 :
        print("Estudiante esta aprobado")
    elif media >= 5 :
        print("Estudiante en recuperacion")
    else:
        print("Estudiante esta suspenso")


    print(f"{n} {nombre} - Matemáticas: {mat}, "
          f"Física: {fis}, "
          f"Química: {qui}, "
          f"Promedio: {round(media, 2)}, "
          f"Estado: {estado}")

# Listas de estudiantes y sus notas
estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

# Recorrer las listas simultáneamente con zip y enumerate
for idx, (nombre, mat, fis, qui) in enumerate(
        zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica), start=1):

    # Calcular media
    media = (mat + fis + qui) / 3

    # Determinamos la nota con un if
    if media >= 6.5:
        estado = "Aprobado"
    elif media >= 5:
        estado = "En recuperación"
    else:
        estado = "Suspenso"

    # Mostramos el reporte
    print(f"{idx} {nombre} - Matemáticas: {mat}, "
          f"Física: {fis}, "
          f"Química: {qui}, "
          f"Promedio: {round(media, 2)}, "
          f"Estado: {estado}")

# Las listas de los estudiantes y sus notas
estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

# Diccionario vacío para almacenar el resultado final
resultado_final = {}

# Juntamos las listas con un zip y los mostramos en pantalla mostrando un for
for nombre, mat, fis, qui in zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica):

    # Calcular media
    media = (mat + fis + qui) / 3

    # Determinamos la nota con un if
    if media >= 6.5:
        estado = "Aprobado"
    elif media >= 5:
        estado = "En recuperación"
    else:
        estado = "Suspenso"

    # Guardar la información en el diccionario anidado
    resultado_final[nombre] = {
        "Matemáticas": mat,
        "Física": fis,
        "Química": qui,
        "Promedio": round(media, 2),  # redondeamos a 2 decimales
        "Estado": estado
    }

# Imprimimos los resultados
for nombre, info in resultado_final.items():
    print(f"{nombre} - Matemáticas: {info['Matemáticas']}, "
          f"Física: {info['Física']}, "
          f"Química: {info['Química']}, "
          f"Promedio: {info['Promedio']}, "
          f"Estado: {info['Estado']}")
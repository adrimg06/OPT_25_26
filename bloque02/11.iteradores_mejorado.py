# Diccionario con estudiantes y sus notas
estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [7, 6, 8],
    "Marta": [9, 10, 9],
    "Carlos": [6, 7, 5],
    "Laura": [10, 9, 10]
}

# Creamos un iterador sobre las claves del diccionario
iter_estudiantes = iter(estudiantes)

# Recorremos el iterador usando while True y next()
while True:
    try:
        nombre = next(iter_estudiantes)
        notas = estudiantes[nombre]
        media = sum(notas) / len(notas)

        # Determinamos la nota con un if
        if media >= 6.5:
            estado = "Aprobado"
        elif media >= 5:
            estado = "En recuperación"
        else:
            estado = "Suspenso"

        # Imprimimos por pantalla
        print(f"{nombre} - Notas: {notas}, Promedio: {round(media, 2)}, Estado: {estado}")

    # Utilizamos el stop interaction para parar el bucle cuando no haya más elementos:
    except StopIteration:
        break

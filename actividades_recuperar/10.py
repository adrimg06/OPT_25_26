estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [7, 6, 8],
    "Marta": [9, 10, 9],
    "Carlos": [6, 7, 5],
    "Laura": [10, 9, 10]
}
#Crea un iterador sobre las claves del diccionario.
iter_estudiantes = iter(estudiantes)

#Recorre el iterador usando next()dentro de un while True
while True:
    nombre = next(iter_estudiantes)
    notas= estudiantes[nombre]
    media = sum(notas) / len(notas)

    if media > 6.5:
        estado = ("aprobado")
    elif media >= 5.0:
        estado = ("recuperacion")
    else:
        estado = ("suspenso")

    print(f"{nombre} - Notas: {notas}, Promedio: {round(media, 2)}, Estado: {estado}")

    # Utilizamos el stop interaction para parar el bucle cuando no haya más elementos:
    
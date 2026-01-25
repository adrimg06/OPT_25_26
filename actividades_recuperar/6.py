from actividades_recuperar.zip_avan import resultado_final

estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

#crear un diccionario vacío llamado resultado_final
resultado_final = {}

# usar zip() para recorrer todas las listas al mismo tiempo y calcular
for nom, mat, fis , qui in zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica):

#nota media
    media = (mat + fis + qui) / 3

    if media >= 6.5:
        print("El estudiante esta aprobado")
    elif media <= 5 and media > 6.5:
        print("El estudiante esta en recuperación")
    else:
        print("el estudiante esta no aprobado")

 # Guardar la información en el diccionario anidado

estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

#crea un diccionario
resultado_final = {}

#promedio de cada estudiante, primero juntaremos todas las listas
for nom, mat, fis, qui in zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica):

#nota media
    nota_media = (mat + fis + qui) / 3

#aprobado, recuperacion, reprobado

if nota_media >= 6.5:
    print(f"El estudiante esta aprobado")
elif nota_media >= 5 <= 6.5 :
    print(f"El estudiante esta aprobado")
else:
    print(f"El estudiante esta aprobado")


resultado_final[nom] = {
    "nombre:": nom,
    "matematicas": mat,
    "fisica": fis,
    "quimica": qui,
}



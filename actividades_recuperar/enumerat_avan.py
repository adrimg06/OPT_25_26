estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

#Recorre las listas simultáneamente usando enumerate()y zip().
for n, (nom, mat, fis, qui) in enumerate(zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica), start=1):
    print(n, nom, mat, fis, qui)
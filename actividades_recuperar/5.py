nombres = ["Ana", "Luis", "Marta"]
notas_matematicas = [8, 7, 9]
notas_fisica = [9, 6, 10]

#usamos zip() 3 listas para comprimirlas:
for nom, mat, fis in zip(nombres,notas_matematicas,notas_fisica):
    print(nom, mat, fis)
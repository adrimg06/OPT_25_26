nombres = ["Ana", "Luis", "Marta"]
notas_matematicas = [8, 7, 9]
notas_fisica = [9, 6, 10]

# Utilizamos el for para mostrarlo en pantalla
for nombre, mat, fis in zip(nombres, notas_matematicas, notas_fisica):
    print(f"{nombre} - Matemáticas: {mat}, Física: {fis}")

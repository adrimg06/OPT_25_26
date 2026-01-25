#crea 3 listas
nombres = ["Ana", "Luis", "Marta"]
notas_matematicas = [8, 7, 9]
notas_fisica = [9, 6, 10]

#Unelas con un zip
for nombres , notas_matematicas , notas_fisica in zip(nombres, notas_matematicas, notas_fisica):
    print(nombres, notas_matematicas, notas_fisica)
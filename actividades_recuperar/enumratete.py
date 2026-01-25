nombres = ["Ana", "Luis", "Marta", "Carlos"]

#Registre la lista usando enumerate()y muestre el índice y el nombre.
for indice, nombre in enumerate(nombres, start=1):
    print(indice,nombre)
#Convierte el resultado en lista de tuplas y muéstralo.
tupas = tuple(nombres)
print("Lista convertida en tupla")
print(tupas)
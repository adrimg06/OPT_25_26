def mostrar_indices(nombres):
    for indice, nombre in enumerate(nombres):
        print(indice, nombre)


nombres = ["Ana", "Luis", "Marta", "Carlos"]

# Mostramos el índice y nombre
mostrar_indices(nombres)

# Convertimos las tupas en listas y las mostramos en pantalla
tuplas = list(enumerate(nombres))
print(tuplas)

# Ponemos el diccionario vació
compras = []

# Repetimos el valor 5 veces
for i in range(5):
    producto = input(f"Introduce el producto {i + 1}: ")
    compras.append(producto)

# Hacemos un print para mostrar la lista de la compra con los elementos introducidos
print("\nLista completa de compras:")
print(compras)

# Creamos una variable para eliminar un producto
producto_eliminar = input("\nIntroduce un producto para eliminar: ")

# Comprobamos que la variable anterior esté en la lista
if producto_eliminar in compras:
    compras.remove(producto_eliminar)
else:
    print("Ese producto no estaba en la lista.")

# Hacemos un sort para ordenar alfabéticamente
compras.sort()

# Hacemos un print para mostrar la lista
print("\nLista ordenada:")
print(compras)

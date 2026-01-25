#Defina una lista vacía compras.
compras = []
#Pida al usuario 5 productos y los añada a la lista con append().
for i in range(5):
    producto = input("Ingrese producto: ")
    compras.append(producto)
#Muestre la lista completa.
print(compras)
#Pida al usuario un producto a eliminar y lo quite con remove().
producto_eliminar = input("Ingrese producto: ")

if producto_eliminar in compras:
    compras.remove(producto_eliminar)
    print(compras)

#Muestre la lista ordenada alfabéticamente con sort().
compras.sort()
#Incluya un docstring explicando qué hace el programa.
print("lista ordenada:")
print(compras)
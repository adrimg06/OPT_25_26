compras = []

for i in range(5):
    producto= input("ingrese unos productos:")
    compras.append(producto)
print("lista virgen")
print(compras)

compras.remove(compras[3])
print("lista ordenada")
print(compras)

compras.sort()
print("lista ordenada")
print(compras)


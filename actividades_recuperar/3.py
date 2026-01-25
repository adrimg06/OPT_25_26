agenda = {}

for n in range(3):
    nombre = input("Ingrese nombre: ")
    telefono = input("Ingrese telefono: ")
    agenda[nombre] = telefono

print("agenda completa")
for nombre, telefono in agenda.items():
    print(nombre,":", telefono)

buscar = input("Ingrese nombre: ")
if buscar in agenda:
    print(agenda[buscar])
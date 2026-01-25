#crea un diccionario vacío llamado agenda.
agenda = {}
#Pide al usuario que introduzca 3 contactos ( nombre y teléfono ).
for i in range(3):
    nombre = input(f"Introduce nombre del contacto {i + 1}: ")
    telefono = input(f"Introduce teléfono de {nombre}: ")
    agenda[nombre] = telefono
#El nombre será la clave .

#El teléfono será el valor .
#Muestra la agenda completa usando un bucle.
print("\n Agenda completa:")
for nombre, telefono in agenda.items():
    print(f"{nombre} : {telefono}")
#Permite al usuario buscar un contacto por nombre:
buscar = input("ingrese nombre del contacto que quiere buscar")
if buscar in agenda:
    print("Telefono:", agenda[buscar])
else:
    print("contacto no encontrado")
#Si existe, muestra el teléfono.
#Si no existe, muestra "Contacto no encontrado" .
#Agregue una cadena de documentos explicando qué hace el programa.


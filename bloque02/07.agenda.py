# creamos un diccionario vacío
agenda = {}

# Pedimos 3 contactos por usuario , PONEMOS I+1 para que que al cliente no le salga 0
for i in range(3):
    nombre = input(f"Introduce nombre del contacto {i + 1}: ")
    telefono = input(f"Introduce teléfono de {nombre}: ")
    agenda[nombre] = telefono

# Mostrar agenda completa
print("\n Agenda completa:")
for nombre, telefono in agenda.items():
    print(f"{nombre} : {telefono}")

# Permitir buscar un contacto
buscar = input("\nBuscar contacto: ")
if buscar in agenda:
    print("Teléfono:", agenda[buscar])
else:
    print("Contacto no encontrado")

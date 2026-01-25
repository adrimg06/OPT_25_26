def gestionar_persona() -> None:
    persona = {
        "nombre": "Roddy",
        "edad": 24,
        "ciudad": "Santiago de los Caballeros",
    }

# Añadir al diccionario persona una nueva clave llamada "profesion" con un valor de tipo cadena (por ejemplo, "Ingeniera").
    persona["profesion"] = "ingeniero"
#Eliminar la clave "ciudad" del diccionario persona.
    persona.pop("ciudad")

    for clave, valor in persona.items():
        print(clave,":", valor)

gestionar_persona()
def gestionar_persona() -> None:

    persona = {
        "nombre": "Jesus",
        "edad": 30,
        "ciudad": "Paradise",
    }

    for clave, valor in persona.items():
        print(clave,":", valor)




gestionar_persona()
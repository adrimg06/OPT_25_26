def gestionar_persona() -> None:
    persona = {
        "nombre": "Juan",
        "edad": 20,
        "ciudad": "Huelva"
    }
    #añadimos un nuevo campo a el diccionario
    persona["profesión"] = "ingenieria"
    #quitamos el campo de ciudad
    persona.pop("ciudad")

    for clave, valor in persona.items():
        print(clave,":", valor)




gestionar_persona()
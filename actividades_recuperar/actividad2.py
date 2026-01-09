def gestionar_persona() -> None:
    persona = {
        "nombre": "ana",
        "edad" : 30,
        "ciudad" : "Madrid"
    }
    #hacemos un for para recorer la lista y despues hacemos un print para mostrarla
    for clave in persona:
        print(f"{clave}: {persona[clave]}")

    persona["profesion"] = "ingeniería"
    del persona["ciudad"]

    for clave in persona:
        print(f"{clave}: {persona[clave]}")

gestionar_persona()
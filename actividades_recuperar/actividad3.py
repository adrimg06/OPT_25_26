def recorrer_valores():
    valores = [10, 20, 30, 40, 50]

    it = iter(valores)
    elemento = next(it)

#creamos un bucle while para cuando el elemnto no sea none

    while elemento is not None:
        print(f"Valor: {elemento}")
        elemento = next(it, None)

recorrer_valores()
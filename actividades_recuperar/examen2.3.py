def recorrer_iterador() -> None:
    valores = [10, 20, 30, 40, 50]

    it = iter(valores)
    elemento = next(it)

    while elemento is not None:
        print(elemento)
        elemento = next(it, None)



recorrer_iterador()
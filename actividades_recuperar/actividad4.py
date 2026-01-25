def contar_apariciones(nombre_elemento: str) -> None:
    elementos = ["python", "java", "python", "c", "python", "go", "java"]

    num_r = elementos.count(nombre_elemento)

    if num_r > 0:
        print(f" El elemento {nombre_elemento} aparece un total de {num_r} veces")
    else:
        print(f"El {nombre_elemento} no esta en la lista")


contar_apariciones("python")
contar_apariciones("java")
contar_apariciones("ruby")
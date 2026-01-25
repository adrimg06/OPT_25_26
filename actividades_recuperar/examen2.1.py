def contar_apariciones(nombre_elemento: str) -> None:
    elementos = ["python", "java", "python", "c", "python", "go", "java"]

    num_vec = elementos.count(nombre_elemento)

    if num_vec > 0:
        print(f"{nombre_elemento} aparece en la lista un numero de {num_vec}veces")
    else:
        print(f"{nombre_elemento} no aparece en la lista")

contar_apariciones("python")
contar_apariciones("java")
contar_apariciones("ruby")
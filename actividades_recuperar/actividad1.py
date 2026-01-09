def contar_aparciciones(nombre_elemento):
    contador = 0
    elementos = ["python", "java", "python", "c", "python", "go",
                 "java"]
    for elemento in elementos:
        if elemento == nombre_elemento:
            contador += 1

    if contador > 0:
        print(f"El elemento {nombre_elemento} aparece un total de {contador} veces")
    else:
        print(f"El elemento {nombre_elemento} no esta en la lista")


contar_aparciciones("python")
contar_aparciciones("java")
contar_aparciciones("ruby")
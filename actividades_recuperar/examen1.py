def contar_apariciones(nombre_elemento: str) -> None:
    elementos = ["python", "java", "python", "c", "python", "go", "java"]

#Contar cuántas veces aparece el valor del parámetro nombre_elemento dentro de la lista elementos.
    num_r = elementos.count(nombre_elemento)
    

#Si nombre_elemento aparece al menos una vez en la lista, mostrar por pantalla el mensaje:
    if num_r > 0:
        print(f"el elemento {nombre_elemento} tiene un total de {num_r} apariciones")
    else:
        print(f"el elemento {nombre_elemento} no aparece en la lista")



contar_apariciones("python")
contar_apariciones("java")
contar_apariciones("ruby")
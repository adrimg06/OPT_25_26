archivo = "prueba.txt"
modo =  "r"
encoding = "utf-8"

with open(archivo, modo, encoding=encoding) as archivo:
    contenido = archivo.read()
    print (contenido)
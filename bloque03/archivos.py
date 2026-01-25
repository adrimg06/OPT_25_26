archivo = "poema.txt"
modo = "r"
encoding = "utf-8"

with open(archivo, modo, encoding=encoding) as f:
    for linea in f:
        print(linea.strip())
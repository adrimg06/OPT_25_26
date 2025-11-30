# Definición de la función
def registrar_usuario(nombre, edad, ciudad="Madrid"):
    print(f"Usuario: {nombre}, Edad: {edad}, Ciudad: {ciudad}")


# Llamada con todos los argumentos posicionales
registrar_usuario("Ana", 25, "Sevilla")

# Llamada omitiendo el argumento de ciudad (usa valor por defecto)
registrar_usuario("Luis", 30)

# Llamada usando argumentos nombrados en distinto orden
registrar_usuario(edad=22, nombre="Marta", ciudad="Barcelona")

# Pedimos al usuario que introduzca un número y lo convertimos a entero
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

# Usamos un bucle for para recorrer los números del 1 al 10 (inclusive)
for factor in range(1, 11):
    # Calculamos el resultado de multiplicar el número introducido por el factor actual
    resultado = numero * factor

    # Mostramos el resultado en formato: "número x factor = resultado"
    print(f"{numero} x {factor} = {resultado}")

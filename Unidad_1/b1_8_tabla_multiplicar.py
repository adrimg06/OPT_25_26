numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

for factor in range(1, 11):
    resultado = numero * factor
    print(f"{numero} x {factor} = {resultado}")

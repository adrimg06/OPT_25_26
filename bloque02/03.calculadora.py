# SUMA DE DOS NUMEROS
def sumar(a, b):
    return a + b


# RESTA DE DOS NUMEROS
def restar(a, b):
    return a - b


# MULTIPLICACION DE 2 NUMEROS
def multiplicar(a, b):
    return a * b


# DIVISION DE DOS NUMEROS, CREAMOS QUE NOS DEVUELVA ERROR SI SE INTENTA DIVIDIR UN NUMERO ENTRE 0
def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero."
    return a / b


# ESTO ES EL PROGRAMA PRINCIPAL
num1 = float(input("Introduce el primer número: "))  # Introducimos el primer numero
num2 = float(input("Introduce el segundo número: "))  # introducimos el segundo numero

print(f"Suma: {sumar(num1, num2)}")
print(f"Resta: {restar(num1, num2)}")
print(f"Multiplicación: {multiplicar(num1, num2)}")
print(f"División: {dividir(num1, num2)}")

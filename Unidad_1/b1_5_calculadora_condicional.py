num1 = input("Introduce el primer número: ")
num2 = input("Introduce el segundo número: ")
operacion = input("Elige operación (suma, resta, multiplicacion, division): ").lower()

if operacion == "suma":
    resultado = num1 + num2
    print("Resultado:", resultado)
elif operacion == "resta":
    resultado = num1 - num2
    print("Resultado:", resultado)
elif operacion == "multiplicacion":
    resultado = num1 * num2
    print("Resultado:", resultado)
elif operacion == "division":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Error: No se puede dividir por cero.")
else:
    print("Operación no reconocida")

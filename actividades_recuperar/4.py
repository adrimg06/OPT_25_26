from actividades_recuperar.analisisnum import mayores_10

numeros = list(range(1,21))


# La lista pero elevado al cuadrado
cuadrados = [n **2 for n in numeros]

# L lista pero solo numeros pares
pares = [n for n in numeros if numeros % 2 == 0]

# La lista pero solo con los numeros mayores de 10
mayores_10 = [n for n in numeros if  n > 10]

# Diccionario que relaciona cada número con su doble
dobles = {n: n * 2 for n in numeros}

# Mostrar resultados
print("lista de cuadrados:", cuadrados)
print("lista de pares:", pares)
print("lista de mayores de 10:", mayores_10)
print("lista de dobles:", dobles)
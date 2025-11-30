# Generamos una  lista de 20 números
numeros = list(range(1, 21))

# La lista pero elevado al cuadrado
cuadrados = [n ** 2 for n in numeros]

# L lista pero solo numeros pares
pares = [n for n in numeros if n % 2 == 0]

# La lista pero solo con los numeros mayores de 10
mayores_10 = [n for n in numeros if n > 10]

# Diccionario que relaciona cada número con su doble
dobles = {n: n * 2 for n in numeros}

# Mostrar resultados
print("Lista original:", numeros)
print("Cuadrados:", cuadrados)
print("Números pares:", pares)
print("Números mayores que 10:", mayores_10)
print("Diccionario número → doble:", dobles)

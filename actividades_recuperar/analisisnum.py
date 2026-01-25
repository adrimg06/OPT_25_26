#Crea un programa que:

#Genere una lista de 20 números enteros (pueden ser introducidos manualmente o generados con range).
numeros = list(range(1,21))
#Obtener mediante comprensiones de listas:

#Una lista con los cuadrados de todos los números.
cuadrados = [n**2 for n in numeros]
#Una lista con solo los números pares.
pares =[n for n in numeros if n % 2 == 0]
#Una lista con los números mayores que 10.
mayores_10 = [n for n in numeros if n > 10]
#Cree un diccionario que relacione cada número con su doble.
dobles = {n: n*2 for n in numeros}
#Muestre en pantalla todos los resultados.

print("Lista original", numeros)
print("pares", pares)
print("Lista mayor", mayores_10)
print("dobles", dobles),

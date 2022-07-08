"""Haga uso de la función filter para construir un programa que, dado 
una lista de n números devuelva aquellos que son primos. Por 
ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], el programa que implemente 
debe devolver como resultado [3, 5, 5, 13"""

lista = [3, 4, 8, 5, 5, 22, 13]

# OPCIÖN 1
# copio la función es_primo del archivo de operaciones
# para usarla como condición en una función lambda

def es_primo(n):
    primo = True
    for i in range(2, n):
        if(n%i == 0):
            primo = False
    return primo

primos = list(filter(lambda x : es_primo(x), lista))

print(primos)


# OPCIÖN 2
# usando comprensión de listas dentro de lambda

primos1 = list(filter(lambda x: all([x%i for i in range(2, x)]), lista))
print(primos1)


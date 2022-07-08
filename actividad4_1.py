"""Haciendo uso de comprensión de listas realice un programa que, dado 
una lista de listas de números enteros, devuelva el máximo de cada 
lista. Por ejemplo, suponga la siguiente listas de listas:
[[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
El programa debe devolver el mayor elemento de cada sublista 
(señalado en negrita)."""

import pdb
pdb.set_trace()


lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

# valor_max = []
# for sublista in lista:
#     valor_max.append(max(sublista))
# print(valor_max) 

valor_max1 = [max(sublista) for sublista in lista]
print(valor_max1)

def max_sublista(n):
    val_max = [max(sublista) for sublista in n]
    return val_max

valor_max2 = max_sublista(lista)

print(valor_max2)
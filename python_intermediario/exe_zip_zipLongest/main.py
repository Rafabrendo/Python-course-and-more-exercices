# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']

# cid = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# cid2 = ['BA', 'SP', 'MG', 'RJ']

# lista = sorted([x for x in zip(cid, cid2)], key=lambda i: i[1], reverse=True)
# print(lista)



# def zipper(lista1, lista2):
#     intervalo = min(len(lista1), len(lista2))
#     return [(lista1[i], lista2[i]) for i in range(intervalo)]



# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# print(zipper(l1, l2))

from itertools import zip_longest


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))
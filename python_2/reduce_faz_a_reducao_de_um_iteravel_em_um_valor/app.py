#reduce -> faz a redução de um iterável em um valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#Basicamento, para um total
# total = 0
# for p in produtos:
#     total += p['preco']

# print(round(total, 1))

# print(sum([p['preco'] for p in produtos]))

def funcao_do_reduce(acumulador, produto):
    print('acumulador' ,acumulador)
    print('produto', produto)
    print()
    # return 1
    return acumulador + produto['preco']


#Tenho que passar um valor inicial no reduce. Nesse caso eu passei 0
total = reduce(
    funcao_do_reduce, 
    produtos, 0
)

total2 = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)

print('Total é', total)
print()
print('total2: ', total2)



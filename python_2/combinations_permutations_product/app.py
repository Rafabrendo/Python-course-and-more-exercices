"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa - iterável + tamanho do grupo
Permutação - Ordem importa
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster'],
] #preciso colocar a virgula no final

# print(list(combinations(pessoas, 2))) #passa a variavel e o minimo de combinações
# print(*list(combinations(pessoas, 2)), sep='\n') #desempacotei da lista, só ficou tupla


# print_iter(combinations(pessoas, 2))

# print_iter(permutations(pessoas, 2))

print_iter(product(*camisetas))


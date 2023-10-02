from produtos import produtos
from typing import Union
import copy

# def aumenta_preco(x) -> Union[list, dict]:
#     return [{** p, 'preco': round(p['preco'] * 1.1, 1)} for p in x ]
    


novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 1)} 
    for p in copy.deepcopy(produtos)
]

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'], reverse=True
)


ordenar_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)


# print(aumenta_preco(novos_produtos))
# print(orderna_produtos(produtos))

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*ordenar_por_preco, sep='\n')
from functools import partial
from types import GeneratorType


# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)



aumenta_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# novos_produtos = [
#     # {**p, 'preco': round(p['preco'] * 1.1, 2)} for p in produtos
#     # {**p, 'preco': aumentar_porcentagem(p['preco'], 1.1)} for p in produtos
#     {**p, 'preco': aumenta_dez_porcento(p['preco'])} for p in produtos

# ]

def muda_preco_de_produtos(produto):
    return{
        **produto, 
        'preco': aumenta_dez_porcento(
            produto['preco']
        )
    }

#Aqui, sem o list, é um iteraitor e eu posso esgota-lo, mas se eu colocar um list, muda tudo, porque eu posso reutilizar. Isso porque eu converti
novos_produtos = list(map(
    muda_preco_de_produtos, 
    produtos
))
#Aqui ele é um Generator porque eu o modifiquei
# novos_produtos = (x for x in produtos) #Para saber se é um generator
#Todo generator é um iteraitor, mas nem todo iteraitor é um genereitor


# print_iter(produtos)
print_iter(novos_produtos)
print_iter(produtos)

# print(novos_produtos)
# print(hasattr(novos_produtos, '__iter__'))
# print(hasattr(novos_produtos, '__next__'))
# print(isinstance(novos_produtos, GeneratorType))

# print(list(novos_produtos)) #Como é um iteraitor, eu o esgotei.


#Coloquei um list la no iteraitor e agr eu posso reutilizar
print(list(novos_produtos))


print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
)))
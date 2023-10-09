#filter é um filtro funcional

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

# lembre-se: O que vem a esquerda do for, em list compreension, é mapeamento, o que vem a direita é filtro.

# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 1000
# ]

def filtrar_preco(produto):
    return produto['preco'] > 100

novos_produtos = filter(
    # lambda p: p['preco'] > 10,
    filtrar_preco,
    # eu não preciso executar a função porque quem vai executa-la é o filter e vai passar o iteraitor tbm
    produtos
)


print_iter(produtos)
print_iter(novos_produtos)



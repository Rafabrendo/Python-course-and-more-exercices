#Esse exemplos são exemplos de mapeamento

produtos =[
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# posso desempacotar dicionario utilizando dois asteriscos **

novos_produtos = [
    {**produto}
    for produto in produtos
]

# como no começo é lista, eu desempacoto com * -> vai desempacotar a primeira parte
# nesse caso eu desempacotei uma
#print(*novos_produtos, sep='\n')

"""
{'nome': 'p1', 'preco': 20}
{'nome': 'p2', 'preco': 10}
{'nome': 'p3', 'preco': 30}
"""

#Aumentando o preço em 5%
#Passei uma expressão lambda
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]
print()
#print(*novos_produtos, sep='\n')



novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
#Vou aumentar somente os produtos com preço acima de 20. Utilizei expressão lambda e operação ternaria. 
#Na operação ternária eu tenho/eu retornei o próprio produto

print()
#print(*novos_produtos, sep='\n')

#Utilizando o filter
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if(produto['preco'] >= 20 and produto['preco'] * 1.05 ) > 10
]

print(*novos_produtos, sep='\n')
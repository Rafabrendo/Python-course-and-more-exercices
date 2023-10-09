"""
Interando strings com while
"""
nome = 'Rafael Brendo'

indice = 0
nova_string = ''
while indice < len(nome):
    #nova_string += nome[indice]
    nova_string += f'*{nome[indice]}'
    #é um jeito de colocar caracteres. Utlizando o while e f'strings

    indice += 1

print(nova_string)
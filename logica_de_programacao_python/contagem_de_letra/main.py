frase = 'O Python é uma linguagem de programação  ' \
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

maior = 0
letra_que_apareceu_mais_vezes = ''
i = 0
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1 #se eu não fizer isso, vou ter um bug no codigo, e vou ter um laço infinito
        continue #vou pular os espaços, se tiver

    q_apareceu = frase.lower().count(letra_atual)


    if i == 0:
        maior = q_apareceu
        letra_que_apareceu_mais_vezes = frase[i]
    else:
        if q_apareceu > maior:
            maior = q_apareceu
            letra_que_apareceu_mais_vezes = frase[i]

    i += 1
    

print(f'A letra {letra_que_apareceu_mais_vezes}'
    f'apareceu {maior} vezes')


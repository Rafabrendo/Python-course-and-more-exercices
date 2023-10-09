#Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta' : 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
       'Pergunta': 'Quanto é 10/5?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '2', 
    }
]

#Aqui eu mostro a resposta dps q eu respondo
# cont = 0
# for p in perguntas:
#     for k, v in p.items():
#         print(k, v)
#         if k == 'Opções':
#             resposta = input('Digite uma opção:')
#             if resposta == p['Resposta']:
#                 cont += 1  
# print(cont)       

#aqui eu não mostro a resposta dps de respondida a pergunta
#   

qtd_acertos = 0 
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ') #vai parar no input

    #Flags
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes) #para verificar se o q foi digitado está nas opções.

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
                qtd_acertos += 1

    print()
    if acertou:
        print('Acertou ✔️')
    else:
        print('Errou ❌')


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')

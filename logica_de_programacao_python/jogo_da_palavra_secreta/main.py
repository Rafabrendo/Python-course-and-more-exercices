"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
-Você vai propor uma palavra secreta e vai dar a possibilidade para o usuário digitar apenas uma letra.
-Quando o usuário digitar uma letra, você vao conferir se a letra digitada está na palavra secreta.
   - Se a letra digitada estiver na palavra  secreta; exiba a letra;
   - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""


# palavra = 'Adivinha'
# armazenar = ''
# tamanho = len(palavra)

# for c in range(5):
   
#     digite = input('Digite uma letra:')

    
#     resultado = ''
    
#     if digite in palavra:
#         if armazenar.count(digite) < palavra.count(digite) :
#             armazenar += digite
    
#     for i in range(tamanho):
#         if palavra[i] in armazenar:
#             resultado += palavra[i]
#         else:
#             resultado += '-'
#     print(resultado)
#     print()


"""
os -> Diversas interfaces de sistema operacional.
Vou utilizar um modulo do os para limpar o terminal
"""

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:

    letra_digitada = input('Digite uma letra:')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue #vai voltar pro começo do laço
    

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada: ', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('cls') #clear no mac e linux; cls no windows para limpar o terminal
        print(f'VOCÊ GANHOU!! PARABÉNS! PALAVRA: {palavra_secreta}')
        print('Tentativas: ', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
    
    


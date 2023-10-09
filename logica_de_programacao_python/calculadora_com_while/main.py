# while True:

#     numero_1 = input('Digite um numero:')
#     numero_2 = input('Digite outro numero:')

#     if numero_1.isnumeric:
#         if not numero_1.isdecimal:
#             numero_1 = int(numero_1)
#         else:
#             numero_1 = float(numero_1)
#     else:
#         print('Digite apenas numeros.')
    
#     if numero_2.isnumeric:
#         if not numero_2.isdecimal:
#             numero_2 = int(numero_2)
#         else:
#             numero_2 = float(numero_2)
#     else:
#         print('Digite apenas numeros.')

#     print(numero_1 * numero_2)
#     cont = input(f'Deseja continuar? [s/n]').lower().startswith('n')

#     if cont:
#         break
    
from time import sleep

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador: (+-*/)')

    numeros_validos = None #é uma flag

    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)

        numeros_validos = True


    # except Exception as error:
    #     print(error) #Para saber qual erro ocorreu!
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operadores inválidos')
        continue #Eu coloco continue porque teoricamente o meu codigo tem que parar aqui e voltar pro começo

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo: ')
    if operador == '+':
        sleep(1)
        print(f'{numero_1} + {numero_2} = ',numero_1 + numero_2)
    elif operador == '-':
        sleep(1)
        print(f'{numero_1} - {numero_2} = ', numero_1 - numero_2)
    elif operador == '/':
        sleep(1)
        print(f'{numero_1} / {numero_2} = ', numero_1 / numero_2)
    elif operador == '*':
        sleep(1)
        print(f'{numero_1} * {numero_2} = ',numero_1 * numero_2)
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
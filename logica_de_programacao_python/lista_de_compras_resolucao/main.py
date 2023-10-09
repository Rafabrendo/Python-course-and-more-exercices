import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    #Poderia ter usado o starwith()
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
            #não coloco o continue porque já está no final do laço. Daí volta pro começo do laço.
        except IndexError:
            print('Indice não existe na lista.')
        except Exception:
            #vai capturar qualquer exception que tem no python
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')
        
        #O for não vai fazer nada numa lista vazia.
        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print('Por favor, escolha i, a ou l.')
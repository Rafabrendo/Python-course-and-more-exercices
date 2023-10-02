# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café', ] -> Refazer['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo['fazer café']
# refazer = todo['fazer café, 'caminhar']

from os import system
from time import sleep

lista = []
desfazeer = []
# def fazer(ordem:str) -> None:
#     return lista.append(ordem)

# def desfazer() -> None:
#     desfazeer.append(lista[-1])
#     return lista.pop()

def refazer() -> None:
    lista.append(desfazeer[-1])
    return desfazeer.pop()

#É um jeito de fazer
# def listar():
    
#     for itens in lista:
#         print(itens)

#Outro jeito
def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return #O return aqui vai parar a execução da função aqui.
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
        #\t -> tab

#outro jeito
def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    tarefa = tarefas.pop()#o pop vai retornar o ultimo elemento antes de excluir 
    tarefas_refazer.append(tarefa)

#outro jeito de fazer
def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

#outro jeito de fazer
def adicionar(tarefa, tarefas):
    print()
    tarefas = tarefa.strip()
    if not tarefas:
        print('Você não digitou uma tarefa.')
        return
    tarefas.append(tarefa)



while True:
    print(
        """Escolha uma opção:
         [1] fazer 
         [2] desfazer 
         [3] refazer  
         [4] listar 
         [5] sair 
         """
    )

    opcao = int(input())
    if opcao == 1:
        comando = str(input("Digite um comando: "))
        fazer(comando)
        continue
        
    
    elif opcao == 2:
        desfazer()
        continue
        
    
    elif opcao == 3:
        refazer()
        continue

    elif opcao == 4:
        listar()
        sleep(1)
        system('cls')
        continue

    elif opcao == 5:
        break

    else:
        print('Não entendi, tente novamente!')
        sleep(2)
        continue
    



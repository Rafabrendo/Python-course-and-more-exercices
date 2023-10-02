# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café', ] -> Refazer['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo['fazer café']
# refazer = todo['fazer café, 'caminhar']


#Vou adiar a execução da função, envolvendo-a em outra função


import os

tarefas=[]
tarefas_refazer=[]

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
    print()

#outro jeito
def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()#o pop vai retornar o ultimo elemento antes de excluir
    tarefas_refazer.append(tarefa)
    listar(tarefas)


#outro jeito de fazer
def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    listar(tarefas)

#outro jeito de fazer
def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print("Adicionada a lista de tarefas")
    tarefas.append(tarefa)
    listar(tarefas)

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    #Vou adiar a execução da função, envolvendo-a em outra função. No caso a lambda
    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }

    # comando = comandos.get(tarefa)()
    #Ou é a tarefa que a possoa digitar, se exisitr, vai ser um comando, se não existir, vai ser adicionar
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
            comandos['adicionar']
    comando()

    
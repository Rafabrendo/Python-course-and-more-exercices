# groupby - agrupando valores (itertools)
#os dados precisam estar ordenados para poderem ser agrupados posteriormente(user sort ou sorted)

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

# alunos = ['a', 'a', 'a', 'b', 'c']
# alunos = ['a', 'a', 'a', 'b', 'c', 'a'] #dados desordenados
# grupos = groupby(sorted(alunos)) #usei o sorted para ordenar
# print(*list(grupos), sep='\n')

# grupos = groupby(alunos)

# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo)) #vai agrupar todos os a's em um grupo

# vou ordernar a lista

# alunos_agrupados = sorted(alunos, key=lambda a: a['nota']) #vai fazer uma copia rasa e ordenar por nota
alunos_agrupados = sorted(alunos, key=ordena) 

# for aluno in alunos_agrupados:
#     print(aluno)

# grupos = groupby(alunos_agrupados, key=lambda a: a['nota'])#passei a chave que eu quero que ele use para agrupar
grupos = groupby(alunos_agrupados, key=ordena)
for chave, grupo in grupos:
    print(chave)
    # print(list(grupo))
    for aluno in grupo:
        print(aluno)


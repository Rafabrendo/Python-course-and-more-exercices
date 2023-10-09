"""
Crie uma função que encontra o primeiro duplicado considerando o segundo número como a duplicação. Retorne 
a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em  si.
    Exemplo:
        [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
    Se não encontrar duplicados na lista, retorne -1
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
]


        
#APENAS COM LISTA
def lista_duplucados(n):
    # occorrencia = []
    ocorrencia = -1
    lista_dupl = list()
    for x in n:
        if x in lista_dupl:
            # occorrencia.append(x)
            ocorrencia = x
            break
        # if n.count(x) > 1:
        #     lista_dupl.append(x)
        lista_dupl.append(x)
    return ocorrencia


for numero in lista_de_listas_de_inteiros:
    print(lista_duplucados(numero))




#   USANDO SET
"""
def encontra_primeiro_dupl(lista_de_inteiro):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiro:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        
        numeros_checados.add(numero)

    return primeiro_duplicado


for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontra_primeiro_dupl(lista)
    )
"""




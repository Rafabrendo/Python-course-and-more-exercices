# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema 
# - Um caso base que para a recursão
# - fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120

# import sys

# sys.setrecursionlimit(1004)

# def recursiva(inicio=0, fim=10):
#     #Caso basse
#     if inicio >= fim:
#         return fim

#     print(inicio, fim)
    
#     # Caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)


# print(recursiva(0, 1001))


# from functools import reduce
# fatorial = reduce(
#     lambda ac, p: ac * p, 
#     range(5, 1, -1),
#     1
#     )
# print(fatorial)


def factorial(n):
    if n <= 1 :
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))
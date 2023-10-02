#Função multiplica:

from functools import reduce

def multiplica(*args):
    return reduce(lambda x, y: x*y, args)

#O reduce é uma função acumulativa, na qual eu posso passar uma função anonima.

numero = 1, 2, 3, 4, 5
# x = multiplica(1, 2, 3, 4)
# print(x)
#print(multiplica(numero)) #Desse jeito apenas retorna a tubla, isso porque ela não está desempacotada #(1, 2, 3, 4, 5)
print(multiplica(*numero)) #Desse jeito retorna o resultado. Isso porque eu desempacotei a tupla #120


#Outro jeito:
from math import prod
#prod é uma função no python que retorna o produto dos iterabeis

def mult(*args):
    return prod(args)



numero = 1, 2, 3, 4, 5, 6
print(mult(numero)) #Retornou (1, 2, 3, 4, 5, 6) porque eu não desempacotei
print(mult(*numero)) #retornou 720


#Função par ou ímpar

# def parImpar(valor):
#     if valor % 2 == 0:
#         return f'Par'
#     else:
#         return f'Impar'

# print(parImpar(2))

# def parImpar(*args):
#     par = []
#     impar = []
#     for n in args:
#         if n % 2 == 0:
#             par.append(n)
#         else:
#             impar.append(n)
#     return f'Par : {par};  Impar : {impar}'



# numero = 1,2,3,4,5,6,7,8,9
# print(parImpar(*numero))
    

def parImpar(numero):
    multiplo_de_2 = numero % 2 == 0
    #condição ternaria
    if multiplo_de_2:
        return f'{numero} é par'
    #nesse caso o else é redudante porque ao entrar numa opção que tenha o return, é fim do codigo
    #else:
    return f'{numero} é ímpar'


print(parImpar(4))
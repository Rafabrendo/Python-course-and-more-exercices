#Variáveis livres + nonlocal (locals, globals)

# print(globals())
# def fora(x):
#     a = x #Esta é uma variável livre

#     #Nesse caso vai retornar a função sem executa-la(Essa função está dentro da função fora)
#     def dentro():
#         # print(locals()) # vai dizer quais variaveis são locais
#         # print(dentro.__code__.co_freevars)  #Vai mostrar as variaveis livres
#         return a
#     return dentro



# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        #valor_final += valor_a_concatenar #Se eu fizer assim vai dar erro porque valor_final é uma variavel que não é desse escopo e por isso não pode ser alterada assim. Daí eu vou usar o nonlocal
        nonlocal valor_final #Significa que essa variavel não é local e eu posso alterá-la
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)
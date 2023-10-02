#Closure

# def duplicar(numero):
#     return numero * 2


# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4



def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar 
    #Estou retornando a função e não executando-a
    #Faz com que lembre o valor 'padrão' passado


duplicar = criar_multiplicador(2) #Esse é o valor padrão #é como se eu tivesse feito um objeto
print(duplicar(2))#Esse é o valor dinamico
triplicar = criar_multiplicador(3)
print(triplicar(2))
quadruplicar = criar_multiplicador(4)
print(quadruplicar(2))

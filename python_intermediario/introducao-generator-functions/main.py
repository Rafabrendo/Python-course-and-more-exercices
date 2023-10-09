#Generator são funções que sabem pausar. Todo generator é um itereitor tbm
#Introdução às Generator functions em Python
#generator = (n for n in range(1000000))
  


#def generator(n=0,  maximum=10):
    #para eu usar a 'pausa', eu posso trocar o return por yield
    # yield 1 #Pausar
    # #return 'ACABOU' #Vai levantar uma exceção com essa palavra q eu coloquei (ACABOU)
    # #StopIteration
    # print('Continuando...')
    # yield 2 #Pausar
    # print('Mais uma...')
    # yield 3
    # print('Vou terminar')
    # return 'ACABOU'


#minha função acumuladora que tbm pausa
def generator(n=0,  maximum=10):
    while True:
        yield n 

        n += 1

        if n >= maximum:
            return

        





# gen = generator(n=0)
# print(gen)
# print(gen.__iter__())
#print(next(gen)) #Esse next é para o primeiro yield
#print(next(gen)) #Esse next é para o proximo yield
"""
1
Continuando...
2
"""

#print(next(gen))
#print(next(gen))

# for n in gen:
#     print(n)
"""
1
Continuando...
2
Mais uma...
3
Vou terminar"""


# gen = generator(n=5, maximum=8)
# for n in gen:
#     print(n)


gen = generator(maximum=1000)
for n in gen:
    print(n)
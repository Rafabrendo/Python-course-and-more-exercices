#Yield from
#No generetor pode se fazer um yield from

def gen1():
    print('Começou gen1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


# def gen2():
#     yield from gen1() #Vai chamar o codigo de gen1 #Vai retornar dados
#     yield 4
#     yield 5
#     yield 6


def gen3():
    print('Começou gen3')
    #yield from gen() 
    yield 10 
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen):
    print('Começou gen2')
    yield from gen() 
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


# g = gen2()
g1 = gen2(gen1)
g2 = gen2(gen3)
for numero in g1:
    print(numero)
for numero in g2:
    print(numero)
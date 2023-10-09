#Decoradores com parâmetros
#As funções decoradoras são factory functions(fabrica de funções)

#agr eu tenho acesso a três escopos
def fabrica_de_decoradores(a=None, b=None, c=None):
    
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        #Vai adiar a execução da função
        #Inner function(função interna)
        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada

    return fabrica_de_funcoes





# def blablabla(a, b, c):
#     print(a, b, c)
#     return fabrica_de_funcoes


# @decoradora() -> vai dar erro assim porque tá tentando executar o decorador antes do python
#Vai executar direto
#@decoradora #vai fazer com qua a função soma vá como parametro na função decoradora
# @blablabla(1, 2, 3)
# @fabrica_de_funcoes
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y 

# multiplica = fabrica_de_funcoes()(lambda x, y: x * y)
decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
dez_mais_cinco = multiplica(10, 5)
print(dez_mais_cinco)

#raise - lançando exceções (erros)
#posso criar uma classe com o meu erro e chamar ela qui
#Posso usar try dentro de try


# print(123)
# raise ValueError('Deu erro') #Estou lançando esse erro com o raise e passei o nome do erro(classe)
# print(123)

# def divide(n, d)
#     try:
#         return n /d
#     except ZeroDivisionError:
        #return n
        #raise #Se eu tiver um raise dentro do except, ele vai relançar a exceção que eu 'estou'(ZeroDivisionError) #Isso é redundante
         


#print(divide(8, 0))


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser int ou float.'
            f' "{tipo_n.__name__}" enviado.'
        )
    return True

def não_aceito_zero(d):#Função 
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero.')
    return True #Ou essa função retorna true ou dá erro 


def divide(n, d): #não é papel dessa função tratar erro
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    não_aceito_zero(d)
    return n / d


print(divide(8, '0'))



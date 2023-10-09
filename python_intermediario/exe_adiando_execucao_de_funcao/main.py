#Exercício - Adiando execução de funções
def soma(x=1, y=1):
    return x + y

def multiplica(x=1, y=1):
    return x * y

#closure
def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5) #Aqui eu salvei na memoria
multiplica_por_dez = criar_funcao(multiplica, 10) #Aqui eu salvei na memoria
print(soma_com_cinco(10)) #Agora eu estou passando o y
print(multiplica_por_dez(2)) #Agora eu estou passando o y

#Posso decorar uma função, assim eu posso adiar a sua execução
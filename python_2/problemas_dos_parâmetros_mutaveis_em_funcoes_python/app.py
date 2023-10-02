#Problema dos parâmetros mutaveis em funções Python #Não é legal colocar parâmetros mutáveis dentro de parâmetros padrão. lista=[] tá dentro de um parametro padrão. Eu colocaria none
# def adiciona_clientes(nome, lista=[]):
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista



# cliente1 = adiciona_clientes('Rafa')
# adiciona_clientes('Joana', cliente1) #Todas as vezes que eu chamar a função, a lista que está como parâmetro
# # vai ser usada e se tiver coisas dentro, elas vão ser usadas tbm. A lista como parâmetro não vai ser recriada
# print(cliente1)


# lista1 = []
#Para resolver isso:
# cliente1 = adiciona_clientes('Rafa', lista1) #Agr a lista do parametro não vai ser mais usada, vai ser usada a lista1
cliente1 = adiciona_clientes('Rafa')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Bruna', cliente1)
cliente1.append('Juca')
print(cliente1)

cliente2 = adiciona_clientes('Brendo') #A lista que foi definida na primeira definição da função vai ser usada.
adiciona_clientes('Joana', cliente2)
print(cliente2)


print()
print(cliente1)
print(cliente2)

# Agr eu vou ter listas independentes.
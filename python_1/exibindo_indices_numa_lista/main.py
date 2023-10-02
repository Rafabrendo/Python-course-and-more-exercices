lista = ['Maria', 'Helena', 'Luiz']

# for num, nome in enumerate(lista):
#     print(num)
    #solução 

lista.append('Rafa')

indices = range(len(lista))
print(indices)

for indice in indices:
    print(indice, lista[indice] )
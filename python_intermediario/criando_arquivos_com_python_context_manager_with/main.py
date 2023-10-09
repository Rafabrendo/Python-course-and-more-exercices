# Criando arquivos com Python
# Usamos a função open para abrir um arquivo em Python(ele pode ou não existir)
# modos:
# r(leitura), w(escrita), x(para criação), a(escreve ao final), b(binário)
# t(modo texto), + (leitura e escrita)
# Context manager - with(abre e fecha)
# Métodos úteis
# write, read(escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines(ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load


#Posso fazer assim, colocando o caminho completo
#caminho_arquivo = 'D:\\workspace\\ws-python-atualizacao\\python_2\\criando_arquivos_com_python_context_manager_with\\'
#vou criar um arquivo.txt
#caminho_arquivo += 'arquivo.txt'
#vou concatenar 

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()#tem que fechar sempre

# vou usar o context manager
# with open(caminho_arquivo, 'w') as arquivo:
#     print('Olá mundo')
#     print('Arquivo vai ser fechado')

# Posso fazer assim tbm: (Esse arquivo vai ser criado dentro do diretorio do projeto, ou seja, na mesma pasta)
caminho_arquivo = 'arquivo.txt'

nomes = ['Rafa', 'Brendo']

#obs.: o with open() abre e fecha o arquivo
with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\r\n') #desse jeito eu quebrei a linha 2x
    arquivo.write('linha 3\n\n') #desse jeito eu tbm quebrei a linha 2x
    arquivo.write('linha 4\n')
    #Vou mandar várias linhas
    arquivo.writelines(
        ('linha 5\n', 'linha 6\n')

    )

    arquivo.seek(0, 0) #vai mover o cursor para o topo e assim eu vou conseguir fazer a leitura
    print(arquivo.read()) #tenho que colocar 'w+' que é escrita com a possibilidade de leitura
    arquivo.seek(0, 0)
    print('Lendo linha por linha:')
    print(arquivo.readline(), end='') #É tipo um next
    print(arquivo.readline().strip()) #.strip serve para remover espaço(olhar aula sobre strings)
    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines(): #readlines é uma lista de strings
        print(linha.strip())

print('#' * 30)

#Para ler o arquivo diretamente.
with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
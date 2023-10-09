
# lista_de_compras = []
lista_de_compras = list()


while True:
    
    print(f' Escolha uma opção:'
            f'[1] Adicionar produto'
            f'[2] Apagar produto'
            f'[3] listar valores da lista de produtos')
    
    escolha = input(':')
    if escolha.isnumeric:
        escolha = int(escolha)
    
    
    if escolha == 1:
        dados = []
        produto = input('Produto: ')
        valor = float(input('Valor: '))
        dados.append(produto)
        dados.append(valor)
        lista_de_compras.append(dados[:])
        dados.clear
    
    if escolha == 2:
        try:
            for indice, produto in enumerate(lista_de_compras):
                print(f'Numero: {indice}  --  Produto: {produto}')
            pop_produto = input('Digite o nome do produto a ser apagado:')
            lista_de_compras.pop(pop_produto)
        except NameError as erro:
            print(erro)
            continue
    
    if escolha == 3:
        valor = 0
        try:
            for indice, produto in enumerate(lista_de_compras):
                print(f'Numero: {indice}  --  Valor: {produto[1]}')
                valor += produto[1]
                print(valor)
        except NameError as erro:
            print('Erro: ', erro)
            continue


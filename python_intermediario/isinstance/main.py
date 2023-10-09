#isinstance -> para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    # se for uma instancia de set, eu adiciono...
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))

    if isinstance(item, str):
        print('STR')
        print(item.upper())

    #se o item é instancia de int ou float
    if isinstance(item, (int, float)):
        print(item, item * 2)
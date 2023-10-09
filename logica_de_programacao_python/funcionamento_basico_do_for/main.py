"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entre seu iterador
"""
# texto = 'Rafael'.__iter__()
texto = iter('Rafael') #é a mesma coisa de chamar o metodo __iter__()
print(texto.__next__()) #assim ou 
print(next(texto)) #assim
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print()
#quando esgota os valores um erro é levantado


#for letra in texto
texto = 'Rafildes' #iterável
iterador = iter(texto) #iterator

#o for faz isso(básicamente):
# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)

# count é um iterador sem fim
from itertools import count

c1 = count() #é infinito, iteraitor e interavel 
r1 = range(10) #é um iteravel mas não um itereitor(__next__)

print(next(c1))
print(next(c1))

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))


#c2 = count(10, 8) #start, step
c2 = count(step=10, start=8) #nomeando. Passei invertido
for i in c2:
    if i >= 40:
        break
    print(i)

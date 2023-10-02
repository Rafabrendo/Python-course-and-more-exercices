#print(*path, sep='\n')
#__name__

# from aula99_package.modulo import fala_oi
#vai importar da aula 99 o modulo e a função dentro do modulo


# print(fala_oi())

"""
vai mostrar:
você importou aula99_package
Oi"""

import aula99_package
#O package passa a se comportar como um modulo

print(aula99_package.dobra(2))

from aula99_package.modulo import soma_do_modulo

print(soma_do_modulo(2, 3))

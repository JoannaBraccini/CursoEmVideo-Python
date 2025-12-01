# Utilizando módulos

from math import sqrt, floor
import random
import emoji

# documentação: python.org, PyPi

num = int(input('Digite um número inteiro: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}.'.format(num, floor(raiz)))

#---------------------------------------------
n = random.randint(1, 10)
print('Número aleatório gerado: {}.'.format(n))

#---------------------------------------------
print(emoji.emojize('Olá, Mundo! :earth_americas:', language="alias"))
# sem o language="alias", usa-se o próprio emoji copiado do Pypi:
print(emoji.emojize('Olá, Mundo! 🌎'))

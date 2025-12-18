# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número inteiro para calcular seu fatorial: '))
count = num
fatorial = 1
print('Calculando {}! = '.format(num), end='')
while count > 0:
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    fatorial *= count #vai multiplicando o valor de count pelo resultado
    count -= 1
print(fatorial)

# Solução com módulo:
from math import factorial
n = int(input('Digite um número para calcular seu fatorial'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

# Solução sem módulo: igual o meu :)
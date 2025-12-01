# Crie um programa que leia um número real qualquer pelo
# teclado e mostre na tela a sua porção inteira
# Ex: 6.127 -> 6

from math import trunc
num = float(input('Digite um número real: '))
print('O número {} tem a parte inteira {}.'.format(num, trunc(num)))

#Solução 1
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, trunc(num)))

#Solução 2
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))

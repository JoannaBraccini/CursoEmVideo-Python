# Escreva um programa que leia dois números inteiros e
# compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior / O segundo valor é maior ou
# Não existe valor maior, os dois são iguais
from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('{}Comparando...{}'.format('\033[33m', '\033[m'))
sleep(2)
if n1 > n2:
    print('{}{} é maior que {}.{}'.format('\033[35m', n1, n2, '\033[m'))
elif n2 > n1:
    print('{}{} é maior que {}.{}'.format('\033[35m', n2, n1, '\033[m'))
else:
    print('{}Não existe valor maior, {} e {} são iguais.{}'.format('\033[35m', n1, n2, '\033[m'))

#Solução igual :)
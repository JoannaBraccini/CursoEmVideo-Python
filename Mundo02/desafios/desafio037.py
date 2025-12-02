# Escreva um programa que leia um número inteiro e peça
# para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
from time import sleep

#matemática:
# Para converter um número decimal para binário,
# divida o número por 2 sucessivamente e anote os restos.
# O resultado é obtido ao ler os restos de baixo para cima,
# formando o número binário equivalente.
# Para octal, divida por 8 e para hexadecimal por 16.

# Python tem métodos que fazem os cálculos: bin(), oct(), hex()

num = int(input('{}Digite um número inteiro: {}'.format('\033[34m', '\033[m')))
base = int(input("""Escolha a base de conversão:
[ 1 ] binária.
[ 2 ] octal.
[ 3 ] hexadecimal.
OPÇÃO: """))
print('{}Calculando...{}'.format('\033[33m', '\033[m'))
sleep(1)
if base == 1:
    print('{} convertido para {}binário{} é {}!'.format(num, '\033[32m', '\033[m', bin(num)[2:]))
elif base == 2:
    print('{} convertido para {}octal{} é {}!'.format(num, '\033[32m', '\033[m', oct(num)[2:]))
elif base == 3:
    print('{} convertido para {}hexadecimal{} é {}!'.format(num, '\033[32m', '\033[m', hex(num)[2:]))
else:
    print('{}Opção inválida.{}'.format('\033[1:31m', '\033[m'))

#Solução
# fatiamento para remover os 2 dígitos indicadores da base (num)[2:]
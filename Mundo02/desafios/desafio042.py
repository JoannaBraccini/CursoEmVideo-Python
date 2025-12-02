# Refaça o DESAFIO 035 dos triângulos, acrescentando o
# recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

#035: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo

r1 = float(input('{}Primeira reta: '.format('\033[34m')))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: {}'.format('\033[m')))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas formam um triângulo do tipo ', end='')
    if r1 == r2 == r3: print('{}EQUILÁTERO{}!'.format('\033[1:33m', '\033[m'))
    elif r1 == r2 or r1 == r3 or r2 == r3: print('{}ISÓSCELES{}!'.format('\033[1:33m', '\033[m'))
    else: print('{}ESCALENO{}!'.format('\033[1:33m', '\033[m'))
else: print('As retas não podem formar um triângulo.')

#Solução:
# if r1 != r2 != r3 != r1 -> escaleno
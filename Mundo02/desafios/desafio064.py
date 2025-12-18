# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = c = s = 0
while n != 999:
    n = int(input('{}Digite um valor inteiro{} {}[999 para parar]:{} '.format('\033[36m', '\033[m', '\033[35m', '\033[m')))
    if n != 999:
        s += n
        c += 1
    else: print('{}Finalizando...{}'.format('\033[33m', '\033[m'))
print('{}Você digitou {} números e a soma entre eles foi {}.{}'.format('\033[34m', c, s, '\033[m'))

# Solução:
print('-='*20)
num = soma = cont = 0 # em vez de declarar uma em cada linha
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

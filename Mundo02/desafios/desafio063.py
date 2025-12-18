# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

# matemática: Comece com os dois primeiros números: 0 e 1.
# Calcule o próximo número somando os dois anteriores: 0 + 1 = 1.
# Continue somando os dois anteriores para encontrar os seguintes números: 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8, 5 + 8 = 13, 8 + 13 = 21, 13 + 21 = 34,
# e assim por diante.

# num = int(input('Digite um número: '))
# if num <= 0:
#     print('Nenhum termo para mostrar.')
# else:
#     a = 0
#     b = 1
#     i = 0
#     while i < num:
#         if i == 0:
#             print(a, end='')
#         else:
#             print(' → {}'.format(a), end='')
#         a = b, a + b
#         i += 1
#     print(' → FIM')

# Solução:
print('-=' * 20)
print('Sequência de Fibonacci')
print('-=' * 20)
n = int(input('Quantos termos da sequência de Fibonacci você quer mostrar? '))
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
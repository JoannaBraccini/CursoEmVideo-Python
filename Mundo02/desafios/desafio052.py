# Faça um programa que leia um número inteiro e diga se ele
# é ou não um número primo.

# Regras básicas:
# Números menores ou iguais a 1 não são primos.
# O número 2 é o único primo par.
# Qualquer número par maior que 2 não é primo.
# Teste de divisibilidade:
# Divida o número por todos os inteiros de 2 até a raiz quadrada dele.
# Se encontrar algum divisor exato (resto zero), o número não é primo.
# Se não encontrar nenhum divisor, ele é primo.

num = int(input('Digite um número inteiro: '))
mult = 0
# limite = int(num ** 0.5) + 1

# if num < 2: mult += 1
# for c in range(2, limite):
#     if num % c == 0:
#         mult += 1
#
# if mult > 0: print('{}{} não é primo!{}'.format('\033[31m', num, '\033[m'))
# else: print('{}{} é primo!{}'.format('\033[33m', num, '\033[m'))

#Solução:
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1:32m', end='')
        mult += 1
    else: print('\033[:31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, mult))
if mult == 2: print('E por isso ele é \033[33mPRIMO\033[m!')
else: print('E por isso ele \033[1:31mNÃO\033[m é PRIMO!')
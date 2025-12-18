# Melhore o desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

# print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
# comp = randint(0, 10)
# print('Pensando...')
# sleep(1)
# num = int(input('Em que número pensei? '))
# count = 1
# while num != comp:
#     n = int(input('Errou! Tente novamente: '))
#     num = n
#     count += 1
# print('Você acertou! Só precisou de {} tentativas.'.format(count))

# Solução:
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador: print('Mais... Tente novamente.')
        elif jogador > computador: print('Menos... Tente novamente.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
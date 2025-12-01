# Escreva um programa que faça o computador "pensar" em um
# número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
comp = randint(0, 5)
num = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(2)
if num == comp:
    print('Você acertou!')
else:
    print('Errou, pensei em {}. Tente novamente.'.format(comp))

#Solução igual <3
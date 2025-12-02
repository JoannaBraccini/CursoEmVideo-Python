# Crie um programa que faça o computador jogar Jokenpô
# com você
# pedra > tesoura > papel > pedra
from time import sleep
from random import randint
user = int(input("""{}Vamos jogar {}JOKENPO{}?
Escolha:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
{}OPÇÃO: """.format('\033[34m', '\033[1:32m', '\033[m', '\033[34m')))
opt = ('Pedra', 'Tesoura', 'Papel')
comp = randint(1, 3)
sleep(1)
if user in (1, 2, 3):
    print('{}JO...KEN...PO{}'.format('\033[1:35m', '\033[m'))
    print("""    Jogador jogou {}
    Computador jogou {}""".format(opt[user-1], opt[comp-1]))
if (comp == 1 and user == 3
        or comp == 2 and user == 1
        or comp == 3 and user == 2):
    print('{}Computador venceu!'.format('\033[31m'))
elif (user == 1 and comp == 3
      or user == 2 and comp == 1
      or user == 3 and comp == 2):
    print('{}Você venceu!'.format('\033[32m'))
elif comp == user: print('{}Empate!'.format('\033[33m'))
else:
    print('{}Opção inválida!{}'.format('\033[1:31m', '\033[m'))

#Solução
if comp == 1:
    if user == 1: print('Empate!')
    elif user == 2: print('Jogador venceu!')
    elif user == 3: print('Computador venceu!')
elif comp == 2:
    if user == 1: print('Computador venceu!')
    elif user == 2: print('Empate!')
    elif user == 3: print('Jogador venceu!')
elif comp == 3:
    if user == 1: print('Jogador venceu!')
    elif user == 2: print('Computador venceu!')
    elif user == 3: print('Empate!')
else: print('Jogada inválida.')
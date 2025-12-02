# Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar no serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que
# passou do prazo
from datetime import date

nasc = int(input('Qual o ano de seu nascimento? '))
atual = date.today().year
idade = atual - nasc

print('Quem nasceu em {} faz {} em {}.'.format(nasc, idade, atual))
if idade < 18:
    print('Você vai se alistar no serviço militar daqui a {} ano(s).'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(nasc + 18))
elif idade == 18:
    print('Já está na hora de se alistar!')
else:
    print('Já passou 1 ano do tempo de alistamento.') if idade - 18 == 1 else print('Já passaram {} anos do tempo de alistamento.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(nasc + 18))

#Solução:
# prints extras do prof: 'quem nasceu em....
# seu alistamento será em....
# seu alistamento foi em....'
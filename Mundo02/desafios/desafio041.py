# A Confederação Nacional de Natação previsa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SENIOR
# Acima: MASTER

from datetime import date
nasc = int(input('{}Qual o ano de nascimento do atleta? {}'.format('\033[34m', '\033[m')))
idade = date.today().year - nasc

if idade <= 9: print('Atleta ({} anos) está na categoria {}MIRIM{}.'.format(idade, '\033[32m', '\033[m'))
elif idade <= 14: print('Atleta ({} anos) está na categoria {}INFANTIL{}.'.format(idade, '\033[33m', '\033[m'))
elif idade <= 19: print('Atleta ({} anos) está na categoria {}JUNIOR{}.'.format(idade, '\033[31m', '\033[m'))
elif idade <= 25: print('Atleta ({} anos) está na categoria {}SENIOR{}.'.format(idade, '\033[35m', '\033[m'))
else: print('Atleta ({} anos) está na categoria {}MASTER{}.'.format(idade, '\033[36m', '\033[m'))

#Solução igual ^^
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.
from datetime import date

atual = date.today().year
maior = 0
menor = 0
for p in range(1, 8):
    ano = int(input('Digite o {}º ano de nascimento: '.format(p)))
    if atual - ano >= 21: maior += 1
    else: menor += 1
print(' Analisando os dados... '.center(30, '='))
print('{}Pessoas maiores de idade: {}.{}'.format('\033[33m', maior, '\033[m'))
print('{}Pessoas menores de idade: {}.{}'.format('\033[34m', menor, '\033[m'))

#Solução igual
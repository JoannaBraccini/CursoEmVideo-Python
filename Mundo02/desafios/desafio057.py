# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while 'M' != sexo != 'F':
    # print('ERRO! Por favor digite apenas M ou F.')
    # sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    sexo = str(input('ERRO! Por favor digite apenas M ou F. ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

#Solução:
# [0] -> pega só a primeira letra
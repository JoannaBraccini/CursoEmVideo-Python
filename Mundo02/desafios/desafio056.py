# Desenvolva um programa que leia o nome, idade e sexo de
# quatro pessoas. No final do programa mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos
idade_total = 0
nome_velho = ''
idade_velho = 0
mulheres_jovens = 0
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo not in 'MF': #Encerra o programa para evitar erros
        print('ERRO! Por favor digite apenas M ou F.')
        break
    idade_total += idade #soma idades
    if sexo in 'M': #valida o homem mais velho
        if idade > idade_velho:
            idade_velho = idade
            nome_velho = nome
    elif sexo in 'F': #valida as mulheres com menos de 20 anos
        if idade < 20: mulheres_jovens += 1
print('A média de idade do grupo é {}.'.format(idade_total / 4))
print('O nome do homem mais velho é {} e ele tem {} anos.'.format(nome_velho, idade_velho))
print('{} mulher(es) tem menos de 20 anos.'.format(mulheres_jovens))

#Solução, diferenças:
#dentro do for
# if p == 1 and sexo in 'M':
#     maior_idade = idade
#     nome_velho = nome
# if sexo in 'M' and idade > maior_idade:
#     maior_idade = idade
#     nome_velho = nome
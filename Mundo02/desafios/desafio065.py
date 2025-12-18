# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = cont = soma = maior = menor = 0
continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um valor inteiro: '))
    if not num.is_integer():
        print('Erro, digite um número inteiro.')
        break
    else:
        if cont == 0:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        soma += num
        cont += 1
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar not in 'SN': continuar = 'S'
        if continuar == 'N': print('Finalizando')
media = soma / cont
print('A média entre os {} números digitados é {:.2f}.'.format(cont, media))
print('O maior valor digitado foi {} e o menor foi {}.'.format(maior, menor))

# Solução: certo ^^
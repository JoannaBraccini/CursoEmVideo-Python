# Faça um programa que leia três números e mostre qual é o
# maior e qual é o menor

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

numeros = [n1, n2, n3]
n = sorted(numeros)
# sorted(n) ordena a lista em ordem crescente mas com retorno
# diferente de .sort() que não tem retorno
print('O maior número é {} e o menor é {}'.format(n[2], n[0]))

#Solução
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor foi {} e o maior valor foi {}.'.format(menor, maior))
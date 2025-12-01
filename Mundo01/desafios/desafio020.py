# O mesmo professor do desafio anterior quer sortear a ordem de
# apresentação de trabalhos dos alunos. Faça um programa que leia o
# nome dos quatro alunos e mostre a ordem sorteada.

from random import sample, shuffle

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

lista = [a1, a2, a3, a4]
ordem = sample(lista, 4) # busca aleatoriamente 4 itens da lista

print('A ordem de apresentação dos trabalhos será')
print(ordem)

#Solução
shuffle(lista) # mistura a lista
print(lista) # mostra a lista misturada
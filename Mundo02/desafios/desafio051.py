# Desenvolva um programa que leia o primeiro termo e a
# razão de uma Progressão Aritmética. No final mostre os
# 10 primeiros termos dessa progressão

# matemática: A Progressão Aritmética (P.A.) é uma sequência
# numérica onde a diferença entre termos consecutivos é sempre
# constante, chamada de razão.

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}{}{}'.format('\033[35m', c, '\033[m'), end=' → ')
print('FIM')

#Solução igual
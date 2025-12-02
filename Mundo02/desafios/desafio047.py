# Crie um programa que mostre na tela todos os números PARES
# que estão no intervalo entre 1 e 50.

for c in range(2, 51, 2):
    print('{}{}{}'.format('\033[34m', c, '\033[m'), end=' ')
print('FIM')
#--- ou ----#
for c in range(2, 51):
    if c % 2 == 0:
        print('{}{}{}'.format('\033[33m', c, '\033[m'), end=' ')
print('FIM')

#Solução igual o primeiro, pois o segundo faz mais iterações
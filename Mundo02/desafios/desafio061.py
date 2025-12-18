# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Razão da PA: '))
c = 1
while c <= 10:
    print('{}{} → {}'.format('\033[35m', t, '\033[m'), end='')
    t += r
    c += 1
print('FIM')

# Solução: igual
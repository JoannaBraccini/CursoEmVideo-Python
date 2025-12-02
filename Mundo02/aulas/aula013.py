# Laços: estrutura de repetição for

# for c in range(1, 10):
#     if moeda: pega
#     passo
#     pula
# passo
# pega

for c in range(0, 7, 2): #index
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}.'.format(s))
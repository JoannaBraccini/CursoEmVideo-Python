# Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('{}Digite o {}º valor inteiro: {}'
                    .format('\033[36m', c, '\033[m')))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma dos {}{} números pares{} digitados é {}{}.{}'
      .format('\033[34m', cont, '\033[m', '\033[35m', soma, '\033[m'))

#Solução adicionou contador
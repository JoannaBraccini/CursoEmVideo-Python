# Faça um programa que calcule a SOMA entre todos os
# números ÍMPARES que são múltiplos de TRÊS e que se
# encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('{}A soma de todos os {} valores calculados é {}{}'.format('\033[35m', cont, soma, '\033[m'))

#Solução: adição do contador
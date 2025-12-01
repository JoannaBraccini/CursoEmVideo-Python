# Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km
# para viagens de até 200Km e R$0.45 para viagens mais longas.

dist = float(input('Qual é a distância da sua viagem? '))
pas = 0.50 if dist <= 200 else 0.45
print('Sua passagem vai custar R${:.2f}.'.format(dist * pas))

#Solução
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('Sua passagem vai custar R${:.2f}.'.format(preco))
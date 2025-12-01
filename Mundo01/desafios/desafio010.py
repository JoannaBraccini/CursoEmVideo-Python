# Crie um programa que leia quanto dinheiro uma pessoa tem
# na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1.00 = R$ 3.27

valor = float(input('Quantos reais você tem na carteira? R$ '))
cambio = 3.27

print('Você pode comprar US$ {}'.format(valor/cambio))

#Solução
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(real, dolar))
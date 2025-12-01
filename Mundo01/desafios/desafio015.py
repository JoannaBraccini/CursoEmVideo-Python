# Escreva um programa que pergunte a quantidade de km
# percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$60 por dia e R$0.15 por km rodado

km = float(input('Qual a quilometragem rodada? '))
dias = int(input('Por quantos dias ele foi alugado? '))
vKm = 0.15
vDia = 60
total = (vKm * km) + (vDia * dias)
print('O valor total da fatura é R$ {:.2f}.'.format(total))

#Solução
dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos quilômetros rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}.'.format(pago))

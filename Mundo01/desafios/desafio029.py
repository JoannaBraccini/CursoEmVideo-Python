# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima
# do limite.

vel = float(input('Qual a velocidade atual do veículo? '))
if vel > 80:
    print('MULTADO! Você escedeu o limite de 80km/h')
    print('Sua multa será de R${:.2f}.'.format((vel - 80) * 7))
print('Tenha um bom dia. Dirija com segurança.')

#Solução ok
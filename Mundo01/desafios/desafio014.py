# Escreva um programa que converta uma temperatura digitada
# em °C e converta para °F

celcius = float(input('Qual a temperatua em °C? '))
farenheit = 9 * celcius / 5 + 32
print('{:.2f}°C equivale a {:.2f}°F'.format(celcius, farenheit))

#Solução
c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32
print('A temperatura de {}°C corresponde a {}°F'. format(c, f))
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Qual o seu peso em quilos? '))
alt = float(input('Qual a sua altura em metros? '))
imc = peso / (alt ** 2)
print('O seu IMC é de {:.1f}.'.format(imc))
if imc < 18.5: print('Você está abaixo do peso ideal.')
elif 18.5 <= imc < 25: print('Você está no peso ideal.')
elif 25 <= imc < 30: print('Você está com sobrepeso.')
elif 30 <= imc < 40: print('Você está com obesidade.')
else: print('Você está com obesidade mórbida.')

#Solução
#print extra 'o seu imc é de...'
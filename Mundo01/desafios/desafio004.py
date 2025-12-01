# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.

entrada = input('Digite qualquer coisa: ')
print(type(entrada))
print('É alfabético? ', entrada.isalpha())
print('É numérico? ', entrada.isnumeric())
print('É alfa-numérico? ', entrada.isalnum())
print('Está em minúsculas? ', entrada.islower())
print('Está em maiúsculas? ', entrada.isupper())

# Solução

entrada = input('Digite algo: ')

print('O tipo primitivo desse valor é', type(entrada))
print('Só tem espaços?', entrada.isspace())
print('É um número?', entrada.isnumeric())
print('É alfabético?', entrada.isalpha())
print('É alfanumérico?', entrada.isalnum())
print('Está em maiúsculas?', entrada.isupper())
print('Está em minúsculas?', entrada.islower())
print('Está capitalizado?', entrada.istitle())
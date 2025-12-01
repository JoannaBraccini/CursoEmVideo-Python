# Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo, calcule e mostre o
# comprimento da hipotenusa

# matemática: raiz quad. da soma dos quadrados dos catetos

from math import sqrt, hypot

cat1 = float(input('Qual o valor do cateto oposto? '))
cat2 = float(input('Qual o valor do cateto adjacente? '))
hip = sqrt((cat1 ** 2 + cat2 ** 2))

print('O comprimento da hipotenusa é {:.2f}.'.format(hip))

#Solução 1
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(hi))

#Solução 2
hy = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}.'.format(hy))

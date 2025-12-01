# Faça um programa que leia um ângulo qualquer e mostre na tela o
# valor do seno, cosseno e tangente desse ângulo

#matemática: converter o grau para radiano, depois aplicar os métodos

from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
rad = radians(ang)

print('Dado o âgulo {}, o seno é {:.2f}, o cosseno é {:.2f} e '
      'a tangente é {:.2f}.'
      .format(ang, sin(rad), cos(rad), tan(rad)))

#Solução
seno = sin(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(ang, seno))
cosseno = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(ang, cosseno))
tangente = tan(radians(ang))
print('O ângulo de {} tem a tangente de {:.2f}.'.format(ang, tangente))

# Faça um programa que leia a largura e altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

larg = float(input('Quantos metros a parede tem de largura? '))
alt = float(input('Quantos metros a parede tem de altura? '))
metros = larg * alt
areaPorLitro = 2
tinta = metros / areaPorLitro
print('Você vai precisar de {} litros de tinta para pintar os {}m².'.format(tinta, metros))

#Solução
larg = float(input('Largura da parede em metros: '))
alt = float(input('Altura da parede em metros: '))
area = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisa de {}l de tinta.'.format(tinta))
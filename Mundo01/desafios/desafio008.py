# Escreva um programa que leia um valor em metros e
# exiba o valor convertido em centímetros e mílimetros

medida = float(input('Digite o valor em metros: '))
cent = int(medida * 100)
mil = int(medida * 1000)
print('Conversão de {} metros:\n{} centímetros\n{} milímetros'.format(medida, cent, mil))

#Solução
medida = float(input('Digite uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A distância de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra 'A'
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez

#rfind = encontra a última ocorrência de uma substring dentro da string
frase = str(input('Digite uma frase: ')).strip().upper()

print("""
Frase: {}
A letra 'A' aparece {} vezes
Na primeira vez, aparece na posição {}
Na última vez, aparece na posição {}
""".format(frase.capitalize(), frase.count('A'), frase.find('A'), frase.rfind('A')))

#Solução: prof usa +1 para considerar base 1 e não base 0
print('A primeira letra A aparece na posição {}.'.format(frase.count('A')+1))
print('A última letra A aparece na posição {}.'.format(frase.rfind('A')+1))
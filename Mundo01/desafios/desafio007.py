# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre sua média

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print('A média entre {} e {} é {:.2f}'.format(n1, n2, media))

#Solução
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é {:.1f}'.format(n1, n2, m))
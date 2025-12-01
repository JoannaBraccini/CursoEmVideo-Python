# Faça um programa que leia de 0 a 9999 e mostre na tela
# cada um dos dígitos separados.
# Ex: 1834 -> unidade 4, dezena 3, centena 8 e milhar 1

num = str(input('Digite um número de 0 a 9999: '))

n = num.zfill(4)
# zfill(n) preenche com '0' à esquerda da string até o total de n digitos

print("""
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
""".format(n[3], n[2], n[1], n[0]))

#Solução com inteiro
num = int(input('Informe um número: '))
u = num // 1 % 10 #divido por 1 e pego o resto da divisão por 10
d = num // 10 % 10 #divido por 10 e pego o resto da divisão por 10
c = num // 100 % 10 #divido por 100 e pego o resto da divisão por 10
m = num // 1000 % 10 # divido por 1000 e pego o resto da divisão por 10

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
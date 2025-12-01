#Operadores aritméticos

# Ordem de precedência
# () -> ** -> * / // % -> + -

# raiz quadrada = n1 ** (1/2)
# raiz cúbica = n1 ** (1/3)

nome = input('Qual o seu nome? ')
print('Prazer em te conhecer, {:^20}!'.format(nome))  # centraliza o nome no espaço dado
print('Prazer em te conhecer, {:>20}!'.format(nome))  # identa à direita
print('Prazer em te conhecer, {:<20}!'.format(nome))  # identa à esquerda

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
# Caso queira evitar nova linha, use end: print('A divisão é {}.'.format(d), end=' ')
print('A soma é {}, o produto é {}, e a divisão é {}.'.format(s, m, d))
print('A divisão inteira é {} com resto {} e a potência é {}.'.format(di, r, e))
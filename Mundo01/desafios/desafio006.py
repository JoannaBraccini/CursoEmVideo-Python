# Crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e raiz quadrada

num = int(input('Digite um número inteiro: '))
dobro = num * 2
triplo = num * 3
r = num ** (1/2)
print('O dobro de {} é {}, o triplo é {} e sua raiz quadrada é {}.'.format(num, dobro, triplo, r))

#Solução
n = int(input('Digite um número inteiro: '))
print('O dobro de {} é {}, o triplo é {} e sua raiz quadrada é {:.2f}.'.format(n, (n*2), (n*3), pow(n, (1/2))))

# {:.2f} formata para ter 2 casas depois do ponto flutuante
# raiz quadrada pode ser calculada com função pow(n, (1/2)) ou n**(1/2)
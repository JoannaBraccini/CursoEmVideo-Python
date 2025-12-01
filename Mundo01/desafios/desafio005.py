# Faça um programa que leia um número Inteiro e
# mostre na tela o seu sucessor e seu antecessor

n = int(input('Digite um número inteiro: '))
print('Antecessor: {} \nSeu número: {} \nSucessor: {}'.format((n-1), n, (n+1)))

#Solução

n = int(input('Digite um número inteiro: '))
print('Analisando seu número {}, seu antecessor é {} e seu sucessor é {}.'.format(n, (n-1), (n+1)))
# Crie um script Python que leia dois números e tente
# mostrar a soma entre eles.

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m'}
n1 = int(input('Digite um número {}inteiro{}: '.format(cores['amarelo'], cores['limpa'])))
n2 = int(input('Digite outro número {}inteiro{}: '.format(cores['amarelo'], cores['limpa'])))
soma = n1+n2

# print('A soma é', soma)
print('A {}soma {}é {}'.format(cores['azul'], cores['limpa'] ,soma)) #nova sintaxe

# Solução

n1 = float(input('Digite um número {}real{} (com ponto flutuante): '.format(cores['amarelo'], cores['limpa'])))
n2 = float(input('Digite o segunto número {}real{}: '.format(cores['amarelo'], cores['limpa'])))
soma = n1 + n2

print('A {}soma{} entre {}{}{} e {}{}{} é {}{}{}.'.format(cores['azul'], cores['limpa'], cores['vermelho'], n1, cores['limpa'], cores['vermelho'], n2, cores['limpa'], cores['amarelo'], soma, cores['limpa']))
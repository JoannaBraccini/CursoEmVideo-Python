# Crie um script Python que leia o nome de uma pessoa e
# mostre uma mensagem de boas-vindas de acordo com o
# valor digitado.

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m'}
nome = input('{}Qual é o seu nome? {}'.format(cores['azul'], cores['limpa']))
mensagem = ('Boas vindas ao {}Curso de Python{}, {}!'.format(cores['vermelho'], cores['limpa'], nome
                                                             ))

print(mensagem)

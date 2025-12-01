 # Crie um script Python que leia o dia, o mês e o
 # ano de nascimento de uma pessoa e mostre uma mensagem
 # com a data formatada
cores = {'limpa':'\033[m',
         'roxo':'\033[35m',
         'vermelho':'\033[31m'}
dia = input('Digite o {}dia{} de seu nascimento: '.format(cores['vermelho'], cores['limpa']))
mes = input('Digite o {}mês{} de seu nascimento: '.format(cores['vermelho'], cores['limpa']))
ano = input('Digite o {}ano{} de seu nascimento: '.format(cores['vermelho'], cores['limpa']))

print('{}Você nasceu no dia {} de {} de {}, correto?'.format(cores['roxo'], dia, mes, ano))

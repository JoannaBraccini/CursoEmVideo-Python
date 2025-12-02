# Escreva um programa para aprovar o empréstimo bancário para
# a compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode
# esceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o valor do salário do comprador? R$ '))
anos = int(input('Em quantos anos o empréstimo será pago? '))
prestacao = casa / (anos * 12)
valor = salario * 30 / 100
if prestacao > valor:
    print('{}Empréstimo negado!{} Prestação ultrapassa valor permitido de R${:.2f}.'.format('\033[1;31m', '\033[m', valor))
else:
    print('{}Empréstimo aprovado!{} Você pagará R${:.2f} por mês.'.format('\033[1;32m', '\033[m', prestacao))

#Solução
print('Para pagar uma casa de R${:.2f} em {} anos,'.format(casa, anos))
print('a prestação será de R${:.2f}'.format(prestacao))
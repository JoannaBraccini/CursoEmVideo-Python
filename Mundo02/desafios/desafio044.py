# Elabore um programa que calcule o valor a ser pago por um
# precouto, considerando o seu preço normal e condição de pagamento:
# à vista em dinheiro ou cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco = float(input('{}Qual o valor da compra? R$ '.format('\033[34m')))
cond = int(input('''Qual a forma de pagamento? 
[ 1 ] à vista em dinheiro ou cheque
[ 2 ] à vista no cartão
[ 3 ] em 2x no cartão
[ 4 ] em 3x ou mais no cartão
OPÇÃO: {}'''.format('\033[m')))

if cond == 1:
    total = preco - (preco * 10 / 100)
elif cond == 2:
    total = preco - (preco * 5 / 100)
elif cond == 3:
    total = preco
    parcela = total / 2
    print('{}Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format('\033[33m', parcela))
elif cond == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('{}Quantas parcelas? '.format('\033[34m')))
    parcela = total / totparc
    print('{}Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format('\033[33m', totparc, parcela))
else:
    total = preco
    print('{}Opção inválida.{}'.format('\033[31m', '\033[m'))

print('{}Sua compra de R${:.2f} vai custar R${:.2f} no total.'.format('\033[33m', preco, total))

#Solução
# input extra na opção 4
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

operacao = 4
operador = ''
while operacao == 4:
    valor1 = int(input('Digite um valor: '))
    valor2 = int(input('Digite outro valor: '))
    while operacao != 5:
        print('Escolha qual operação deseja realizar:')
        operacao = int(input("""
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa
        Opção: """))
        if operacao == 1:
            operacao = valor1 + valor2
            operador = '+'
        elif operacao == 2:
            operacao = valor1 * valor2
            operador = 'x'
        elif operacao == 3:
            operador = 'comparado com'
            if valor1 > valor2:
                operacao = valor1
            else:
                operacao = valor2
                print('Calculando...')
        elif operacao == 4:
            break
        sleep(1)
        print('{}{} {} {} = {}{}'.format('\033[34m', valor1, operador, valor2, operacao, '\033[m'))
        print('=-=' * 15)

# Solução:
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor:'))
opcao = 0
while opcao != 5:
    print('''[ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto entre {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2: maior = n1
        else: maior = n2
        print('Entre {} e {}, o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os novos valores:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else: print('Opção inválida. Tente novamente.')
    print('-=' * 10)
    sleep(1)
print('Fim do programa. Volte sempre!')
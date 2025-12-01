# Condições parte 1

# if carro.esquerda():
#     bloco True
# else:
#     bloco False

# if composto padrão
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

# if composto simplificado (ternário like)
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('--FIM--')

# ---------------------
nome = str(input('Qual é o seu nome? '))
if nome == 'Joanna':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

# ---------------------
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('Parabéns!' if m >= 6.0 else 'Estude mais!')

# Crie um programa que leia uma frase qualquer e diga se ela é
# um palíndromo, desconsiderando espaços.

# Exemplo: A base do teto desaba

frase = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(frase)
inverso = ''.join(frase)[::-1]

if junto == inverso:
    print('{}A frase "{}" é um palíndromo!{}'.format('\033[35m', inverso, '\033[m'))
else:
    print('{}A frase "{}" não é um palíndromo...{}'.format('\033[35m', inverso, '\033[m'))

#Solução usando for:
inversa = ''
for letra in range(len(junto) -1, -1, -1):
    inversa += junto[letra]
if inversa == junto: print('PALÍNDROMO')
else: print('Não é palíndromo')
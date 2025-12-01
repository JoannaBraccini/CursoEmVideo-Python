# Crie um programa que leia o nome de uma cidade e diga
# se ela começa ou não com o nome 'SANTO'

cidade = str(input('Digite o nome de uma cidade: ')).strip()
nome = cidade.upper().split()

print('{} começa com SANTO? {}'.format(cidade, nome[0] == 'SANTO'))

#Solução
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')
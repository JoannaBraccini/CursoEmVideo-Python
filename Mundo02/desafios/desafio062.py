# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

# t = int(input('Primeiro termo da PA: '))
# r = int(input('Razão da PA: '))
# c = 1
# while c <= 10:
#     print('{}{}{}'.format('\033[35m', t, '\033[m'),
#           end=' → ' if c < 10 else '')
#     t += r
#     c += 1
#
# e = 1
# while e != 0:
#     q = int(input('\nQuer ver mais quantos termos? '))
#     nc = 1
#     while nc <= q:
#         print('{}{}{}'.format('\033[35m', t, '\033[m'),
#               end=' → ' if nc < q else '')
#         t += r
#         nc += 1
#     if q == 0:
#         e = 0
#         print('Finalizando...')

# Solução:
print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}{} → {}'.format('\033[35m', termo, '\033[m'), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
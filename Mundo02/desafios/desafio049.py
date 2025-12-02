# Refaça o DESAFIO 009, mostrando a tabuada de um número que
# o usuário escolher, só que agora utilizando um laço FOR

num = int(input('Digite um número inteiro para ver a tabuada: '))
print('{}='.format('\033[36m')*14)
for c in range(1,11):
    print('{:2} x {:2} = {}'.format(num, c, num * c))
print('{}='.format('\033[36m')*14)

#Solução igual
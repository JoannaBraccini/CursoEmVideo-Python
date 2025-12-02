# Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

from time import sleep
print('{}Contagem regressiva!{}'.center(20).format('\033[1:33m', '\033[m'))
# 10 inicial, -1 final (pois ele não conta o último), -1 passo de trás pra frente
for c in range(10, -1, -1):
    print('{}{}{}'.center(20).format('\033[34m', c, '\033[m'))
    sleep(1)
print('{}*🎆* Feliz ano novo! *🎆*{}'.center(20).format('\033[1:31m', '\033[m'))

#Solução igual :)
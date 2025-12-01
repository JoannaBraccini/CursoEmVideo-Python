# Cores no terminal

# ANSI escape sequences
# \033[style;text;backm
# \033[0;33;44m

# style: 0=none, 1=bold, 4=underline, 7=negative
# text: 30=black, 31=red, 32=green, 33=yellow, 34=blue, 35=purple, 36=cyan, 37=gray
# back: 40=black, 41=red, 42=green, 43=yellow, 44=blue, 45=purple, 46=cyan, 47=gray

# \033[m = reset
# \033[7;30m = negative text color

print('\033[1;30;47mOlá, Mundo!\033[m')
print('\033[7;35;46mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!'.format(a, b))

nome = 'Joanna'
print('Olá! muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

print('Olá! muito prazer em te conhecer, {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))

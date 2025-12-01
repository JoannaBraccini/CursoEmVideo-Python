# Manipulando Texto

# len => length => len(var) => comprimento da string
# var.count('o',0,13) => quantas vezes aparece a letra 'o' entre 0 e 13
# var.find('deo') => onde começa o trecho buscado (índice)
# 'Curso' in var => dentro da var existe a palavra 'Curso'?
# var.replace('Python','JavaScript') => substitui a palavra Python por JavaScript
# var.upper() => todos caracteres para maiúsculas
# var.lower() => todos caracteres para minúsculas
# var.capitalize() => inicial da string maiúscula, resto minúscula
# var.title() => inicial de cada palavra maiúscula, resto minúscula
# var.strip() => remove os espaços no início e no final da string
# var.rstrip() => remove os espaços no final da string
# var.lstrip => remove os espaços no início da string

# var.split() => separa a string em uma lista
# '-'.join(var) => junta a lista em uma string separada por '-'

frase = 'Curso em Vídeo Python'
print(frase.split())
print('-'.join(frase.split()))

print("""Esta é uma frase muito longa
que pode ocupar várias linhas
no código, mas mantém as quebras de linha.""")

print(frase.count('o'))
print(len(frase))
print(frase.replace('Python','JavaScript'))

print('Curso' in frase)
print(frase.find('deo'))
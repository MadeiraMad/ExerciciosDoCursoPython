from random import choice
a = str(input(' Digite o nome do primeiro aluno: '))
b = str(input(' Digite o nome do segundo aluno: '))
c = str(input(' Digite o nome do terceiro aluno: '))
d = str(input(' Digite o nome do quarto aluno: '))
lista = [a, b, c, d]
print('O aluno escolhido e: ', (choice(lista)))

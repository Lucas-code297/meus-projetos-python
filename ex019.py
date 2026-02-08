# programa que lê o nome de 4 alunos e sorteia um escolhido
from random import choices
n1 = str(input('Nome do(a) primeiro(a) aluno(a): '))
n2 = str(input('Nome do(a) segundo(a) aluno(a): '))
n3 = str(input('Nome do(a) terceiro(a) aluno(a): '))
n4 = str(input('Nome do(a) quarto(a) aluno(a): '))
lista = [n1, n2, n3, n4]
s = choices(lista)
print(f'O(a) aluno(a) escolhido(a) foi: {s}')
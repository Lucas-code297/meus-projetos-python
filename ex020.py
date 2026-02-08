# programa que lê o nome de 4 alunos e sorteia a ordem de apresentação dos alunos
from random import shuffle
n1 = str(input('Digite o nome do(a) primeiro(a) aluno(a): '))
n2 = str(input('Digite o nome do(a) segundo(a) aluno(a): '))
n3 = str(input('Digite o nome do(a) terceiro(a) aluno(a): '))
n4 = str(input('Digite o nome do(a) quarto(a) aluno(a): '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(lista)

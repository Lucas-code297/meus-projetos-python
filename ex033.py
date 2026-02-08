# programa que lê 3 números e diz qual é o maior e qual é o menor
a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
c = int(input('Digite outro número inteiro: '))
if a > b and (a > c):
    print(f'O número {a} é o maior valor!')
if b > a and (b > c):
    print(f'O número {b} é o maior valor!')
if c > a and (c > b):
    print(f'O número {c} é o maior valor!')
if a < b and (a < c):
    print(f'O número {a} é o menor valor!')
if b < c and (b < a):
    print(f'O número {b} é o menor valor!')
if c < b and (c < a):
    print(f'O número {c} é o menor valor!')
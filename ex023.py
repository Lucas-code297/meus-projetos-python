# fazer um programa que leia qualquer número de 0 a 9999 e mostre na tela cada um dos digitos separados
# numero = 1254
# unidade = 4
# dezena = 5
# centena = 2
# milhar = 1
from math import trunc
n = int(input('Digite um número de 0 a 9999: '))
u = n / 1 % 10
d = n / 10 % 10
c = n / 100 % 10
m = n / 1000 % 10
print('-' * 20)
print(f'Unidade: {trunc(u)}')
print(f'Dezena: {trunc(d)}')
print(f'Centena: {trunc(c)}')
print(f'Milhar: {trunc(m)}')
print('-' * 20)
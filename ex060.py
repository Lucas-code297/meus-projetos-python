# fatorial
s = 1
from math import factorial
while s != 'N':
    n = int(input('Digite um valor: '))
    print(f'O fatorial deste número é {factorial(n)}.')
    s = str(input('Deseja continuar? [S/N] ')). upper()
    print('=-' * 15)
print('Programa finalizado.')

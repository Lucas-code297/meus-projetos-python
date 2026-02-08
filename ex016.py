# programa que lê um número real e diz a sua parte inteira
from math import trunc
num = float(input('Digite um número: '))
inteira = trunc(num)
print(f'A parte inteira desse número é {inteira}!')
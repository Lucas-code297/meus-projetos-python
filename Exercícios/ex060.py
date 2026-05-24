from math import factorial
n = int(input('Digite um número inteiro \npara calcular seu fatorial: '))
t = n + 1
print(f'Calculando: {n}! =', end=' ')
while t != 2:
    t -= 1
    print(f'{t}', end=' x ')
print(f'1 = {factorial(n)}')

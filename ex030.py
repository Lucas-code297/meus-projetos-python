# programa que diz se o número é par ou impar
n = int(input('Digite um número inteiro, por gentileza: '))
par = n % 2
if par == 0:
    print(f'O número {n} é um número par!')
else:
    print(f'O número {n} é um número impar!')
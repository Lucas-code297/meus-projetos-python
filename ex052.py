# programa que lê um número inteiro e diz se ele é ou não um número primo
n = int(input('Digite um número inteiro: '))
d = list()
for c in range(1, n+1):
    s = n % c
    if s == 0:
        d.append(s)
if len(d) > 2:
    print(f'O número {n} não é primo!')
elif len(d) == 2:
    print(f'O número {n} é primo!')


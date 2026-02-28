n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[32m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mO número {n} foi divisível {cont} vezes.', end=' ')
if cont == 2:
    print('\nPortanto, É PRIMO!')
else:
    print('\nPortanto, NÃO É PRIMO!')
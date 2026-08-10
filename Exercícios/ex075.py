cont = 0
numeros = (int(input('Digite um valor: ')),
           int(input('Digite outro valor:')),
           int(input('Digite mais um valor:')),
           int(input('Digite o último valor:')))
print(f'Você digitou os valores {numeros}.')
if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado.')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
print('Os valores pares foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
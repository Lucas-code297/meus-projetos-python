# fatorial com a estrutura de repetição 'for'
n = int(input('Digite um valor: '))
for c in range(n-1, 0, -1):
    n = n * c
print(f'O fatorial desse número é {n}.')
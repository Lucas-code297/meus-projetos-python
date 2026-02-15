n = int(input('Digite um número inteiro: '))
print('-=' * 8)
print(f'Tabuada de {n}:')
for c in range(1, 10+1):
    print(f'{n} x {c} = {n * c}')
print('-=' * 8)
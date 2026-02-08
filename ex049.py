# refazendo o exercício 009 utilizando o laço for
print('Farei uma tabuada do número que desejar.')
n = int(input('Digite o número(inteiro) desejado: '))
print('=' * 20)
for c in range(1, 10+1):
    print(f'{n} x {c} = {n*c}')
print('=' * 20)

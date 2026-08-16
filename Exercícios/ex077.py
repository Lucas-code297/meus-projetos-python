palavras = ('MERCADO',
         'ESCOLA',
         'CASA',
         'PAREDE',
         'TINTA',
         'MESA')
for pos in palavras:
    print(f'\nNa palavra {pos} temos: ', end='')
    for letra in pos:
        if letra in 'AEIOU':
            print(letra, end=' ')

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Esses três segmentos PODEM formar um triângulo', end=' ')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print(f'ISÓSCELES')
else:
    print('Esses três segmentos NÃO PODEM formar um triângulo.')
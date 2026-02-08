# complemento do exércio 035, irá mostrar que tipo de triângulo será formado
# equilátero: todos os lados iguais
# isósceles: dois lados iguais
# escaleno: todos os lados diferentes
a = float(input('Digite o comprimento do primeiro segmento: '))
b = float(input('Digite o comprimento do segundo segmento: '))
c = float(input('Digite o comprimento do terceiro segmento: '))
if a + b > c and a + c > b and c + b > a:
    print('Esses três segmentos poderão formar um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Não poderão formar um triângulo.')

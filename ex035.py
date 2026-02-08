# programa que lê o comprimento de 3 retas e diz se elas podem ou não formar um triângulo
a = float(input('Diga o comprimento do primeiro segmento: '))
b = float(input('Diga o comprimento do segundo segmento: '))
c = float(input('Diga o comprimento do terceiro segmento: '))
if a + b > c and (a + c > b and b + c > a):
    print('Esses três segmentos podem formar um triângulo!')
else:
    print('Esses três segmentos não podem formar um triângulo!')

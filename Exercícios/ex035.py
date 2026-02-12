a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Esses três segmento PODEM formar um triângulo!')
else:
    print('Esses três segmentos NÃO podem formar um triângulo!')
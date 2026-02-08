# programa que lê o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# calcula e mostra o comprimento da hipotenusa
from math import hypot
co = float(input('Qual é o comprimento do cateto oposto? '))
ca = float(input('Qual é o comprimento do cateto adjacente? '))
h = hypot(co, ca)
print(f'O comprimento da hipotenusa é {h:.2f}!')
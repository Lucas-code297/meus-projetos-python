from math import hypot
co = float(input('Qual é o comprimento do cateto oposto? '))
ca = float(input('Qual é o comprimento do cateto adjascente? '))
print(f'A hipostenusa vai medir {hypot(ca, co):.2f}')
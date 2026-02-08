# criar um programa que lê algo em metros e converte em centímetros e milímetros
# km hm dam m dm cm mm
# a cada casa avançada, multiplica por 10
# a cada casa voltada, divide por 10
m = float(input('Quantos metros são? '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
c = m * 100
mili = m * 1000
print(f'{km}km.')
print(f'{hm}hm.')
print(f'{dam}dam.')
print(f'{dm}dm.')
print(f'{c}cm.')
print(f'{mili}mm.')
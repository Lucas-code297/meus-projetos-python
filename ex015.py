# programa que calcula alugem de carro
km = float(input('Rodou por quantos km? '))
dias = int(input('Foi alugado por quantos dias? '))
# pagar (dias)
d = dias * 60
# pagar (km)
k = km * 0.15
total = d + k
print(f'O total a pagar é R${total:.2f}!')

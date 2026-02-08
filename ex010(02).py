# programa que lê quanto a pessoa tem na carteira e quantos dólares ela pode comprar
# compra via cartão internacional
dinheiro = float(input('Quanto você deseja investir? '))
cotação = float(input('Quanto está a cotação atualmente do dólar(cartão)? '))
IOF = float(input('Quanto está a taxa IOF atualmente?'))
#calcular a cotação com o IOF
c = cotação * IOF
r = dinheiro / c
print(f'Certo! Você poderá comprar U${r:.2f} via cartão internacional!')
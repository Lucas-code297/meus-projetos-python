# programa que lê quanto a pessoa tem na carteira e diz quantos dólares ela pode comprar (em espécie)
# considerando a cotação do dólar turismo e a taxa IOF
dinheiro = float(input('Quanto você deseja investir? '))
cotação = float(input('Quanto estação a cotação do dólar turismo atualmente(para compra em espécie)? '))
IOF = float(input('Quanto está a taxa IOF? '))
#calculo da cotação com o IOF
c = (cotação * IOF)
d = dinheiro / c
print(f'Certo! Você poderá comprar U${d:.2f} em espécie!')

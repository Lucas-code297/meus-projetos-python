dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos km rodados? '))
pagar = (dias * 60) + (km * 0.15)
print(f'Certo! Você deve pagar R${pagar:.2f}!')
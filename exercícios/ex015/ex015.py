dias = int(input('Por quantas dias o carro foi alugado? '))
km = int(input('Percorreu quantos km? '))
pagar = (dias * 60) + (km * 0.15)
print(f'O valor total a pagar é R${pagar:.2f}!')
viagem = float(input('Qual é a distância da viagem em km? '))
if viagem <= 200:
    preço = viagem * 0.50
    print(f'A viagem custará R${preço:.2f}! Tenha uma ótima viagem!')
else:
    pagar = viagem * 0.45
    print(f'A viagem custará R${pagar:.2f}! Tenha uma ótima viagem!')
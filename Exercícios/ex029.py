velocidade = int(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou o limite de velocidade que é 80Km/h.')
    print(f'Você deve pagar uma multa de de R${multa:.2f}!')
else:
    print('Tudo certo! Tenha uma ótima viagem!')
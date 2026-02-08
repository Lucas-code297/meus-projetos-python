# programa que lê a velocidade de um carro
# caso ele ultrapasse 80km, mostre uma mensagem na tela dizendo que ele foi multado
# a multa vai custar R$7,00 por cada km excedido
velocidade = int(input('Olá! Poderia me informar a velocidade do carro? '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Tudo bem, você está dentro do limite de velocidade')
    print('Tenha uma boa viagem!')
else:
    print('Você foi multada por exceder o limite de velocidade!')
    print(f'Portanto, deve-se pagar uma multa de R${multa:.2f}!')
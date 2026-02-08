# programa que calcula o IMC de uma pessoa
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida
altura = float(input('Qual é a sua altura? '))
peso = float(input('Quanto você pesa? '))
c = peso / (altura ** 2)
if c < 18.5:
    print('Você está abaixo do peso.')
elif c <= 25:
    print('Você está no seu peso ideal.')
elif c <= 30:
    print('Você está um pouco acima do peso.')
elif c <= 40:
    print('Você está em estado de obesidade.')
else:
    print('Você está em estado de obesidade mórbida! Por favor, procure um médico!')
print(f'Seu IMC é {c:.1f}.')

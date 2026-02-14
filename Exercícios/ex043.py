peso = float(input('Qual é o seu peso atual? '))
altura = float(input('Qual é a sua altura? '))
IMC = peso / (altura * altura)
if IMC <= 18.5:
    print(f'Seu IMC é {IMC:.1f}', end=' --> ')
    print('abaixo do peso.')
elif 18.5 < IMC < 25:
    print(f'Seu IMC é {IMC:.1f}', end=' --> ')
    print('peso ideal.')
elif 25 < IMC < 30:
    print(f'Seu IMC é {IMC:.1f}', end=' --> ')
    print('Sobrepeso.')
elif 30 < IMC < 40:
    print(f'Seu IMC é {IMC:.1f}', end=' --> ')
    print('obesidade.')
else:
    print(f'Seu IMC é {IMC:.1f}', end=' --> ')
    print('Obesidade mórbida.')
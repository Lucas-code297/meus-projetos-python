salario = float(input('Qual é o seu salário? R$'))
if salario >= 1250:
    a = salario + ((10 * salario) / 100)
    print(f'Certo! Seu salário passará a ser R${a:.2f}!')
else:
    if salario <= 1250:
        b = salario + ((salario * 15) / 100)
        print(f'Tudo bem! Seu salário passará a ser R${b:.2f}!')
salario = float(input('Qual é o seu salário? R$ '))
novo = salario + ((15 * salario) / 100)
print(f'O salário de R${salario} passará a ser R${novo:.2f} com o aumento de 15%.')
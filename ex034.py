# programa que lê o salário do funcionário e calcula o seu aumento
# para salários superiores a R$1.250,00. Calcular um valor de 10%
# para salários menores ou iguais, um aumento de 15%
salário = float(input('Qual é o salário do funcionário? '))
# para salários superiores
d = (salário * 10) / 100
a = d + salário
# para salários menores ou iguais
di = (salário * 15) / 100
b = salário + di
if salário <= 1.250:
    print(f'Certo! Seu novo salário é R${b:.2f}')
else:
    print(f'Certo! Seu novo salário é R${a:.2f}')
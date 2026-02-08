# programa que lê o salário do funcionário e mostre o seu novo salário com aumento de 15%
salário = float(input('Qual é o salário do funcionário? '))
d = (salário * 15) / 100
a = salário + d
print(f'Certo! Seu novo salário é R${a:.2f}')

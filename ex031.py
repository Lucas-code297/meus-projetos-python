# programa que pergunta a distância da viagem em km
# pergunte o preço e calcule
# tendo em vista que para viagens até 200km, deve-se cobrar R$0,50 por km
# mais que isso, deve-se cobrar R$0,45
viagem = float(input('Qual a distância da viagem? '))
# calculo para viagens até 200km
a = viagem * 0.50
# calculo para viagens acima de 200km
b = viagem * 0.45
if viagem <= 200:
    print(f'Certo! O custo da sua viagem é de R${a:.2f}!')
else:
    print(f'Certo! O custo da sua viagem é de R${b:.2f}!')
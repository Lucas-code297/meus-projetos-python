# programa que calcula o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento
# à vista no dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
print(f'{" LOJAS LUCAS ":=^40}')
produto = float(input('Qual é o valor do produto? R$ '))
print('Abaixo a lista das condições de pagamento:\n ')
print('1 - À vista no dinheiro/cheque;\n'
      '2 - À vista no cartão;\n'
      '3 - Em até 2x no cartão;\n'
      '4 - 3x ou mais no cartão.\n ')
condição = int(input('Digite o número de acordo com a condição deseja: '))
if condição == 1:
    total = produto - (produto * 10 / 100)
elif condição == 2:
    total = produto - (produto * 5 / 100)
elif condição == 3:
    total = produto
    parcela = produto / 2
    print(f'Seu produto parcelado em 2x de R${parcela:.2f} sem juros.')
elif condição == 4:
    total = produto + (produto * 20 / 100)
    totalparcelas = int(input('Serão quantas parcelas? '))
    parcela = total / totalparcelas
    print(f'Seu produto será parcelado em {totalparcelas} de R${parcela:.2f} com juros')
else:
    total = produto
    print('Inválido! Digite um número de acordo com a lista!')
print(f'Sua compra de R${produto:.2f} passará a custar R${total:.2f} no final.')


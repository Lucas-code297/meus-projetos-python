print('-=' * 9, end=' ')
print('LOJA LUCAS', end=' ')
print('-=' * 9)
preço = float(input('Qual é o preço das compras? R$ '))
print('[1] À vista dinheiro/cheque\n'
      '[2] À vista no cartão\n'
      '[3] Em até 2x no cartão;\n'
      '[4] 3x ou mais no cartão.')
op = int(input('Qual será a condição de pagamento? '))
if op == 1:
    total = preço - ((10 * preço) / 100)
    print(f'Certo! Você deve pagar R${total:.2f}! Boas compras.')
elif op == 2:
    total = preço - ((5 * preço) / 100)
    print(f'Tudo bem! Você deve pagar R${total:.2f}! Boas compras.')
elif op == 3:
    total = preço
    parcela = total / 2
    print(f'Certo! Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.')
elif op == 4:
    total = preço + ((preço * 20) / 100)
    totparc = int(input('Quanta parcelas?'))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS.')
else:
    total = preço
    print('Opção inválida!')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
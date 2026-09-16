# conversão de real para dólar
dinheiro_cliente = float(input('Quanto você possui na carteira? R$'))
# impostos (atuais 2026)
dolar_comercial_atual  = 5.14
aliquota_do_IOF = 0.011 #(1,1%)
IOF_do_cartao = 0.0438
spread_do_banco = 0.035 #(3,5%)
# convertendo de real para dolar (dinheiro em especie e considerando impostos citados acima)

# calcular o valor do IOF por dolar
dolar_com_IOF = dolar_comercial_atual * (1 + aliquota_do_IOF)

# converter o valor total
valor_final_em_USD = dinheiro_cliente / dolar_com_IOF

# comprando dolar no cartão (irei considerar o banco nubank)

# Aplicar o spread do banco sobre o dolar
dolar_do_banco = dolar_comercial_atual * (1 + spread_do_banco)

# aplicar o IOF do cartao
dolar_final_com_imposto = dolar_do_banco * (1 + IOF_do_cartao)

# dividir o valor em reais pelo custo final do dolar
valor_em_dolares = dinheiro_cliente / dolar_final_com_imposto

# imprimindo o resultado na tela
print('Valores de acordo com o tipo de conversão:')
print(f'Dinheiro em espécie: US${valor_final_em_USD:.2f}')
print(f'Dinheiro no cartão: US${valor_em_dolares:.2f}')
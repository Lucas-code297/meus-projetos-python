n = int(input('Quanto você tem na carteira? '))
dólar = 5.22
IOF = 0.011
imposto = n * IOF
valor_liquido = n - imposto
conversão = valor_liquido / dólar
print(f'Com R${n:.2f} você consegue comprar U${conversão:.2f}.')
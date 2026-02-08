# programa que le um numero inteiro qualquer e pede para o usuario escolher qual será a base de conversão
# 1 para binário, 2 para octal, 3 para hexadecimal
n = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão:\n'
      '1 - Binário;\n'
      '2 - Octal;\n'
      '3 - Hexadecimal.')
base = int(input('Digite o número de acordo com a base desejada: '))
if base == 1:
    print(f'A conversão para base binária é: {n:b}')
elif base == 2:
    print(f'A conversão para base octal é: {n:o}')
elif base == 3:
    print(f'A conversão para base hexadecimal é: {n:x}')
else:
    print('Digite um número de acordo com a lista!')


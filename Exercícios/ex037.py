n = int(input('Digite um número inteiro: '))
print('[1] converter para BINÁRIO;\n'
      '[2] converter para OCTAL;\n'
      '[3] converter para HEXADECIMAL.')
op = int(input('Digite o número de acordo com a opção desejada: '))
if op == 1:
    print(f'O numéro {n} convertido para binário fica: {bin(n)[2:]}')
if op == 2:
    print(f'O número {n} convertido para octal fica: {oct(n)[2:]}')
if op == 3:
    print(f'O número {n} convertido para hexadecimal fica: {hex(n)[2:]}')
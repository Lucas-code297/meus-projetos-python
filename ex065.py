op = 'S'
cont = média = soma = maior = menor = 0
while op in 'Ss':
    n = int(input('Digite um número inteiro: '))
    cont += 1
    soma += n
    média = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    op = str(input('Deseja continuar? [S/N]')). strip().upper()[0]
print(f'Você digitou {cont} números e a média é {média:.2f}')
print(f'O maior valor é {maior} e o menor valor é {menor}.')
soma = count = 0
for c in range(6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
        count += 1
print(f'A soma dos {count} números pares digitados é {soma}!')
# menor e maior valor
maior = menor = 0
# a = b = 0
# acumuladores
cont = 0
soma = 0
op = 'A'
while op not in 'Nn':
    n = int(input('Digite um número inteiro: '))
    op = str(input('Quer continuar [S/N]? ')).strip().upper()
    cont += 1 # contar quantos números foram digitados
    soma += n
    media = soma / cont # calcula a media dos valores
    if op != 'n' or op != 'N':
        if cont == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
print(f'Você digitou {cont} números e a media deles é {media:.2f}.')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
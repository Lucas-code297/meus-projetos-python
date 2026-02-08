n = cont = soma = 0
n = int(input('Digite um número inteiro (999 condição de parada): '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número inteiro (999 condião de parada): '))
print(f'Você digitou {cont} números e a soma deles é {soma}.')
# gerar 5 valores, colocá-los em uma tupla e dizer qual é o menor e qual é o menor

from random import randint
# contador
cont = maior = menor = 0
print(f'Gerados:', end=' ')
while True:
    gerar = randint(0, 10)
    cont += 1
    tupla = (gerar)
    print(tupla, end=' ')
    if cont == 1:
        maior = gerar
        menor = gerar
    else:
        if gerar > maior:
            maior = gerar
        if gerar < menor:
            menor = gerar
    if cont == 5:
        break
print(f'\nMaior valor gerado: {maior}')
print(f'Menor valor gerado: {menor}')
print('Finalizado.')
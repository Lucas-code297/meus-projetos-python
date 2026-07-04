from random import randint
maior = menor = cont = 0
tupla = []
print(f'Valores sorteados:', end=' ')
while True:
    tupla = [randint(0, 10)]
    cont += 1
    '''tupla = gerar'''
    '''print('Gerados:', end=' ')'''
    print(tupla, end=' ')
    if cont == 1:
        maior = tupla
        menor = tupla
    else:
        if tupla > maior:
            maior = tupla
        if tupla < menor:
            menor = tupla
    if cont == 5:
        break
'''print(tupla)'''
print(f'\nMaior valor sorteado: {maior}')
print(f'Menor valor sorteado: {menor}')
print('Finalizado.')
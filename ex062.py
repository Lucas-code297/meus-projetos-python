# gerador de PA melhorado
from time import sleep
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ➡ ', end=' ' )
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
    if mais == 0:
        print('Finalizando...')
    sleep(1)
print('Programa finalizado.')
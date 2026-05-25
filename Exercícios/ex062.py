print('GERADOR DE PA')
print('-=' * 8)
primeiro = int(input('Qual é o primeiro termo? '))
r = int(input('Qual é a razão? '))
termo = primeiro
mais = 10
total = 0
cont = 1
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end=' --> ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Deseja adicionar quantos termos a mais? '))
print('FIM.')
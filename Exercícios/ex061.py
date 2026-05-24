print('GERADOR DE PA ')
print('-=' * 8)
pt = int(input('Digite o primeiro termo: '))
r = int(input('Qual é a razão? '))
termo = pt + (10 - 1) * r
print(pt, end=' --> ')
while pt != termo:
    pt += r
    print(pt, end=' --> ')
print('FIM.')
#ex 51 com estrutura de repetição while
print('GERADOR DE PA')
print('-=' * 8)
pt = int(input('Qual é o primeiro termo? '))
r = int(input('Qual é a razão? '))
tpa = pt + (10 - 1) * r
print(pt)
while pt != tpa:
    pt += r
    print(pt)
print('FIM.')
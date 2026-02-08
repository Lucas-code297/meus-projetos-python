# programa que lê o primeiro termo e a razão de uma PA.
# no final mostra os 10 primeiros termos dessa progressão
pt = int(input('Qual é o primeiro termo? '))
r = int(input('Qual é a razão? '))
tpa = pt + (10 - 1) * r
for c in range(pt, tpa+r, r):
    pt += r
    print(pt)
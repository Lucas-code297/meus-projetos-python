p = int(input('Qual é o primeiro termo? '))
r = int(input('Qual é a razão? '))
tpa = p + (10 - 1) * r
for c in range(p, tpa+1, r):
    print(c, end=' --> ')
print('FIM.')
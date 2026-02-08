# programa que lê o ano de nascimento de 7 pessoas e no final mostra quantas pessoas atingiram maior idade (21)
# e quantas não atingiram a maior idade
p = list()
m = list()
from datetime  import date
atual = date.today().year
for c in range(7):
    ano = int(input('Em que ano você nasceu? '))
    if atual - ano >= 21:
        p.append(c)
    elif atual - ano < 21:
        m.append(c)
if len(p) >= 0:
    print(f'{len(p)} pessoas atingiram a maior idade.')
if len(m) > 0:
    print(f'{len(m)} pessoas ainda não atingiram a maior idade.')
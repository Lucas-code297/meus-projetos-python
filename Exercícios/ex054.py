d = list()
cont = 0
from datetime import date
atual = date.today().year
for c in range(1, 7+1):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = atual - ano
    if idade < 18:
        d.append(idade)
    else:
        cont += 1
print(f'Ao todo tivemos {len(d)} pessoas menores de idade.')
print(f'Também tivemos {cont} pessoas maiores de idade.')
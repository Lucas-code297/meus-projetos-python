# programa que lê o ano de nascimento de um atleta e diz sua categoria de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER
from datetime import date
ano = int(input('Em que ano você nasceu? '))
atual = date.today().year
categoria = atual - ano
print(f'O atleta tem {categoria} anos.')
if categoria <= 9:
    print('Categoria: MIRIM.')
elif categoria <= 14:
    print('Categoria: INFANTIL.')
elif categoria <= 19:
    print('Categoria: JUNIOR.')
elif categoria <= 25:
    print('Categoria: SÊNIOR.')
else:
    print('Categoria: MASTER.')

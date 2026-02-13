from datetime import date
atual = date.today().year
ano = int(input('Qual seu ano de nascimento? '))
idade = atual - ano
if idade <= 9:
    print('Categoria: MIRIM.')
elif idade <= 14:
    print('Categoria: INFANTIL.')
elif idade <= 19:
    print('Categoria: JUNIOR.')
elif idade <= 25:
    print('Categoria: SÊNIOR.')
else:
    if idade > 25:
        print('Categoria: MASTER.')
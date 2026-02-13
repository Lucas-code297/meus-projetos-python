from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = atual - ano
if idade < 18:
    print(f'Você possui {idade} anos, resta {18 - idade} anos para o seu alistamento.')
elif idade > 18:
    print(f'Você possui {idade} anos, seu alistamento foi em {atual - (idade - 18)}.')
if idade == 18:
    print(f'Você possui {idade} anos. Deve se alistar AGORA!')
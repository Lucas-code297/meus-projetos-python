# programa de alistamento militar
# deve ler o ano de nascimento do usuario e, de acordo com a sua idade, dizer:
# se ele ainda vai se alistar, se já está na hora de se alistar ou se já passou
# deve mostrar também o tempo que falta ou que passou do prazo
from datetime import date
ano = int(input('Em que ano você nasceu? '))
atual = date.today().year
c = atual - ano
if c == 18:
    print('Já está na hora de se alistar!')
elif c < 18:
    print(f'Você nasceu em {ano} e está completando {c} anos em {ano + c}!\n'
          f'Restam apenas {18 - c} anos para seu alistamnto! \n'
          f'Você deve se alistar em {ano + 18}!')
else:
    print(f'Você nasceu em {ano} e está completando {c} anos em {ano + c}!\n'
          f'Sendo assim, já passou do seu ano de alistamento, ocorrido em {ano + 18}!')



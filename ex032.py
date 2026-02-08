# programa que lê qualquer ano e diz se é bissexto
from datetime import date
ano = int(input('Digite um ano (digite 0 se quiser saber do ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or (ano % 400 == 0):
    print(f'O ano {ano} é um ano bissexto!')
else:
    print(f'O {ano} não é um ano bissexto!')
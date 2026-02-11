from time import sleep
print('Digite um ano e direi se é bissexto.')
print('Digite 0 caso queria saber o ano atual')
ano = int(input('Que ano quer analisar? '))
'''a = ano % 4
b = ano % 100
c = ano % 400
print(a, b, c)'''
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é um ano bissexto!')
else:
    print(f'O ano {ano} não é um ano bissexto!')
from time import sleep
print('=' * 20)
print('BRASILEIRÃO')
print('=' * 20)
sleep(1)
# tabela do brasileirão
tupla_timetodos = ('Palmeiras','Flamengo','Fluminense','Atlético-PR','Bragantino','Bahia','Coritiba','São paulo',
                   'Atlético-MG','Corinthians','Cruzeiro','Botafogo','EC Vitória','Internacional','Santos','Grêmio',
                   'Vasco da Gama','Remo','Mirassol','Chapecoense')
print(f'Os 5 primeiros colocados são {tupla_timetodos[0:5]}')
print('=' * 20)
print(f'Os 4 últimos colocados são {tupla_timetodos[-4:]}')
print('=' * 20)
print(f'Os times em ordem alfabética são: {sorted(tupla_timetodos)}')
print('=' * 20)
print(f'O time da Chapecoense está na {tupla_timetodos.index("Chapecoense") + 1}ª posição.')